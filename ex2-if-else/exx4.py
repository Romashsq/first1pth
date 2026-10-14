# Рівень 5. Комплексні алгоритми

#14 Калькулятор
a = 20
b = 5
operation = "/"

if operation in ("/", "//", "%") and b == 0:
    print("Division by zero")
elif operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
elif operation == "//":
    print(a // b)
elif operation == "%":
    print(a % b)
elif operation == "**":
    print(a ** b)
else:
    print("Unknown operation")
'4.0'

tests = [(20, 5, "+"), (20, 5, "-"), (20, 5, "*"), (20, 5, "/"), (20, 5, "//"), (20, 5, "%"),
         (20, 5, "**"), (20, 0, "/"), (20, 0, "//"), (20, 0, "%"), (20, 5, "?")]
for a, b, operation in tests:
    match operation:
        case "/" | "//" | "%" if b == 0:
            print("Division by zero")
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            print(a / b)
        case "//":
            print(a // b)
        case "%":
            print(a % b)
        case "**":
            print(a ** b)
        case _:
            print("Unknown operation")
'25, 15, 100, 4.0, 4, 0, 3200000, 3 times zero division, unknown'
# match is shorter, if/elif is more usual

#15 Банкомат
LIMIT = 5000
tests = [
    (10000, 2500, True, False),
    (10000, 2500, False, False),
    (10000, 2500, True, True),
    (10000, 0, True, False),
    (10000, -100, True, False),
    (1000, 2500, True, False),
    (10000, 6000, True, False),
    (10000, 5000, True, False),
]

for balance, amount, is_card_active, is_blocked in tests:
    if not is_card_active:
        print("Card is not active")
    elif is_blocked:
        print("Card is blocked")
    elif amount <= 0:
        print("Amount must be more than 0")
    elif amount > balance:
        print("Not enough money")
    elif amount > LIMIT:
        print("Limit is 5000")
    else:
        balance = balance - amount
        print("Success")
    print("Balance:", balance)
'1 success 7500'
'2 not active bc is_card_active = False'
'3 blocked'
'4 and 5 bc amount <= 0'
'6 not enough bc 2500 > 1000'
'7 limit bc 6000 > 5000'
'8 success bc 5000 is not more than limit'

#16 Світлофор
color = "yellow"

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Unknown signal")

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Unknown signal")
'Wait'
# match looks cleaner, if/elif is better when we need more conditions
