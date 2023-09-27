# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import pickle


def pickle_to_csv(file_path: str, dst_path: str):
    with open(file_path, 'rb') as p_file:
        csv_dict = pickle.load(p_file)
    csv_headers = []
    csv_data = []
    for item in csv_dict:
        for k, v in item.items():
            csv_headers.append(k)
            csv_data.append({k: v})
    with open(dst_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        csv_writer.writeheader()
        csv_writer.writerows(csv_data)
        print(csv_data)


if __name__ == "__main__":
    pickle_to_csv("task4.pickle", "task6.csv")
