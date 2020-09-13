from rest_framework import serializers

from .models import Dataset, FirstNumberStatistic


class FirstNumberStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstNumberStatistic
        fields = (
            "number",
            "percentage",
        )

    percentage = serializers.SerializerMethodField()

    @staticmethod
    def get_percentage(character_statistic):
        return f"{round(character_statistic.percentage * 100, 2)}%"


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ("id", "file", "graph", "distribution_match")


class DetailDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = DatasetSerializer.Meta.fields + ("statistics",)

    statistics = FirstNumberStatisticSerializer(many=True, required=False)
