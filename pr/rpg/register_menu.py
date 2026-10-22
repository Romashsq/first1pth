from Class_Hero import Hero
from Archer import Archer
from Magic import Magic
from Warior import Warior
HEROES = [
    {
        "id":1,
        "name": "Archer",
        "class": Archer
    },
    {
        "id":2,
        "name": "Magic",
        "class": Magic
    },
    {
        "id":3,
        "name": "Warior",
        "class": Warior
    }
]
def register(account, heroes):
    while True:
        name = input('Enter your name: ').strip()
        account["name"] = name

        for hero in heroes:
            print(f"{hero['id']}. {hero['class']}")
        hero = int(input('Select your hero: ').strip())
        match hero:
            case 1:
                account["hero"] = hero[0]
                print(f'You selected {account["hero"]}')
            case 2:
                account["hero"] = hero[1]
                print(f'You selected {account["hero"]}')
            case 3:
                account["hero"] = hero[2]
                print(f'You selected {account["hero"]}')
