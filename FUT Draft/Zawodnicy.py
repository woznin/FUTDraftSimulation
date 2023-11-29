import random


class Zawodnik:

    def __init__(self):
        self.atk = 0
        self.deff = 0
        self.nazwa = ''

    def przydziel_atrybuty(self, minimum=65, maximum=95):
        self.deff = round(random.uniform(minimum, maximum))
        self.atk = round(random.uniform(minimum, maximum))
        temp = open('nazwiska.txt').read().splitlines()
        temp2 = 'ABCDEFGHIJKLMNOPRSTUVWZ'
        self.nazwa =random.choice(temp2) + '. ' + random.choice(temp)

    def wyswietl_atrybuty(self):
        print(self.nazwa)
        print(self.atk)
        print(self.deff)


x = Zawodnik()
x.przydziel_atrybuty()
x.wyswietl_atrybuty()
