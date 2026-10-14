# Рівень 4. Умовні конструкції

#9 Повне та неповне розгалуження
temperatures = [-10, -1, 0, 5, 25]

for t in temperatures:
    if t < 0:
        print(t, "Frost")
'only -10 and -1'

for t in temperatures:
    if t < 0:
        print(t, "Frost")
    else:
        print(t, "Not below zero")
'-10 and -1 frost, other not below zero'

'Поясніть різницю між повним і неповним розгалуженням'
# incomplete is only if, complete is if and else so something always prints

#10 Множинний вибір — система оцінювання
scores = [0, 59, 60, 69, 70, 79, 80, 89, 90, 100, -5, 101]

for score in scores:
    if score < 0 or score > 100:
        print(score, "Incorrect value")
    elif score >= 90:
        print(score, "A")
    elif score >= 80:
        print(score, "B")
    elif score >= 70:
        print(score, "C")
    elif score >= 60:
        print(score, "D")
    else:
        print(score, "F")

'Чому порядок умов важливий?'
# bc Python stops at first True, if >= 60 was first then 95 would be D

#11 Тернарний оператор
age = 20
result = "adult" if age >= 18 else "not adult"
if age >= 18:
    result = "adult"
else:
    result = "not adult"
print(result)

number = 7
result = "even" if number % 2 == 0 else "odd"
if number % 2 == 0:
    result = "even"
else:
    result = "odd"
print(result)

order_sum = 2500
result = "free delivery" if order_sum >= 2000 else "paid delivery"
if order_sum >= 2000:
    result = "free delivery"
else:
    result = "paid delivery"
print(result)

is_online = True
result = "online" if is_online else "offline"
if is_online:
    result = "online"
else:
    result = "offline"
print(result)

has_access = False
result = "Доступ дозволено" if has_access else "Доступ заборонено"
if has_access:
    result = "Доступ дозволено"
else:
    result = "Доступ заборонено"
print(result)

'Порівняйте читабельність обох варіантів'
# ternary is shorter for simple things, if/else is better when there is more code
'Чому не варто замінювати довгу if/elif/else вкладеними тернарними?'
# bc a if x else b if y else c is very hard to read

#12 Множинний вибір через match/case
command = "save"

match command:
    case "new":
        print("Create file")
    case "open":
        print("Open file")
    case "save":
        print("Save file")
    case "close":
        print("Close file")
    case "quit" | "exit":
        print("Exit")
    case _:
        print("Unknown command")

if command == "new":
    print("Create file")
elif command == "open":
    print("Open file")
elif command == "save":
    print("Save file")
elif command == "close":
    print("Close file")
elif command == "quit" or command == "exit":
    print("Exit")
else:
    print("Unknown command")

'Порівняйте обидва варіанти за читабельністю'
# match is cleaner bc no need to write command == every time

commands = [("move", 100, 200), ("stop",), ("resize", 800, 600), ("jump", 1)]
for command in commands:
    match command:
        case ("move", x, y):
            print("Move to", x, y)
        case ("stop",):
            print("Stop")
        case ("resize", width, height):
            print("Resize to", width, height)
        case _:
            print("Unknown command")

#13 Вибір правильної конструкції
'Показати попередження, якщо заряд батареї нижчий за 15%'
# if bc we need only warning
'Визначити, чи число додатне або недодатне'
# if/else bc only 2 options, ternary also ok
'Визначити категорію оцінки за п\'ятьма діапазонами'
# if/elif/else bc there are ranges
'Вибрати напис У мережі або Не в мережі'
# ternary bc it is simple choice from 2
'Обробити команди start, stop, pause, resume'
# match/case bc one variable and fixed values, if/elif also possible
'Розібрати кортеж ("click", 100, 200)'
# match/case bc it can take x and y from tuple
'Надати доступ, якщо користувач авторизований, активний і не заблокований'
# if/else with and, not
