# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.(Может помочь метод translate из модуля string)

import re


def wordscount_in_string(string: str) -> dict:
    string_dict = {}
    string = string.lower()
    string = re.sub(r'[^\w\s]', '', string)
    string_list = string.split()
    for word in string_list:
        if word in string_dict:
            string_dict[word] += 1
        else:
            string_dict[word] = 1
    return string_dict

my_str = "Сейчас я не могу сказать, что именно, но в его облике меня что-то привлекло. " \
         "Старотипный плащ, фасона 1965 года, на нём не было места, которое было бы не зашито. " \
         "Но этот заштопанный и перештопанный плащ был чистым. " \
         "Брюки, такие же старые, но до безумия наутюженные. " \
         "Ботинки начищены до зеркального блеска, но это не могло скрыть их возраста. " \
         "Один ботинок, был перевязан проволокой. Я так понял, что подошва на нём просто отвалилась. " \
         "Из-под плаща была видна старая, почти ветхая рубашка, но и она была чистой и наутюженной. " \
         "Его лицо было обычным лицом старого человека, вот только, во взгляде было что-то непреклонное и гордое, не смотря ни на что. " \
         "Сегодня был праздник, и я уже понял, что дед не мог быть небритым в такой день. " \
         "На его лице было с десяток порезов, некоторые из них были заклеены кусочками газеты. " \
         "Деда трусило от холода, его руки были синего цвета… Его очень трусило, но он стоял на ветру и ждал. " \
         "Какой-то нехороший комок подкатил к моему горлу. Я начал замерзать, а продавщицы всё не было."

string_dict = wordscount_in_string(my_str)
max_words = max(string_dict.values())
key = list(filter(lambda key: string_dict[key] == max_words, string_dict))
print(f"В введенной строке чаще всего ({max_words} раз) встречается слово {key}.")