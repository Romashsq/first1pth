


post1_liked = set()
post1_liked.add(1)

user1 = {
    "id": 2,
    "name": 'Roman'

}

user1[0] = 'Lol'
print(user1)
# def like_post(user):
#     while True:
#         click = input('Press the button - CLICK: ').strip().lower()
#         if user['id'] in post1_liked:
#             print('Bye')
#             break
#         if click == 'click':
#             post1_liked.add(user["id"])
#         print(f'You liked post1 {post1_liked} and your id is {user["id"]}')
#         break
        

# like_post(user1)





point = (55.9, 12.5) 

lat, lon = point
print(lat)
# lat[0] = 1
print(lat)
# bc tuple is not available for assignment


def min_max(nums):
    a = min(nums)
    b = max(nums)
    print(a,b)
    return a,b
result = min_max([1,2,3,4,5,5555,3,12,111231231])
print(type(result))
# наверное потому что мы возвращаем сразу два значения поэтому вернула кортеж

sales = {}
sales[("monday", "Helsingør")] = 4500
sales[("monday", "Niva")] = 2100
sales[("tuesday", "Niva")] = 2500
# sales[['thursday', 'Helsingor']] = 2500 unhashable type
print(sales)


for key, value in sales.items():
    print(f'{key} | {value}')

words = "the cat and the dog and the bird".split()
counts = {}

def count(sent):
    for d in words:
        counts[d] = counts.get(d, 0) + 1    
    return counts
print(count(counts))



seats = [("Roman", 1), ("Katya", 2), ("Vova", 1), ("Masha", 2), ("Dima", 3)]

tables = {}

def seat_guests(table):
    for name, seat in table:
        tables.setdefault(seat, []).append(name)
    return tables
print(seat_guests(seats))
nammme = hash('ROman')

print(nammme % 8)


a = {1,2,4,3,24,6,7,"Lomario"}

b = {1,2,3,4,543232,4,5,6, "Romario"}

print(b.intersection(a))


customers = {
    'Roman': 1
}
while True:
    enter_name = input('enter name: ').strip()
    if enter_name == 'stop':
        break
    if enter_name in customers:
        customers[enter_name] += 1
    else: 
        customers.setdefault(enter_name, + 1)
    print(customers)



a,b = 1,2 
print(a,b)