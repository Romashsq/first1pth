FUEL_PRICE = 55.5
CONSUMPTION_PER_100KM = 8.2

distance = float(input("Введите расстояние в км: "))


fuel = distance / 100 * CONSUMPTION_PER_100KM
cost = fuel * FUEL_PRICE
tens = distance // 10
rest = distance % 10

print(f"Топлива нужно: {fuel} л")
print(f"Стоимость поездки: {cost} грн")
print(f"Полных десятков км: {tens}, остаток: {rest} км")