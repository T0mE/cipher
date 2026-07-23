from cipher import Rot13, Rot47
from file_handler import FileHandler
from buffer import Buffer
from model import Data

class Facade:

    def __init__(self):
        self.buffer = Buffer()

    def encrypt_rot13(self, text: str) -> None:
        self.buffer.add_data(Data(text=Rot13.encrypt(text),rot_type="rot13",status="encrypt"))

    def decrypt_rot13(self, text: str) -> None:
        self.buffer.add_data(Data(text=Rot13.decrypt(text),rot_type="rot13",status="decrypt"))

    def encrypt_rot47(self, text: str) -> None:
        self.buffer.add_data(Data(text=Rot47.encrypt(text),rot_type="rot47",status="encrypt"))

    def decrypt_rot47(self, text: str) -> None:
        self.buffer.add_data(Data(text=Rot47.decrypt(text),rot_type="rot47",status="decrypt"))

    def save_to_file(self, file_name: str) -> None:
        return self.buffer.write_data(file_name)

    def get_buffer(self) -> list[Data]:
        return self.buffer.read_data()

    def load_from_file(self, file_name: str) -> None:
        data = FileHandler.read_file(file_name)
        for item in data:
            self.buffer.add_data(Data(text=item['text'],rot_type=item['rot_type'],status=item['status']))

# f = Facade()
# f.encrypt_rot13("Ala ma kota")
# f.encrypt_rot47("Ala ma kota")
# print(f.get_buffer())
# f.save_to_file("Test_facade.json")
