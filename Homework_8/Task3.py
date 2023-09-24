# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import csv
import json


def json_to_csv(source_path: str, dst_path: str):
    try:
        with open(source_path, encoding="utf-8") as json_file:
            data: dict = json.load(json_file)

    except FileNotFoundError:
        print("File not found!")
        exit(0)
    csv_data = []

    for level, user in data.items():
        for id, name in user.items():
            csv_data.append({"level": level,
                             "id": id,
                             "name": name})
    with open(dst_path, "w", newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=["level", "id", "name"])
        csv_writer.writeheader()
        csv_writer.writerows(csv_data)

    # Вариант без DictWriter
    # with open(dst_path, "w", newline='', encoding="utf-8") as csv_file:
    #     writer = csv.writer(csv_file)
    #     writer.writerow(data.keys())
    #     writer.writerow(data.values())


if __name__ == "__main__":
    json_to_csv('task2.json', 'task3.csv')
