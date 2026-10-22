from Class_Hero import Hero
from Archer import Archer
from Magic import Magic
from Warior import Warior
from register_menu import register

OPTIONS_UNREGISTERED = [
    'CREATE ACCOUNT',
    'I HAVE AN ACCOUNT',
    'EXIT',
]

HEROES = [
    {
        "id":1,
        "class": Archer
    },
    {
        "id":2,
        "class": Magic
    },
    {
        "id":3,
        "class": Warior
    }
]

OPTIONS_REGISTERED = [
    'сражаться с монстром;',
    'посмотреть характеристики персонажа;',
    'открыть инвентарь;',
    'использовать предмет;',
    'выйти из игры.',
]

my_account = {}

def menu():
    for i, option in enumerate(OPTIONS_UNREGISTERED, start=1):
        print(f'{i}. {option}')
    select_option = int(input('Select option'))
    match select_option:
        case 1:
            register(my_account, HEROES)
            
menu()
