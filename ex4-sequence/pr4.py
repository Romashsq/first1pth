# numbers = [10, 20, 30, 40, 50]
# print(numbers[0])
# print(numbers[-1])
# print(numbers[2])

# name = 'Roman'
# print('r' in name)
# print(len(name))
# print(name[-1])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# print(numbers[0:3:])
# print(numbers[5:8:])
# print(numbers[:-4:-1])

# cart = []
# cart.append('Monitor')
# cart.append('r')
# cart.append('2')
# print(cart)
# cart.remove('2')
# print(cart)
# cart.insert(0,'LOL')
# print(cart)
# print(cart[0])

# menu = ["Pizza", "Pasta", "Salad"]

# for i, dish in enumerate(menu, start=1):
#     print(f'{i}: {dish}')

# gmail = "  Roman@Gmail.COM  "

# def get_wrong_email(email):
#     good_email = email.strip().lower()
#     print(good_email)
# get_wrong_email(gmail)

# stri = "red,green,blue"

# def get_array(data):
#     good_data = data.split(',')
#     print(good_data)
# get_array(stri)

# enter_word = input('Enter').strip()

# def get_count_word(word):
#     words_list = []
#     counter = 0
#     for letter in word:
#         words_list.append(letter)
#         counter += 1
#     print(counter)
#     print(words_list)
# get_count_word(enter_word)

# def check_word(word):
#     if word == word[:: -1]:
#         print('YEEE')
#     else: 
#         print('Fuck up')
# check_word(enter_word)

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a)



# products = [
#     {"name": "Laptop", "price": 5000},
#     {"name": "Mouse", "price": 150},
#     {"name": "Monitor", "price": 2000},
#     {"name": "Cable", "price": 50},
# ]



# def collect_by_price(array):
#     enter_price = int(input('Enter price: '))
#     for product in array:
#         if product["price"] >= enter_price:
#             print(product["name"])
# collect_by_price(products)

class BankAccount:
    def __init__(self,name, bank_id, user_id, amount, cvv, pin):
        self.name = name
        self.bank_id = bank_id
        self.user_id = user_id
        self.amount = amount
        self.__cvv = cvv
        self.__pin = pin

    def count_week():
        for day in range(1, 8):
            enter_tips = int(input('Enter how much you got today!: ').strip())
            tips.append(enter_tips)
            print(tips)
            sum_result = sum(tips)
        print(sum_result)
        return sum_result


tips = []
def count_week():
    for day in range(1, 8):
        enter_tips = int(input('Enter how much you got today!: ').strip())
        tips.append(enter_tips)
        print(tips)
        sum_result = sum(tips)
    print(sum_result)
    return sum_result

MENU = [
    '1. COUNT WEEK',
    '2. GER AVERAGE',
    '3. WITHDRAW SUM'
]
def menu():
    while True:
        print('---- MENU ----')
        for option in MENU:
            print(option)
        select_option = int(input('ENTER OPTION!'))

        match select_option:
            case 1:
                while True:
                    try:
                        print('COUNTING TIPS')
                        count_week()
                        break
                    except ValueError:
                        print('try again')
                        continue

menu()
                    
