# # Последовательность чисел
# # Выведите все числа от 1 до 100 включительно.

# for i in range(1, 101):
#     print(i)

# # Дополнительно:

# # выведите только числа, кратные 7;

# for i in range(1, 101):
#     if i % 7 == 0:
#         print(i)

# # выведите числа от 100 до 1 в обратном порядке;

# for i in range(1, 101, -1):
#     print(i)

# сосчитайте, сколько чисел в диапазоне от 1 до 100 делятся на 3 без остатка.
counter = 0
for i in range(1, 101):
    if i % 3 == 0:
        counter += 1
print(counter)


# Сумма и среднее арифметическое


# Спросите у пользователя натуральное число n. Вычислите сумму всех чисел от 1 до n и их среднее арифметическое.

# n = int(input('Enter your number: '))
# select_opt = [
#     '1. Count % 2',
#     '2. Count % 3'
# ]

# def count(num):
#     total = 0
#     amount = 0
#     for opt in select_opt:
#         print(opt)
#     select = int(input('Enter option: '))
#     match select:
#         case 1:
#             for i in range(1, num + 1):
#                 if i % 2 == 0:
#                     total += i
#                     amount += 1
#             print(total, total / amount)
#         case 2:
#             for i in range(1, num + 1):
#                 if i % 3 == 0:
#                     total += i
#                     amount += 1
#             print(total, total / amount)
#         case _:
#             print('Unknown command')
# count(n)

# average = total / n
# print("Сумма:", total)
# print("Среднее:", average)
# Например, для n=5 сумма равна 15, а среднее – 3.

# Дополнительно: вычислите сумму только четных чисел в этом диапазоне.


# Таблица умножения

# Выведите таблицу умножения для числа, введенного пользователем, от 1 до 10.

num = int(input('Enter your number: ').strip())
for n in range(1,11):
    result = num * n
    print(f'{num} * {n} = {num * n}')

for n in range(1, 11):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()


# 4. Подсчет цифр

# Пользователь вводит целое неотрицательное число. Посчитайте количество его цифр без преобразования числа в строку.

# Дополнительно: вычислите сумму цифр.

# Совет: используйте // 10и % 10. Отдельно обработайте число 0.

num = int(input("Число: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print(count)


# 5. Поиск делителей

# Спросите целое положительное число и выведите все его натуральные делители.

num = int(input('Enter your number: ').strip())
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        count += 1

# Дополнительно: сосчитайте количество делителей

print(f'Количество делителей: {count}')

# Дополнительно: определите, является ли число простым (for ... else)

if num == 1:
    print('1 не является простым числом')
else:
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} не простое, делится на {i}')
            break
    else:
        print(f'{num} простое')


# 6. Система проверки пароля

# Пользователь имеет максимум три попытки ввести правильный пароль. Используйте while и else.

password = 'python123'
attempts = 0
while attempts < 3:
    user_password = input('Enter password: ').strip()
    if user_password == password:
        print('Access granted')
        break
    attempts += 1
    print(f'Wrong password. Attempts left: {3 - attempts}')
else:
    print('Access denied')


# 7. Меню программы

# Меню работает, пока пользователь не выберет 0. После каждой команды меню показывается снова.

menu = [
    '1 - Вывести приветствие',
    '2 - Показать числа от 1 до 10',
    '3 - Вычислить сумму от 1 до N',
    '0 - Выход'
]

while True:
    for opt in menu:
        print(opt)
    select = input('Choose option: ').strip()
    match select:
        case '1':
            print('Привет!')
        case '2':
            for i in range(1, 11):
                print(i, end=' ')
            print()
        case '3':
            n = int(input('Enter N: ').strip())
            total = 0
            for i in range(1, n + 1):
                total += i
            print(f'сумма от 1 до {n}: {total}')
        case '0':
            print('Пока!')
            break
        case _:
            print('Unknown command')


# 8. Геометрические фигуры

# Прямоугольник h * w

h = int(input('Enter height: ').strip())
w = int(input('Enter width: ').strip())
for i in range(h):
    print('*' * w)
print()

# А. Прямоугольный треугольник

for i in range(1, h + 1):
    print('*' * i)
print()

# Б. Перевернутый треугольник

for i in range(h, 0, -1):
    print('*' * i)
print()

# В. Квадрат с полостью внутри

for i in range(h):
    if i == 0 or i == h - 1:
        print('*' * w)
    else:
        print('*' + ' ' * (w - 2) + '*')