from django.core import validators
from django.db import models
from django.core.files.images import ImageFile

import pandas as pd
import matplotlib
from io import BytesIO
from scipy.stats import chisquare

from .exceptions import (
    IncorrectFileStructureException,
    IncorrectDataException,
    EmptyFileException,
)

matplotlib.use("Agg")


class BenfordDistribution:
    DISTRIBUTION = {
        1: 0.31,
        2: 0.176,
        3: 0.125,
        4: 0.097,
        5: 0.079,
        6: 0.067,
        7: 0.058,
        8: 0.051,
        9: 0.046,
    }


class Dataset(models.Model):
    IDENTIFIER_COLUMN = "7_2009"

    SIGNIFICANCE_LEVEL = 0.95

    file = models.FileField(upload_to="datasets")

    created = models.DateTimeField(auto_now_add=True)

    graph = models.ImageField(upload_to="images", null=True)

    distribution_match = models.BooleanField(default=False)

    def calculate_benford_distribution(self):
        first_number_percentages = self._calculate_distribution()
        self._set_statistics(first_number_percentages)
        graph = self._generate_graph(first_number_percentages)
        self.graph.save(f"{self.id}_graph.png", ImageFile(graph))
        self.distribution_match = self._chi_square_test(first_number_percentages)
        self.save()

    def _calculate_distribution(self):
        try:
            dataframe = pd.read_csv(self.file.path, sep="\t")
        except pd.errors.EmptyDataError:
            raise EmptyFileException()
        if self.IDENTIFIER_COLUMN not in dataframe:
            raise IncorrectFileStructureException(self.IDENTIFIER_COLUMN)
        first_number_counts = self._calculate_first_number_appearances(dataframe)
        first_number_percentages = first_number_counts.map(
            lambda val: round(val / first_number_counts.sum(), 4)
        )
        return first_number_percentages

    def _calculate_first_number_appearances(self, dataframe):
        first_number_counts = dataframe.assign(
            first_number=lambda frame: frame[self.IDENTIFIER_COLUMN].map(
                lambda value: self._get_first_digit(value)
            )
        ).first_number.value_counts()
        first_number_counts = self._fill_missing_numbers(first_number_counts)
        return first_number_counts[BenfordDistribution.DISTRIBUTION.keys()]

    @staticmethod
    def _fill_missing_numbers(first_number_counts_from_data):
        first_numbers = set(first_number_counts_from_data.index.values)
        missing_numbers = set(BenfordDistribution.DISTRIBUTION.keys()) - set(
            first_numbers
        )
        return first_number_counts_from_data.append(
            pd.Series([0] * len(missing_numbers), index=list(missing_numbers))
        )

    @staticmethod
    def _generate_graph(distribution):
        graph = BytesIO()
        graph_data = pd.DataFrame(
            {
                "Belford's distribution": pd.Series(BenfordDistribution.DISTRIBUTION),
                "Given data": distribution,
            }
        )
        graph_data.plot(kind="bar").get_figure().savefig(graph)
        return graph

    def _set_statistics(self, statistics):
        for index, value in statistics.iteritems():
            FirstNumberStatistic.objects.create(
                number=index, percentage=value, dataset=self
            )

    def _get_first_digit(self, number):
        if not isinstance(number, int):
            raise IncorrectDataException(self.IDENTIFIER_COLUMN)
        return int(str(number)[0])

    def _chi_square_test(self, ditribution):
        result = chisquare(
            ditribution.values, list(BenfordDistribution.DISTRIBUTION.values())
        )
        return result.pvalue > self.SIGNIFICANCE_LEVEL


class FirstNumberStatistic(models.Model):
    number = models.DecimalField(
        decimal_places=0,
        max_digits=1,
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(9)],
    )

    percentage = models.DecimalField(decimal_places=4, max_digits=5)

    dataset = models.ForeignKey(
        Dataset, related_name="statistics", on_delete=models.CASCADE
    )
