# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.
import json


def users_to_json(file_path: str):
    while True:
        user_name = input("Введите имя (для выхода введите exit): ")
        if user_name == "exit":
            break
        user_id = input("Введите идентификатор (для выхода введите exit): ")
        if user_id == "exit":
            break
        user_access = input("Введите уровень доступа от 1 до 7 (для выхода введите 0): ")
        if user_access == "0":
            break
        try:
            with open(file_path, encoding="utf-8") as read_file:
                file_data = json.load(read_file)
        except:
            file_data: dict = {str(i): {}for i in range(1, 8)}

        file_data[user_access].update({user_id: user_name})
        with open(file_path, "w", encoding="utf-8") as write_file:
            json.dump(file_data, write_file, indent=2)


if __name__ == "__main__":
    users_to_json("task2.json")
