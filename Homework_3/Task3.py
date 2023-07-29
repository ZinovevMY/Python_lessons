# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

import itertools as it


def equip_layout(capacity: int | float, equipment: dict) -> dict:
    res_dict ={}
    summ = 0
    for k, v in it.product(equipment, repeat=len(equipment)):
        summ += v
        if summ <= capacity:
            res_dict[k] = v
    return res_dict


def equip_all_layouts():
    pass


backpack_capacity = 15
equipment = {"спальный мешок": 1, "палатка": 3, "плитка": 1.5, "сапоги": 0.5, "тушенка": 3,
             "крупа": 2, "макароны": 2, "топор": 1, "вода": 4, "теплая одежда": 3, "одеяло": 2, "канат": 1.5}

equip_backpack = equip_layout(backpack_capacity, equipment)
print(equip_backpack.items())