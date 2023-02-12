# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению.

import random

my_list = [random.randint(0, 100) for _ in range(15)]
print(my_list)
number = int(input('Введите искомое число: '))

if my_list.count(number) == 0:
    nearest = my_list[0]
    for num in my_list:
        if abs(number - num) < abs(number - nearest):
            nearest = num
    print(f'Ближайшее число к {number} - это {nearest}')
else:
    print(f'Число {number} встречается {my_list.count(number)} раз')


