import somemodule as sm

bottom_num = int(input("Введите нижнее число диапазона: "))
top_num = int(input("Введите верхнее число диапазона: "))
attempts_num = int(input("Введите количество попыток: "))

sm.guess_number(bottom_num, top_num, attempts_num)