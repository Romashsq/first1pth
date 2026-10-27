from random import randint


def get_both(nums):
    return list(filter(lambda x: x % 2 == 0, nums)), list(filter(lambda x: x % 2 != 0, nums))


nums = [randint(0, 100) for i in range(10)]
evens, odds = get_both(nums)
print("Все:", nums)
print("Чётные:", evens)
print("Нечётные:", odds)