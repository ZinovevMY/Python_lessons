import mistery_module as mm

mistery = "Висит груша, нельзя скушать."
clue = "ЛАМПОЧКА"
clue_list = ['мяч', 'лампочка', 'арбуз', 'паровоз']
attempts = 3

guessed = mm.mistery(mistery, clue, clue_list, attempts)

if guessed > 0:
    print(f"Отгадано с {guessed} попытки!")
else:
    print("Не отгадали!")