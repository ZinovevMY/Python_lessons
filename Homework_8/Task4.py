# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.
import csv
import hashlib
import json


def read_csv(src_path: str, dst_path: str):
    try:
        with open(src_path, encoding="utf-8") as file:
            data = list(csv.reader(file))
            del data[0]
            for i in range(len(data)):
                data[i][0] = data[i][0] + "0" * (10 - len(data[i][0]))
                data[i][2] = data[i][2].capitalize()
                hash_data = data[i][1] + data[i][2]
                hash_obj = hashlib.md5(hash_data.encode())
                data[i].append(hash_obj.hexdigest())
        with open(dst_path, "a") as json_file:
            json_dict: dict = {}
            json_data: list = []
            for i in range(len(data)):
                key = data[i][0]
                if key not in json_dict:
                    json_dict[key] = {}
                json_dict[key] = (data[i][1:])
                json_data.append({k: v for k, v in json_dict.items()})
                json_dict.clear()
            json.dump(json_data, json_file, indent=2)
    except FileNotFoundError:
        print("File not found!")
        exit(0)


if __name__ == "__main__":
    read_csv("task3.csv", "task4.json")
