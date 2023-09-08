# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from pathlib import Path
import Task1 as t1
import Task2 as t2
import Task3 as t3
import Task4 as t4


def files_in_folder(dir_name: str, file_name: str):
    full_path = Path(dir_name)
    if not full_path.exists():
        Path.mkdir(full_path)
    else:
        cnt = 1
        while full_path.exists():
            stem = full_path.stem
            new_stem = stem + str(cnt)
            new_path = full_path.with_stem(new_stem)
            full_path.rename(new_path)
            cnt += 1

    t1.fill_file(10, full_path)
    t2.pseudonyms(full_path)


if __name__ == "__main__":
    files_in_folder("C:\\Users\\Zinovev.MI\\Desktop\\", "task6.txt")

