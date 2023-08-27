# Задача: Расчет финансовых показателей портфеля акций
# Описание задачи:
# Вы являетесь инвестором и хотите создать программу для расчета нескольких финансовых показателей вашего портфеля акций.
# Создайте модуль Python под названием "portfolio.py", который будет содержать функции для выполнения следующих операций:
# Расчет общей стоимости портфеля акций:
# Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float принимает два аргумента: stocks - словарь,
# где ключами являются символы акций (например, "AAPL" для Apple Inc.), и значениями - количество акций каждого символа.
# prices - словарь, где ключами являются символы акций, а значениями - текущая цена каждой акции.
# Функция должна вернуть общую стоимость портфеля акций на основе количества акций и их текущих цен.
# Пример: Пришло
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
# Вышло:
# 16410,25
# Расчет доходности портфеля:
# Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float принимает два аргумента:
# initial_value - начальная стоимость портфеля акций. current_value - текущая стоимость портфеля акций.
# Функция должна вернуть процентную доходность портфеля. Пример:
# Пришло:
# 10000.0
# 15000.0
# Вышло:
# 50%
# Определение наиболее прибыльной акции:
# Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str принимает два аргумента:
# stocks - словарь с акциями и их количеством. prices - словарь с акциями и их текущими ценами.
# Функция должна вернуть символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью.
# Начальная стоимость - первый вызов calculate_portfolio_value,
# данные из этого вызова следует сохранить в защищенную переменную на уровне модуля.
# Пример:
# Пришло:
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
# Вышло:
# MSFT

def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    summary = 0
    for k, v in stocks.items():
        summary += v * prices.get(k)
    return summary


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    delta_value = current_value - initial_value
    profitability = (delta_value / initial_value) * 100
    return profitability


def get_most_profitable_stock(start_prices: dict, current_prices: dict) -> str:
    price_delta = 0
    company = ''
    for k, v in start_prices.items():
        if k in current_prices:
            if (current_prices[k] - start_prices[k]) > price_delta:
                company = k
    return company


if __name__ == "__main__":
    start_stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    start_prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
    current_stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    current_prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}

    initial_value = calculate_portfolio_value(start_stocks, start_prices)
    current_value = calculate_portfolio_value(current_stocks, current_prices)
    profitability = calculate_portfolio_return(initial_value, current_value)
    profit_company = get_most_profitable_stock(start_prices, current_prices)

    print(initial_value)
    print(current_value)
    print(f'{profitability: .2f}%')
    print(profit_company)
