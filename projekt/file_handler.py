import json
import os
from dataclasses import asdict


class FileHandler:

    @staticmethod
    def read_file(file_name: str) -> list[str] | None :
        try:
            with open(file_name) as my_file:
                data = json.load(my_file)
                return data['data']
        except FileNotFoundError:
            print("Plik nie istnieje")
        except json.JSONDecodeError:
            print("Plik nie jest poprawnym JSON")

    @staticmethod
    def write_file(file_name: str, data: list[str]) -> None:
        exists_json = []
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                exists_json = json.load(f).get('data', [])

        data_to_json = [asdict(value) if not isinstance(value, dict) else value for value in data]
        exists_json.extend(data_to_json)

        with open(file_name, 'w') as f:
            json.dump({'data': exists_json}, f)
