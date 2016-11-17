# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def __init__(self):
        self._health = 200
        self._attack = 10
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        super(GreenDragon,self).__init__()
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.
class RedDragon(Dragon):
    def __init__(self):
        super(RedDragon,self).__init__()
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
class BlackDragon(Dragon):
    def __init__(self):
        super(BlackDragon,self).__init__()
        self._color = 'черный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
class Troll(Attacker):
    def __init__(self):
        self._health = 99999999999999999
        self._attack = 50
    def set_answer(self, answer):
        self.__answer = answer
    def question(self):
        self.__quest = 'Угадай число от 1 до 5'
        x = randint(1,5)
        self.set_answer(x)
        return self.__quest
    def check_answer(self, answer):
        return answer == self.__answer

enemy_types = [GreenDragon, RedDragon, BlackDragon, Troll]