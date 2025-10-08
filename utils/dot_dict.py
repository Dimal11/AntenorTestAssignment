import json
from config import BASE_DIR

DATA_DIR = BASE_DIR / "data_set"

class DotDict:

    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                value = DotDict(value)
            self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def __repr__(self):
        return f"<DotDict {self.__dict__}>"


def load_file_data(file_name: str) -> DotDict:
    path = DATA_DIR / file_name
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return DotDict(data)