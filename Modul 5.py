'''class StringVar:
    def __init__(self, x = str(input('Введите строку: '))):
        self.x = x

    def set_srt(self, x):
        self.x = x
        return x

    def get_str(self):
        return print(self.x)

st = StringVar()

st.get_str()

st.set_srt(input('Измените строку: '))

st.get_str()


class Point:
    color = 'red'
    size = 2
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return print(self.x, self.y)

    def set_coord(self, x, y):
        self.x = x
        self.y = y
        return x, y

pt = Point(2, 3)

pt.get_coord()

pt.set_coord(5, 7)

pt.get_coord()'''


class Warrior:
    health = 100
    # armor =

    def attack(self):
        pass

    def deffence(self):
        pass

from random import randint

w1 = Warrior
w2 = Warrior

while w1.health > 10 or w2.health > 10:
    x = randint(0, 1)
    print(x)
    if x == 0:
        w1.health -= randint(1, 10)
        print(f'Здоровье война 1: {w1.health},\nЗдоровье война 2: {w2.health}')
    else:
        w2.health -= randint(1, 10)
        print(f'Здоровье война 2: {w2.health},\nЗдоровье война 1: {w1.health}')

if w1.health < 10:
    print('Воин 2 победил')
else:
    print('Воин 1 победил')
