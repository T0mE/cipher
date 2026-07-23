from typing import TYPE_CHECKING
import json
import os
from dataclasses import asdict

if TYPE_CHECKING:
    from model import Data


class FileHandler:
    DIR = "data"

    @staticmethod
    def create_file_path(file_name: str):
        return f"{FileHandler.DIR}/{file_name}"

    @staticmethod
    def read_file(file_name: str) -> list[dict[str, str]] | None :
        file_path = FileHandler.create_file_path(file_name)
        try:
            with open(file_path) as my_file:
                data = json.load(my_file)
                return data['data']
        except FileNotFoundError:
            print("Plik nie istnieje")
        except json.JSONDecodeError:
            print("Plik nie jest poprawnym JSON")

    @staticmethod
    def write_file(file_name: str, data: list["Data"]) -> None:
        file_path = FileHandler.create_file_path(file_name)
        exists_json = []
        if os.path.exists(file_name):
            with open(file_path, 'r') as f:
                exists_json = json.load(f).get('data', [])

        data_to_json = [asdict(value) if not isinstance(value, dict) else value for value in data]
        exists_json.extend(data_to_json)

        with open(file_path, 'w') as f:
            json.dump({'data': exists_json}, f, indent=4)
