#1
print(10 > 5)
'True'
print(10 == 5)
'False'
print(7 != 3)
'True'
print(12 <= 12)
'True'
print(15 < 10)
'False'
print(True and False)
'False'
print(True or False)
'True'
print(not True)
'False'
print(not False)
'True'

print(5 > 3 and 10 < 20)
'True bc both are True'
print(5 > 3 and 10 > 20)
'False bc 10 is less than 20'
print(5 < 3 or 10 < 20)
'True bc 10 less than 20'
print(not (5 > 3))
'False bc 5 > 3 is True'
print(5 > 3 or 10 / 0 > 1)
'True bc 5 > 3 is True and short-circuit saves from zero division'

print(0 or 15)
'15 bc 0 is False'
print(10 and 20)
'20 bc 10 is True'
print("" or "Python")
'Python bc empty string is False'
# print([] and)
'[] bc empty list is False'
#2

# if 1 & 0:
'False bc 1 & 0 is 0'
# if 1 | 0:
'True bc 1 | 0 is 1'
# if ~ 1:
'True bc ~1 is -2 (any non-zero number is True in Python)'
# if ~ 1 & 0:
'False bc anything bitwise AND 0 is 0'
# if (1 | 0) & 1:
'True bc 1 & 1 is 1'
# if ~ (1 & 0):
'True bc ~(0) is -1'
# (1 & 0) | 2:
'2 bc 0 | 2 is 2'

values = [
    0,
    1,
    -1,
    0.0,
    "",
    "0",
    [],
    [0],
    (),
    (0,),
    {},
    {"x": None},
    None,
    False,
    True
]

for value in values:
    print(repr(value), bool(value))
# 0 False
# 1 True
# -1 True
# 0.0 False
# "" False
# "0" True
# [] False
# [0] True
# () False
# (0,) True
# {} False
# {"x": None} True
# None False
# False False
# True True

'Чому 0 і "0" мають різну логічну інтерпретацію'
# bc 0 is num and "0" is filled str
'Чому порожній список є хибним, а список [0] — істинним?'
#bc 0 is num inside of the list
"Чому None часто перевіряють через is None?"
#maybe bc if name is None, если имя не верное то фолз?

'Чи означає bool(value) == True, що значення дорівнює числу 1?'
# I didn't get it

