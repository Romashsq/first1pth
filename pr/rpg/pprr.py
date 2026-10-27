# text = "  Hello Python  "
# text_updated = text.upper().strip()
# print(text_updated)




# email = "Roman.Bondarenko@Gmail.com"
# email_update = email.split("@")
# print(email_update[0].lower())

# word = 'programming'
# counter = 0
# for w in word:
#     if w == 'm':
#         counter += 1
# print(counter)


# date = '08.12.2026'
# new_date = date.split('.')
# print(new_date[-1])


# words = ["Python", "is", "cool"]
# print(' '.join(words) + '!')


# c = 'Denmark'
# new_C = c.encode('ascii')
# print(list(new_C))

# cc = "Київ"

# cc2 = cc.encode('utf-8')
# print(list(cc2))
# print(len(cc2))

# data = b"Hello"

# data_new_2 = bytearray(data)
# data_new_2[0] = 98
# print(data_new_2)
# new_d = data.decode('utf-8')
# print(list(data))
# print(new_d)






# point = (10, 20)
# x,y = point
# print(x)
# print(y)
# print(x + y)


# # point2 = (10, 20)
# # point2[0] = 5
# # 'tuple' object does not support item assignment

# from collections import namedtuple

# Dish = namedtuple('DISH', ['name', 'price', 'ingredients'])

# new_dish = Dish('pizza', 10, ['mozzarella', 'parma', 'cheder', 'tom'])


# lol = {1, 2, 3, 4}
# print(lol)





# staff = [
#     {"name": "Roman", "role": "waiter", "hours": 32},
#     {"name": "Katya", "role": "chef", "hours": 40},
#     {"name": "Vova", "role": "waiter", "hours": 18},
#     {"name": "Masha", "role": "chef", "hours": 25},
# ]

# # input_cat = input('Enter category').strip()

# # if input_cat == 'waiter':
# #     for employee in staff['role']:
# #         print(employee)



# def print_by_category():

#     input_cat = input('Enter category').strip()
#     for employee in staff:
#         if employee['role'] == input_cat:
#             print(
#                 f'Name: {employee['name']}/n'
#                 f'Role: {employee['role']}/n'
#                 f'Hours: {employee['hours']}/n'
#             )

# print_by_category()


# name = input('Enter name').strip()
# new_name = hash(name)
# print(new_name)

# print(name.capitalize())
# print(name.startswith('R'))
# print(name.endswith('N'))
# print(name.count('n'))


# message = input('Enter message!').strip()
# if message == '':
#     print('Empty')
# elif 'spam' in message:
#     print('Spam')
# print(message)



nums = [0,1,2,3,4,5,6,7,89,90]

print(8 in nums)

# nums.append('Roman')
# nums.insert(2, 'Lol')
# print(nums)

# get_type = input('Enter which one you would like to get Четные/Нечетные').strip().lower()
# enter_range_nums = int(input('Enter which range you want!').strip())
# def get_num(type):
#     if type == 'четные':
#         num_loops = [i for i in range(enter_range_nums) if i % 2 == 0]
#         print(f'Numbers -{num_loops}')
#         print(f'Sum - {sum(num_loops)}')
#         reverse = num_loops.reverse()
#         print(reverse)
#     if type == 'нечетные':
#         num_loops = [i for i in range(enter_range_nums) if i % 3 == 0]
#         print(f'Numbers -{num_loops}')
#         print(f'Sum - {sum(num_loops)}')
#         reverse = num_loops.reverse()
#         print(reverse)

# get_num(get_type)


user = {
    'name': 'Roman',
    'age': 19,
    'married': False,
    'skills': ['Python', 'n8n', 'Claude AI', 'Frontend']
}

print(user['name'])
print(user.get('surname', 'romashsq'))


OPTIONS = [
    '1. Change something',
    '2. Add something',
    '3. Delete something'
]

# Добавили словарь, чтобы код работал
user = {'name': 'Alex', 'age': 25, 'married': False}

def menu():
    while True:
        for o in OPTIONS:
            print(o)
        option = input('Select option: ').strip()
        match option:
            case '1':
                change = input('Enter what you want to change!: ').strip()
                if change in user.keys():
                    match change: 
                        case 'name':
                            new_name = input('Enter new name: ').strip()
                            user['name'] = new_name
                            print(f'Successfully changed name to {user["name"]}')
                        case 'age':
                            new_age = int(input('Enter new age: ').strip())
                            user['age'] = new_age
                            print(f'Successfully changed age to {user["age"]}')
                        case 'married':
                            is_married = input('Enter if you are married! YES/NO: ').strip()
                            if is_married != 'YES' and is_married != 'NO':
                                raise ValueError('IDK!')
                            if is_married == 'YES':
                                user['married'] = True
                            else:
                                user['married'] = False
                            print(f'Successfully changed married status to {user["married"]}')
                else:
                    print(f"Key '{change}' not found in user profile!")
                
                break 

menu()





student = {'Name', 'Age', 'Language'}
name, age, language = student
print(name)

