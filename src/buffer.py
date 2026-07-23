from file_handler import FileHandler
from model import Data


class Buffer:
    def __init__(self) -> None:
        self.data: list[Data] = []

    def add_data(self, item: Data) -> None:
        if not isinstance(item, Data):
            raise TypeError('Data must be Data object.')
        self.data.append(item)

    def read_data(self) -> list[Data]:
        return self.data

    def write_data(self, file_name: str) -> None:
        FileHandler.write_file(file_name, self.data)
