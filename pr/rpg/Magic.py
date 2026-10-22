from Class_Hero import Hero

class Magic(Hero):
    def __init__(self, name,):
        super().__init__(
            name=name,
            hero_type='Warrior',
            health=80, 
            damage=[2,4,8,12],
            unique_attack="fire_ball"
        )