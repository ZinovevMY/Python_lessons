# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle


def pickle_reader(file_path: str):
    res = b''
    with open(file_path) as file:
        pickle_str = csv.reader(file)
        for row in pickle_str:
            res += pickle.dumps(row)
        print(res)


pickle_reader("task6.csv")
