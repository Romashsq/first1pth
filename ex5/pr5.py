data_ar = [1,2,3,4,5,6,"romario"]
data_ar2 = [1,7,8,9,10,6,"lolario"]


data = {1,2,3,4,5,6,"romario"}
data2 = {1,7,8,9,10,6,"lolario"}
print(data | data2)

data2 |= {2}
print(data - data2)

data_obj = {
    ('Food', 'Drink'): 25

}



students = {
    "Roman": 1,
    "Roman": 2,
    "Roman": 3,
    "Roman": 4,
    "Roman": 3,
}

new_student = {
    'Lomar': []
}
print(students | new_student)




contacts = {
    "Іван": "0991234567", 
    "Марія": "0679876543", 
    "Петро": "0505551122"

}

contacts['Ольга'] = '0631112233'
print(contacts)
del contacts["Марія"]
print(contacts)
print('Іван' in contacts)
print(contacts["Петро"])
stepan_phone = None
contacts.get(stepan_phone)
