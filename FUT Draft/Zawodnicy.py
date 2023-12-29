import random


class Zawodnik:

    def __init__(self):
        self.atk = 0
        self.pom = 0
        self.deff = 0
        self.ovr = 0
        self.nazwa = ''
        self.pozycja = ''


    def przydziel_atrybuty(self, minimum=65, maximum=95):
        self.deff = round(random.uniform(minimum, maximum))
        self.atk = round(random.uniform(minimum, maximum))
        self.pom = round(random.uniform(minimum, maximum))
        temp = open('nazwiska.txt').read().splitlines()
        temp2 = 'ABCDEFGHIJKLMNOPRSTUVWZ'
        self.nazwa = random.choice(temp2) + '. ' + random.choice(temp)
        self.ovr = round((self.atk+self.deff+self.pom)/3)

    def wyswietl_atrybuty(self):
        print(f"Imie i nazwisko {self.nazwa}")
        print(f"Atk {self.atk}")
        print(f"Pom {self.pom}")
        print(f"Def {self.deff}")
        print(f"OVR {self.ovr}")
        print(f"Pozycja {self.pozycja}")

