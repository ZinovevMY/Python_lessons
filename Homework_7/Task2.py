# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random


def pseudonyms(filename: str):
    name_length = random.randint(4, 7)
    pseudonym = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                  'z']
    with open(filename, 'a', encoding='utf-8') as file:
        for _ in range(name_length):
            if len(pseudonym) == 0 or pseudonym[-1] in consonants:
                pseudonym += random.choice(vowels)
            else:
                pseudonym += random.choice(consonants)
            pseudonym = pseudonym.capitalize()
        file.write(pseudonym + "\n")


pseudonyms('task2_text.txt')
