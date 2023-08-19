import somemodule as sm

bottom_num = int(input("Введите нижнее число диапазона: "))
top_num = int(input("Введите верхнее число диапазона: "))
attempts_num = int(input("Введите количество попыток: "))

is_guessed = sm.guess_number(bottom_num, top_num, attempts_num)
if is_guessed:
    print("Угадал")
else:
    print("Не угадал")