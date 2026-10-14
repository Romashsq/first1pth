# Рівень 2-3. Логічні умови та побітові операції

#4 Система доступу
users = [
    (21, True, False, True),
    (17, True, False, True),
    (30, False, False, True),
    (25, True, True, True),
    (19, True, False, False),
]

for age, is_authenticated, is_blocked, has_permission in users:
    if is_authenticated and not is_blocked and age >= 18 and has_permission:
        print("Access allowed")
    else:
        print("Access denied")
'1 allowed bc all conditions are True'
'2 denied bc 17 < 18'
'3 denied bc not authenticated'
'4 denied bc blocked'
'5 denied bc no permission'

print("--- test ---")
tests = [
    (21, False, False, True, "not authenticated"),
    (21, True, True, True, "blocked"),
    (17, True, False, True, "younger than 18"),
    (21, True, False, False, "no permission"),
]
for age, is_authenticated, is_blocked, has_permission, reason in tests:
    if is_authenticated and not is_blocked and age >= 18 and has_permission:
        print("Access allowed")
    else:
        print("Access denied bc", reason)

#5 Валідація даних користувача
username = "student_01"
email = "student@example.com"
age = 20
password = "Python123"

is_valid = True
if username == "":
    print("Username is empty")
    is_valid = False
if len(username) < 5:
    print("Username is shorter than 5")
    is_valid = False
if "@" not in email:
    print("Email has no @")
    is_valid = False
if age < 16:
    print("Age is less than 16")
    is_valid = False
if len(password) < 8:
    print("Password is shorter than 8")
    is_valid = False
print("Validation 1:", is_valid)

is_valid_2 = username != "" and len(username) >= 5 and "@" in email and age >= 16 and len(password) >= 8
print("Validation 2:", is_valid_2)
'True bc all data is correct'

#6 Робота з двійковими числами
print(5 & 3, bin(5 & 3))
'1 bc 0101 & 0011 = 0001'
print(5 | 3, bin(5 | 3))
'7 bc 0101 | 0011 = 0111'
print(5 ^ 3, bin(5 ^ 3))
'6 bc 0101 ^ 0011 = 0110'
print(5 << 1, bin(5 << 1))
'10 bc 0101 -> 1010'
print(5 >> 1, bin(5 >> 1))
'2 bc 0101 -> 0010'
print(~5, bin(~5))
'-6'
'Чому ~5 у Python дорівнює -6, а не 2?'
# bc Python numbers have no limit of bits, ~ flips all of them and number becomes negative, ~x = -x - 1

#7 Логічні чи побітові оператори?
print(True and False)
'False'
print(True & False)
'False - same'
print(5 and 3)
'3 bc 5 is True so and returns second'
print(5 & 3)
'1 bc 0101 & 0011 = 0001 - not same'
print(0 or 7)
'7 bc 0 is False so or returns second'
print(0 | 7)
'7 - same'
print(4 or 2)
'4 bc 4 is True so or returns first'
print(4 | 2)
'6 bc 100 | 010 = 110 - not same'

'Чи можна замінювати and на &?'
# only for True and False, for numbers no
'Чи завжди or та | повертають однаковий результат?'
# no, 4 or 2 = 4 but 4 | 2 = 6
'Чим відрізняються правила обчислення цих операторів?'
# and/or return one of values and can skip second part, & and | count every bit
'Чому & і | не є універсальною заміною логічних операторів?'
# bc no short-circuit, x != 0 & 10 / x > 1 can make zero division

#8 Система дозволів через бітові маски
READ = 1
WRITE = 2
DELETE = 4
EXECUTE = 8

permissions = READ | WRITE
print("READ", bool(permissions & READ))
print("WRITE", bool(permissions & WRITE))
print("DELETE", bool(permissions & DELETE))
print("EXECUTE", bool(permissions & EXECUTE))
'True True False False bc 0011'

permissions = permissions | EXECUTE
'1011'
permissions = permissions & ~WRITE
'1001'
print("READ", bool(permissions & READ))
print("WRITE", bool(permissions & WRITE))
print("DELETE", bool(permissions & DELETE))
print("EXECUTE", bool(permissions & EXECUTE))
'True False False True bc READ and DELETE did not change'

'Поясніть роботу операторів |, &, ~'
# | turns bit on, & checks if bit is there, ~ makes mask without this bit so & ~ turns it off
