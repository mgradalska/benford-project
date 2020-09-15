import os
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from .exceptions import (
    IncorrectFileStructureException,
    IncorrectDataException,
    EmptyFileException,
    IncorrectFileException,
)
from .models import Dataset


files_path = os.path.join(settings.BASE_DIR, "benford_analyzer/test_data/")


class DatasetTestCase(TestCase):
    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_correct_file_is_analyzed(self):
        with open(f"{files_path}correct", "rb") as f:
            file_content = f.read()
            mock_file = SimpleUploadedFile("correct", file_content)
            dataset = Dataset.objects.create(file=mock_file)
            dataset.calculate_benford_distribution()
            assert dataset.distribution_match == True
            assert dataset.graph is not None
            assert dataset.statistics.count() == 9

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_not_benford_file_is_analyzed(self):
        with open(f"{files_path}not_benford_data", "rb") as f:
            file_content = f.read()
            mock_file = SimpleUploadedFile("not_benford_data", file_content)
            dataset = Dataset.objects.create(file=mock_file)
            dataset.calculate_benford_distribution()
            assert dataset.distribution_match == False
            assert dataset.graph is not None
            assert dataset.statistics.count() == 9

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_analyze_failes_when_column_is_missing(self):
        with open(f"{files_path}missing_column", "rb") as f:
            file_content = f.read()
            mock_file = SimpleUploadedFile("missing_column", file_content)
            dataset = Dataset.objects.create(file=mock_file)
            with self.assertRaises(IncorrectFileStructureException):
                dataset.calculate_benford_distribution()

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_analyze_failes_when_data_not_integers(self):
        with open(f"{files_path}incorrect_data", "rb") as f:
            file_content = f.read()
            mock_file = SimpleUploadedFile("icorrect_data", file_content)
            dataset = Dataset.objects.create(file=mock_file)
            with self.assertRaises(IncorrectDataException):
                dataset.calculate_benford_distribution()

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_analyze_failes_when_some_data_is_empty(self):
        with open(f"{files_path}empty_data", "rb") as f:
            file_content = f.read()
            mock_file = SimpleUploadedFile("empty_data", file_content)
            dataset = Dataset.objects.create(file=mock_file)
            with self.assertRaises(IncorrectDataException):
                dataset.calculate_benford_distribution()

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_analyze_failes_when_given_empty_file(self):
        with open(f"{files_path}empty_file", "rb") as f:
            file_content = f.read()
            mock_file = SimpleUploadedFile("empty_file", file_content)
            dataset = Dataset.objects.create(file=mock_file)
            with self.assertRaises(EmptyFileException):
                dataset.calculate_benford_distribution()

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_analyze_failes_when_given_incorrect_file(self):
        with open(f"{files_path}incorrect_file.png", "rb") as f:
            file_content = f.read()
            mock_file = SimpleUploadedFile("incorrect_file", file_content)
            dataset = Dataset.objects.create(file=mock_file)
            with self.assertRaises(IncorrectFileException):
                dataset.calculate_benford_distribution()
