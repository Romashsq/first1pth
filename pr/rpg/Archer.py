from Class_Hero import Hero

class Archer(Hero):
    def __init__(self, name,):
        super().__init__(
            name=name,
            hero_type='Archer',
            health=100, 
            damage=[1,3,6,10],
            unique_attack="fire_ball"
        )