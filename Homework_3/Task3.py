# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

import itertools as it


def equip_layout(capacity: int | float, equipment: dict) -> dict:
    res_dict = {}
    summ = 0
    for k, v in equipment.items():
        summ += v
        if summ <= capacity:
            res_dict[k] = v
    return res_dict


def get_all_variants(equipment: dict) -> tuple:
    s = list(equipment)
    return it.chain.from_iterable(it.combinations(s, r) for r in range(1, len(s) + 1))


def equip_variant(equipment_list: list, equipment: dict, capacity: int | float) -> dict:
    result = {}
    summ = 0
    for i in equipment_list:
        if equipment[i]:
            summ += equipment[i]
            if summ <= capacity:
                result[i] = equipment[i]
    return result


backpack_capacity = 15
equipment = {"спальный мешок": 1, "палатка": 3, "плитка": 1.5, "сапоги": 0.5, "тушенка": 3,
             "крупа": 2, "макароны": 2, "топор": 1, "вода": 4, "теплая одежда": 3, "одеяло": 2, "канат": 1.5}


print(f"Вернем один вариант укладки рюкзака: {equip_layout(backpack_capacity, equipment)}")
all_variants = get_all_variants(equipment)
print("Вернем все возможные варианты укладки рюкзака:")
for var in all_variants:
    variant = list(var)
    print(equip_variant(variant, equipment, backpack_capacity))
