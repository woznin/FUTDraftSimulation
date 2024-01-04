import random


class Zawodnik:

    def __init__(self):
        self.ovr = 0
        self.nazwa = ''
        self.pozycja = ''


    def przydziel_atrybuty(self, minimum=65, maximum=95):
        temp = open('nazwiska.txt').read().splitlines()
        temp2 = 'ABCDEFGHIJKLMNOPRSTUVWZ'
        self.nazwa = random.choice(temp2) + '. ' + random.choice(temp)
        self.ovr = round(random.uniform(minimum, maximum))

    def wyswietl_atrybuty(self):
        print(f"Imie i nazwisko {self.nazwa}")
        print(f"OVR {self.ovr}")
        print(f"Pozycja {self.pozycja}")

