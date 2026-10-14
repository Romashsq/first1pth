age = int(input("Сколько вам лет? "))
answer = input("Вы студент? (yes/no): ")

is_student = answer == "yes"

discount_allowed = age <= 18 or age >= 60 or (is_student and age < 25)
full_price = not discount_allowed

print(f"Скидка доступна {discount_allowed}")
print(f"Полная цена {full_price}")