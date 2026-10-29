# 1
def calculate_total(price, quantity):
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        raise TypeError('Цена должна быть числом')
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise TypeError('Колличество должно быть целым числом!')
    if price <= 0 and quantity <= 0:
        raise ValueError('Прайс и колличество должны быть больше либо равно 0')
    return price * quantity

# print(calculate_total(2, 2.5)) 
# print(calculate_total(0, 2))

# 2
enter_price = float(input('Enter your price').strip())
enter_discount = int(input('Enter your discount').strip())
def apply_discount(total, discount_percent=0):
    if isinstance(total, bool) or not isinstance(total, (int,float)):
        raise ValueError('total price expects to get more than 0')
    if total <= 0:
        raise ValueError('Total price must be more than 0')
    if isinstance(discount_percent, bool) or not isinstance(discount_percent, int):
        raise ValueError('total price expects to get more than 0 or whole number')
    if discount_percent < 0 or discount_percent > 100:
        return 'Discount can be 0 or 100'
    result = (total * discount_percent) / 100
    result2 = total - result
    return f'Discount -{result} and Price with discount {result2}'

print(apply_discount(enter_price, enter_discount))


# 3


enter_numbers = int(input(f'Enter numbers: ').strip())
nums_list = []
def calculate_statistics(numbers):


    for num in range(numbers):
        nums_list.append(num)

    if not numbers:
        return None, None, None  
        
    min_num = min(nums_list)
    max_num = max(nums_list)
    average = sum(nums_list) / len(nums_list)
    
    return min_num, max_num, average
print(calculate_statistics(enter_numbers))


# 4

def calculate_average(*numbers):
    if not numbers:
        return 'Empty'
    for num in numbers:
        if isinstance(num, bool) or not isinstance(num, int):
            raise ValueError('Not number')
    return sum(numbers)

print(calculate_average(10,10,1,100) )

# 5 
enter_name = input('Enter name ').strip()
user_data = {}
def user(name, **params):

    if not name:
        return 'There is no name here!'
    user_data['name'] = name

    if not params:
        return f'There is only name {user_data["name"]}'
    
    if 'age' in params:
        age_val = params["age"]
        if isinstance(age_val, bool) or not isinstance(age_val, int):
            return f'Age has to be int'
        if age_val < 0 or age_val > 100:
            return 'Age must be between 0 and 100'
        
    for key, value in params.items():
        user_data[key] = value
    

    return user_data
    
print(user(enter_name, age=10, city='Odessa',is_married=False)   )


# 6

# 1
def change(value):
    value = 100
# def change(value): example that if we add value_1 with value = 110
#     value_1 = 100
#     result = value_1 + value
#     return result
# Выведет 10, так как value = 100(Просто переменная внутри функции), а value in change(value) выступает в роли параметра куда мы должны передать наше значение  
number = 10
change(number)
print(number)

# 2
def change(items):
    items.append(100)


numbers = [10, 20]
change(numbers)
print(numbers)
# Выведет [10, 20, 100], так как items in change(items) выступает в роли параметра, куда передается ссылка на наш список numbers. 
# Команда .append(100) меняет сам исходный объект в памяти (мутирует его). 
# Поскольку items и numbers смотрят на один и тот же список, изменения видны снаружи функции.


# 3
def change(items):
    items = [100, 200]

numbers = [10, 20]
change(numbers)
print(numbers)
# Выведет [10, 20], так как items in change(items) принимает ссылку на numbers, но строчка items = [100, 200] это перепривязка локального имени. 
# мы заставили локальную переменную items смотреть на совершенно новый список
# исходный список numbers снаружи остался нетронутым.

# 7
def add_product(name, products=None):
    if products is None:
        products = []  # Создаем новый список при каждом "пустом" вызове
    products.append(name)
    return products
