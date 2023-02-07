import random


class Warrior:
    def __init__(self, health, armor, endurance):
        self.health = health
        self.armor = armor
        self.endurance = endurance

    def attack(self):
        if self.endurance > 0:
            self.endurance -= 10

    def defence(self):
        if self.armor > 0:
            self.armor -= random.randint(0, 10)
            self.health -= random.randint(0, 20)
        else:
            self.health -= random.randint(10, 30)


w1 = Warrior(100, 50, 50)
w2 = Warrior(100, 50, 50)
count = 0

random_1 = ['Атака', 'Защита']

while w1.health > 10 and w2.health > 10:
    count += 1
    print(f'Ход {count}')
    x1 = random.choice(random_1)
    x2 = random.choice(random_1)
    if x1 == 'Атака' and x2 == 'Атака':
        print('Воин 1 атакует')
        print('Воин 2 атакует')
        if w1.endurance > 0:
            w1.attack()
            w2.health -= random.randint(10, 30)
            print(f'Здоровье 1: {w1.health}, Выносливость 1: {w1.endurance}'
                  f'\nЗдоровье 2: {w2.health}, Выносливость 2: {w2.endurance}')
        else:
            w1.attack()
            w2.health -= random.randint(0, 10)
            print(
                f'Здоровье 1: {w1.health}, Выносливость 1: {w1.endurance}'
                f'\nЗдоровье 2: {w2.health}, Выносливость 2: {w2.endurance}')
        if w2.endurance > 0:
            w2.attack()
            w1.health -= random.randint(10, 30)
            print(
                f'Здоровье 1: {w1.health}, Выносливость 1: {w1.endurance}'
                f'\nЗдоровье 2: {w2.health}, Выносливость 2: {w2.endurance}')
        else:
            w2.attack()
            w1.health -= random.randint(0, 10)
            print(f'Здоровье 1: {w1.health}, Выносливость 1: {w1.endurance}'
                  f'\nЗдоровье 2: {w2.health}, Выносливость 2: {w2.endurance}')
    elif x1 == 'Атака' and x2 == 'Защита':
        print('Воин 1 атакует')
        print('Воин 2 защищается')
        if w1.endurance > 0 < w2.armor:
            w1.attack()
            w2.defence()
            print(f'Выносливость 1: {w1.endurance}\nЗдоровье 2: {w2.health}, Броня 2: {w2.armor}')
        elif w1.endurance <= 0 < w2.armor:
            w2.armor -= random.randint(0, 5)
            w2.health -= random.randint(0, 5)
            print(f'Выносливость 1: {w1.endurance}\nЗдоровье 2: {w2.health}, Броня 2: {w2.armor}')
        else:
            w2.health -= random.randint(0, 10)
            print(f'Выносливость 1: {w1.endurance}\nЗдоровье 2: {w2.health}, Броня 2: {w2.armor}')
    elif x2 == 'Атака' and x1 == 'Защита':
        print('Воин 1 защищается')
        print('Воин 2 атакует')
        if w2.endurance > 0 < w1.armor:
            w1.defence()
            w2.attack()
            print(f'Выносливость 2: {w2.endurance}\nЗдоровье 1: {w1.health}, Броня 1: {w1.armor}')
        elif w2.endurance <= 0 < w1.armor:
            w1.armor -= random.randint(0, 5)
            w1.health -= random.randint(0, 5)
            print(f'Выносливость 2: {w2.endurance}\nЗдоровье 1: {w1.health}, Броня 1: {w1.armor}')
        else:
            w1.health -= random.randint(0, 10)
            print(f'Выносливость 2: т{w2.endurance}\nЗдоровье 1: {w1.health}, Броня 1: {w1.armor}')
    else:
        print('Оба защищаются')

if w1.health < 10:
    print('Воин 2 победил')
else:
    print('Воин 1 победил')

q1 = input('Pollice verso(y/n): ')
if q1 == 'y':
    print('FATALITY!!!')
elif q1 == 'n':
    print('Помилован!')
