class IncorrectFileStructureException(Exception):
    def __init__(self, column_name):
        super().__init__(f"Identifier column '{column_name}' is missing.")


class IncorrectDataException(Exception):
    def __init__(self, column_name):
        super().__init__(
            f"Incorrect data. Only integers in '{column_name}' column allowed."
        )


class EmptyFileException(Exception):
    def __init__(self):
        super().__init__(f"The file is empty.")


class IncorrectFileException(Exception):
    def __init__(self):
        super().__init__(f"Incorrect file. Only flat text files are accepted.")
