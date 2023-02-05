class Army():
    units: list
    def __init__(self):
        self.units=[]
    def add_units(self, *units):
        for i in units:
            self.units.append(i)

class Battle():

    def war(self, first_army, second_army):
        first_army_pointer=0
        second_army_pointer=0

        while first_army_pointer!=len(first_army.units) and second_army_pointer!=len(second_army.units):
            if fight(first_army.units[first_army_pointer],
                  second_army.units[second_army_pointer]):
                second_army_pointer+=1
            else:
                first_army_pointer+=1
        if second_army_pointer == len(first_army.units):
            return True
        else:
            return False
def fight(first, second, first_extra=None, second_extra=None):
    while first.is_alive and second.is_alive:
        second.get_damage(first.attack)
        if isinstance(first, Vampire):
            extra_health = first.attack/(first.vampirism//100)
            if isinstance(second, Defender):
                extra_health -= (second.shields * first.vampirism)/100
            if first.health > first.max_health:
                first.health = first.max_health
            elif isinstance(first, Lancer) and second_extra is not None:
                second_extra.get_damage(first.attack // 2)
            if isinstance(second, Vampire):
                extra_health = second.attack/(second.vampirism//100)
                if isinstance(first, Defender):
                    extra_health -= (first.shields * second.vampirism)/100
                if second.health > second.max_health:
                    second.health = second.max_health
            elif isinstance(second, Lancer) and first_extra is not None:
                first_extra.get_damage(second.attack // 2)
            if second.is_alive:
                first.get_damage(second.attack)
        return first.is_alive and not second.is_alive

class Warrior:
    health: int
    attack: int
    shields: int
    is_alive: bool
    def __init__(self):
        self.health=50
        self.attack=5
        self.is_alive=True
        self.shields=0
    def get_damage(self, damage):
        self.health -= damage
        if self.health < 1:
            self.is_alive=False
class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack+=2

class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health+=10
        self.attack-=2
        self.shields+=2
    def get_damage(self, damage):
        self.health -= (damage > self.shields)*(damage - self.shields)
        if self.health < 1:
            self.is_alive=False

class Vampire(Warrior):
    vampirism: int
    def __init__(self):
        super().__init__()
        self.health = 40
        self.max_health = 40
        self.attack = 4
        self.vampirism=50

class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6

if __name__=="__main__":
    army3 = Army()
    army3.add_units(Warrior(), Lancer(), Defender())
    army4 = Army()
    army4.add_units(Vampire(), Warrior(), Lancer())
    battle=Battle()
    print(battle.war(army3, army4))