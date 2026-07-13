from file_handler import FileHandler

class Buffer:
    def __init__(self) -> None:
        self.data: list[str] = []

    def add_data(self, item: str) -> None:
        self.data.append(item)

    def read_data(self) -> list[str]:
        return self.data

    def write_data(self, file_name: str) -> None:
        FileHandler.write_file(file_name, self.data)

# b = Buffer()
# b.add_data("szyfruj tekst")
# b.add_data("kolejny tekst do zaszyfrowania")
# print(b.read_data())
# b.write_data("test_buffer.json")