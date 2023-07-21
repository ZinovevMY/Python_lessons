# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

MIN_PERCENT = 30
MAX_PERCENT = 600
LUXURY_BALANCE = 5000000

def start_menu():
    print("Выберите операцию:\n"
          "1. Показать баланс\n"
          "2. Внести деньги на счет\n"
          "3. Снять деньги со счета\n"
          "4. Завершить обслуживание\n")
    return int(input("-> "))


def decrease_percent(balance: int):
    return int(balance * 1.5 / 100)


def accrue_dividend(balance):
    return int(balance * 3 / 100)


def luxury_tax(balance):
    tax = 0
    if balance > LUXURY_BALANCE:
        tax = int(balance / 10)
        print(f"Начислен налог на роскошь в размере {tax} у.е.")
    return tax


def increase_balance(balance: int, operation_counter: int):
    while True:
        increase_summ = int(input("Укажите сумму для пополнения (кратно 50): "))
        if increase_summ % 50 != 0:
            print("Указана неверная сумма!")
        else:
            if operation_counter % 3 == 0:
                dividend = accrue_dividend(balance)
                print(f"Начислены проценты в размере {dividend} у.е.")
                increase_summ += dividend
            return increase_summ


def decrease_balance(balance: int, operation_counter: int):
    dividend = 0
    percent = 0
    while True:
        decrease_summ = int(input("Укажите сумму для снятия (кратно 50): "))
        if decrease_summ % 50 != 0:
            print("Указана неверная сумма!")
        elif decrease_summ > balance:
            print("Недостаточно средств на счете!")
        else:
            percent = decrease_percent(balance)
            if percent < MIN_PERCENT:
                percent = 30
            elif percent > MAX_PERCENT:
                percent = 600
        if operation_counter % 3 == 0:
            dividend = accrue_dividend(balance)
            print(f"Начислены проценты в размере {dividend} у.е.")
        return decrease_summ + percent + dividend


def show_balance(balance: int):
    print(f"На вашем счете {balance} у.е.")


balance = 0
op_counter = 0

while True:
    operation = start_menu()
    match operation:
        case 1:
            show_balance(balance)
        case 2:
            if luxury_tax(balance) > 0:
                balance -= luxury_tax(balance)
                show_balance(balance)
            balance += increase_balance(balance, op_counter)
            op_counter += 1
            show_balance(balance)
        case 3:
            if luxury_tax(balance) > 0:
                balance -= luxury_tax(balance)
                show_balance(balance)
            balance -= decrease_balance(balance, op_counter)
            op_counter += 1
            show_balance(balance)
        case 4:
            exit()
