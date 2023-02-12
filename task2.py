eng = 'qwertyuiopasdfghjklzxcvbnm'
rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'

eng_dict = {1 : 'AEIOULNSTR',
            2 : 'DG',
            3 : 'BCMP',
            4 : 'FHVWY',
            5 : 'K',
            6 : 'JX',
            7 : 'QZ'}

word = input('Введите слово (русское или английское): ')

if word[0].lower()in eng:
    summa = 0
    for letter in word:
        for key, value in eng_dict.items():
            if letter.upper() in value:
                summa += key
    print(f'Сумма букв в слове {word} - {summa}')
else:
    print('Русское слово, оно еще в разработке')