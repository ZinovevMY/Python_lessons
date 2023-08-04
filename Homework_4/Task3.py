# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

MIN_PERCENT = 30
MAX_PERCENT = 600
LUXURY_BALANCE = 5000000

def start_menu():
    print("Выберите операцию:\n"
          "1. Показать баланс\n"
          "2. Внести деньги на счет\n"
          "3. Снять деньги со счета\n"
          "4. История зачислений/списаний\n"
          "5. Завершить обслуживание\n")
    return int(input("-> "))


def decrease_percent(balance: int):
    return int(balance * 1.5 / 100)


def accrue_dividend(balance):
    return int(balance * 3 / 100)


def luxury_tax(balance):
    tax = int(balance / 10)
    print(f"Начислен налог на роскошь в размере {tax} у.е.")
    return tax


def increase_balance(balance: int, operation_counter: int):
    while True:
        increase_summ = int(input("Укажите сумму для пополнения (кратно 50): "))
        if increase_summ % 50 != 0:
            print("Указана неверная сумма!")
        else:
            if operation_counter > 0 and operation_counter % 3 == 0:
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
        else:
            percent = decrease_percent(balance)
            if percent < MIN_PERCENT:
                percent = 30
            elif percent > MAX_PERCENT:
                percent = 600
            decrease_summ += percent
        if decrease_summ > balance:
            print(f"Недостаточно средств на счете! Снимаемая сумма с учетом комиссии составляет {decrease_summ} у.е.")
            decrease_summ = 0
            return decrease_summ
        if operation_counter > 0 and operation_counter % 3 == 0:
            dividend = accrue_dividend(balance)
            print(f"Начислены проценты в размере {dividend} у.е.")
        return decrease_summ - dividend


def show_balance(balance: int):
    print(f"На вашем счете {balance} у.е.")


balance = 0
op_counter = 0
enrollment_log = []
inc_bal = 0
dec_bal = 0

while True:
    operation = start_menu()
    match operation:
        case 1:
            show_balance(balance)
        case 2:
            if balance > LUXURY_BALANCE:
                tax = luxury_tax(balance)
                balance -= tax
                enrollment_log.append(-tax)
                show_balance(balance)
            inc_bal = increase_balance(balance, op_counter)
            balance += inc_bal
            enrollment_log.append(inc_bal)
            op_counter += 1
            show_balance(balance)
        case 3:
            if balance > LUXURY_BALANCE:
                tax = luxury_tax(balance)
                balance -= tax
                enrollment_log.append(-tax)
                show_balance(balance)
            dec_bal = decrease_balance(balance, op_counter)
            balance -= dec_bal
            enrollment_log.append(-dec_bal)
            op_counter += 1
            show_balance(balance)
        case 4:
            print(enrollment_log)
        case 5:
            exit()