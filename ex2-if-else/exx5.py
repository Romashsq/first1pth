# Рівень 6. Підсумковий проєкт + додатковий рівень

#17 Система керування доступом до навчальної платформи
VIEW_COURSES = 1
SUBMIT_HOMEWORK = 2
VIEW_CERTIFICATES = 4
MANAGE_USERS = 8

tests = [
    (20, True, True, False, False, False, "courses"),
    (20, True, True, False, True, False, "certificates"),
    (30, True, True, False, False, True, "users"),
    (20, False, True, False, False, False, "courses"),
    (20, True, True, True, False, False, "courses"),
    (20, True, False, False, False, False, "courses"),
    (14, True, True, False, False, False, "courses"),
    (20, True, True, False, False, False, "users"),
    (20, True, True, False, False, False, "dance"),
    (20, True, True, False, False, False, "homework"),
    (20, True, True, False, False, False, "help"),
    (20, True, True, False, False, False, "exit"),
]

for age, is_authenticated, is_active, is_blocked, is_premium, is_admin, command in tests:
    print("---", command)

    if not is_authenticated:
        print("Доступ заборонено: not authenticated")
        continue
    elif not is_active:
        print("Доступ заборонено: not active")
        continue
    elif is_blocked:
        print("Доступ заборонено: blocked")
        continue
    elif age < 16:
        print("Доступ заборонено: younger than 16")
        continue
    print("Доступ дозволено")

    if is_admin:
        role = "admin"
        mask = VIEW_COURSES | SUBMIT_HOMEWORK | VIEW_CERTIFICATES | MANAGE_USERS
    elif is_premium:
        role = "premium"
        mask = VIEW_COURSES | SUBMIT_HOMEWORK | VIEW_CERTIFICATES
    else:
        role = "user"
        mask = VIEW_COURSES | SUBMIT_HOMEWORK
    print("Role:", role)

    match command:
        case "courses":
            print("Команда виконана успішно" if mask & VIEW_COURSES else "Недостатньо прав")
        case "homework":
            print("Команда виконана успішно" if mask & SUBMIT_HOMEWORK else "Недостатньо прав")
        case "certificates":
            print("Команда виконана успішно" if mask & VIEW_CERTIFICATES else "Недостатньо прав")
        case "users":
            print("Команда виконана успішно" if mask & MANAGE_USERS else "Недостатньо прав")
        case "help":
            print("courses, homework, certificates, users, help, exit")
        case "exit":
            print("Bye")
        case _:
            print("Невідома команда")
'1 user courses - success'
'2 premium certificates - success'
'3 admin users - success'
'4 5 6 7 - denied bc not authenticated, blocked, not active, 14 < 16'
'8 user users - not enough rights bc user has no MANAGE_USERS'
'9 unknown command'
'10 user homework - success'




#18 Аналіз помилок
age = 20
if age == 18:
    print("Adult")
'= is for giving value, for compare need =='

score = 95
if score >= 90:
    print("A")
elif score >= 60:
    print("D")
'95 >= 60 was True first so it was D, need bigger first'

number = 10
if number >= 0 and number <= 100:
    print("У діапазоні")
'after and need full condition, Python does not know what <= 100 compares'

is_admin = True
is_blocked = False
if is_admin and not is_blocked:
    print("Доступ дозволено")
'with or blocked admin also gets access, need and'

command = "start"
match command:
    case "start":
        print("Запуск")
    case _:
        print("Невідома команда")
'start without quotes is variable and catches everything, need "start"'

permissions = 3
if permissions & 2:
    print("Є дозвіл WRITE")
'permissions and 2 is always 2 if permissions not 0, it does not check bit, & 2 checks bit 0010'



#19 Самостійне проєктування алгоритму
KITCHEN = 1
BEDROOM = 2
GARAGE = 4

rooms = KITCHEN | BEDROOM
is_home = True
is_alarm = False

commands = [("open", KITCHEN), ("open", GARAGE), ("give", GARAGE), ("open", GARAGE),
            ("take", BEDROOM), ("open", BEDROOM), ("lock",), ("fly",)]

for command in commands:
    match command:
        case ("open", room):
            if is_alarm and not is_home:
                print("Alarm is on")
            elif rooms & room:
                print("Door opened")
            else:
                print("No access")
        case ("give", room):
            rooms = rooms | room
            print("Access given", bin(rooms))
        case ("take", room):
            rooms = rooms & ~room
            print("Access taken", bin(rooms))
        case ("lock",):
            print("All doors locked")
        case _:
            print("Unknown command")
print("Mode:", "home" if is_home else "away")
'kitchen opened, garage no access, then give garage and it opens, take bedroom and no access'
