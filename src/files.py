import json


class JSONManager:
    @staticmethod
    def save_to_json(data: list, filename: str):
        with open(filename, 'w') as file:
            serialized_data = [record.to_dict() for record in data]
            json.dump(serialized_data, file, indent=4, ensure_ascii=False)
        print(f"Data saved to {filename}")

    @staticmethod
    def load_from_json(filename: str) -> list or str:
        with open(filename, 'r') as file:
            serialized_data = json.load(file)

        return serialized_data

