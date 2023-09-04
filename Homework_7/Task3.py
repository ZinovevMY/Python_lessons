# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

def file_comparator(filename1: str, filename2: str, output_file: str):
    with (
            open(filename1, encoding='utf-8') as nums_file,
            open(filename2, encoding='utf-8') as names_file,
            open(output_file, 'a', encoding='utf-8') as res_file
    ):

        names = names_file.read().split('\n')
        nums = nums_file.read().split('\n')
        if names[-1] == "":
            names.remove(names[-1])
        if nums[-1] == "":
            nums.remove(nums[-1])
        if len(names) > len(nums):
            nums += [nums[i % len(nums)] for i in range(len(nums), len(names))]
        elif len(names) < len(nums):
            names += [names[i % len(names)] for i in range(len(names), len(nums))]
        for i in range(len(names)):
            numbers = [num for num in nums[i].split("|")]
            if float(numbers[0]) * float(numbers[1]) > 0:
                res_file.write(f'{names[i].upper()} {float(numbers[0]) * float(numbers[1]): .2f}\n')
            else:
                res_file.write(f'{names[i].lower()} {float(numbers[0]) * float(numbers[1]): .2f}\n')


if __name__ == "__main__":
    file_comparator("task1_text.txt", "task2_text.txt", "task3_text.txt")
