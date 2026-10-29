from collections import defaultdict, Counter, ChainMap, OrderedDict


# Блок 1. Теоретический блиц

# 1. Почему кортеж (1, 2, [3, 4]) не может быть элементом set или ключом dict?
# Элементы set и ключи dict должны быть хешируемыми: Python раскладывает их
# по ячейкам хеш-таблицы по хешу. Хеш кортежа считается из хешей всех его
# элементов. Сам кортеж неизменяемый, но внутри лежит список, а список
# изменяемый и хеша не имеет. Поэтому хеш всего кортежа посчитать нельзя:
# TypeError: unhashable type: 'list'.

# 2. Что такое коллизия? Что делает Python при коллизии?
# Коллизия - когда два разных ключа получают один и тот же номер ячейки
# (hash(ключ) % количество ячеек совпал). Python использует открытую адресацию:
# если ячейка занята другим ключом, он по специальной формуле проверяет
# следующие ячейки, пока не найдёт свободную, и кладёт ключ туда.
# При поиске он идёт по той же цепочке ячеек и сравнивает хеш и сам ключ,
# пока не найдёт нужный ключ или пустую ячейку.


# 1
day1_users = ["alice", "bob", "charlie", "david", "alice", "eva"]
day2_users = ["bob", "frank", "eva", "george", "charlie", "charlie"]

set1 = set(day1_users)
set2 = set(day2_users)

print("Все уникальные:", set1 | set2)
print("Оба дня:", set1 & set2)
print("Только первый день:", set1 - set2)


# 2
orders = [
    ["хліб", "молоко"],
    ["молоко", "хліб"],
    ["сік", "хліб"],
    ["хліб", "молоко"]
]

unique_orders = set()
for order in orders:
    unique_orders.add(frozenset(order))
print("Уникальных наборов:", len(unique_orders))


# 3
orders_data = [
    ("Електроніка", "Ноутбук"),
    ("Їжа", "Яблуко"),
    ("Електроніка", "Смартфон"),
    ("Їжа", "Хліб"),
    ("Одяг", "Сорочка"),
    ("Їжа", "Молоко")
]

groups = defaultdict(list)
for category, item in orders_data:
    groups[category].append(item)
print(dict(groups))


# 4
text = "python python java python c++ java python c++ javascript"

languages = Counter(text.split())
print(languages)
print("Топ-2:", languages.most_common(2))


# 5
default_config = {"theme": "light", "language": "uk", "font_size": 12}
user_config = {"theme": "dark", "font_size": 16}

config = ChainMap(user_config, default_config)
print("theme:", config["theme"])
print("font_size:", config["font_size"])
print("language:", config["language"])


# 6
data = OrderedDict([("a", 1), ("b", 2), ("c", 3), ("d", 4)])

data.move_to_end("a")
first = data.popitem(last=False)
print("Удалён первый:", first)
print("Оставшиеся ключи:", list(data.keys()))




