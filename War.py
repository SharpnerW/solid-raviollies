#making easier
true=True
false=False
#
class Army():
    units: list
    def __init__(self):
        self.units=[]
    def add_units(self, *units):
        for i in units:
            self.units.append(i)

class Battle():
    def __init__(self, *args):
        self.result=self.fight(*args)
    def fight(self, first, second):
        while first.is_alive and second.is_alive:
            second.get_damage(first.attack)
            if isinstance(first, Vampire): #and not isinstance(second, Vampire)):
                extra_health = first.attack/(first.vampirism//100)
                if isinstance(second, Defender):
                    extra_health -= (second.shields * first.vampirism)/100
                if first.health > first.max_health:
                    first.health = first.max_health
            if isinstance(second, Vampire): #and not isinstance(first, Vampire):
                extra_health = second.attack/(second.vampirism//100)
                if isinstance(first, Defender):
                    extra_health -= (first.shields * second.vampirism)/100
                if second.health > second.max_health:
                    second.health = second.max_health
            if second.is_alive:
                first.get_damage(second.attack)
        return first.is_alive and not second.is_alive
    def war(self, first_army, second_army):
        first_army_pointer=0
        second_army_pointer=0

        while first_army_pointer!=len(first_army.units) and second_army_pointer!=len(second_army.units):
            if self.fight(first_army.units[first_army_pointer],
                  second_army_pointer.units[second_army_pointer]):
                second_army_pointer+=1
            else:
                first_army_pointer+=1
        if second_army_pointer == len(first_army.units):
            return true
        else:
            return false


class Warrior:
    health: int
    attack: int
    shields: int
    is_alive: bool
    def __init__(self):
        self.health=50
        self.attack=5
        self.is_alive=true
        self.shields=0
    def get_damage(self, damage):
        self.health -= damage
        if self.health < 1:
            self.is_alive=false
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
            self.is_alive=false

class Vampire(Warrior):
    vampirism: int
    def __init__(self):
        super().__init__()
        self.health = 40
        self.max_health = 40
        self.attack = 4
        self.vampirism=50



if __name__=="__main__":
    chuck=Knight()
    carl=Defender()
    print(Battle(chuck, carl).result)