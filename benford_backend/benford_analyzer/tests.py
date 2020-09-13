import os
import tempfile

from django.core.files import File
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings

from .exceptions import (
    IncorrectFileStructureException,
    IncorrectDataException,
    EmptyFileException,
)
from .models import Dataset


files_path = os.path.join(settings.BASE_DIR, "benford_analyzer/test_data/")


class DatasetTestCase(TestCase):
    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_correct_file_is_analyzed(self):
        file_content = File(open(f"{files_path}correct")).read()
        mock_file = SimpleUploadedFile("correct", bytes(file_content, "utf-8"))
        dataset = Dataset.objects.create(file=mock_file)
        dataset.calculate_benford_distribution()
        assert dataset.distribution_match == True
        assert dataset.graph is not None
        assert dataset.statistics.count() == 9

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_not_benford_file_is_analyzed(self):
        file_content = File(open(f"{files_path}not_benford_data")).read()
        mock_file = SimpleUploadedFile("not_benford_data", bytes(file_content, "utf-8"))
        dataset = Dataset.objects.create(file=mock_file)
        dataset.calculate_benford_distribution()
        assert dataset.distribution_match == False
        assert dataset.graph is not None
        assert dataset.statistics.count() == 9

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_analyze_failes_when_column_is_missing(self):
        file_content = File(open(f"{files_path}missing_column")).read()
        mock_file = SimpleUploadedFile("missing_column", bytes(file_content, "utf-8"))
        dataset = Dataset.objects.create(file=mock_file)
        with self.assertRaises(IncorrectFileStructureException):
            dataset.calculate_benford_distribution()

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_analyze_failes_when_data_not_integers(self):
        file_content = File(open(f"{files_path}incorrect_data")).read()
        mock_file = SimpleUploadedFile("icorrect_data", bytes(file_content, "utf-8"))
        dataset = Dataset.objects.create(file=mock_file)
        with self.assertRaises(IncorrectDataException):
            dataset.calculate_benford_distribution()

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_analyze_failes_when_some_data_is_empty(self):
        file_content = File(open(f"{files_path}empty_data")).read()
        mock_file = SimpleUploadedFile("empty_data", bytes(file_content, "utf-8"))
        dataset = Dataset.objects.create(file=mock_file)
        with self.assertRaises(IncorrectDataException):
            dataset.calculate_benford_distribution()

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory().name)
    def test_analyze_failes_when_given_empty_file(self):
        file_content = File(open(f"{files_path}empty_file")).read()
        mock_file = SimpleUploadedFile("empty_file", bytes(file_content, "utf-8"))
        dataset = Dataset.objects.create(file=mock_file)
        with self.assertRaises(EmptyFileException):
            dataset.calculate_benford_distribution()
