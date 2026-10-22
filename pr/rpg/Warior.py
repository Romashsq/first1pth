from Class_Hero import Hero

class Warior(Hero):
    def __init__(self, name,):
        super().__init__(
            name=name,
            hero_type='Warrior',
            health=120, 
            damage=[3,4,5,6,7,8],
            unique_attack="throw_knife"
)



