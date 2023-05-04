#Уровень 1
class StringVar():
    def __init__(self, string: str):
        self.string = string

    def get(self):
        return self.string

    def set(self, new_string: str):
        self.string = new_string

string1 = StringVar('hello')

print(string1.get())
string1.set('no hello')
print(string1.get())

#Уровень 2
import math

class DistCalc:
    #расстояние между двумя точками
    @staticmethod
    def dist_two_dots(point, other):
        return math.sqrt((point.x + other.x) ** 2 + (point.y + other.y) ** 2)
class Point(DistCalc):
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y

    def get(self):
        return (self.x, self.y)

    def set(self,x:int, y:int):
        self.x = x
        self.y = y

    def distance(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

p = Point(1, 1)
print(p.dist_two_dots(point=Point(1, 1), other=Point(3, 4)))

#Уровень 3
## - 3.1
class Warrior:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.damage = 20

    def __is_dead(self, unit):
        if unit.health <= 0:
            return print(f'Winner: {self.name}')

    def attack(self, unit):
        unit.health -= self.damage
        print(f'{self.name} attack {unit.name}')
        print(f'{unit.name} has {unit.health}')
        print('--------')
        self.__is_dead(unit)

unit1 = Warrior('John')
unit2 = Warrior('Sam')

unit1.attack(unit2)
unit2.attack(unit1)
unit1.attack(unit2)
unit2.attack(unit1)
unit1.attack(unit2)
unit1.attack(unit2)
unit1.attack(unit2)
unit1.attack(unit2)

## - 3.2
class Warrior:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.damage = 20
        self.armor = 100
        self.endurance = 100