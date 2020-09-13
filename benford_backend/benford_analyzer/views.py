from django.db.transaction import atomic
from rest_framework import viewsets
from rest_framework.response import Response

from .exceptions import (
    IncorrectFileStructureException,
    IncorrectDataException,
    EmptyFileException,
)
from .serializers import DatasetSerializer, DetailDatasetSerializer
from .models import Dataset


class BenfordAnalyzerView(viewsets.ModelViewSet):
    serializer_class = DatasetSerializer

    queryset = Dataset.objects.all()

    http_method_names = ["get", "post"]

    def get_serializer_class(self):
        if self.action == "list":
            return DatasetSerializer
        return DetailDatasetSerializer

    @atomic
    def create(self, request, *args, **kwargs):
        file = request.data.get("file")
        if not file:
            return Response("No file to analyze.", status=400)
        dataset = Dataset.objects.create(file=file)
        try:
            dataset.calculate_benford_distribution()
        except (
            IncorrectFileStructureException,
            IncorrectDataException,
            EmptyFileException,
        ) as error:
            dataset.delete()
            return Response(str(error), status=400)

        return Response(DetailDatasetSerializer(dataset).data)
