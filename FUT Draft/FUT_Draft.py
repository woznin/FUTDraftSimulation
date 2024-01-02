import ttkbootstrap as ttk
import random
from Zawodnicy import Zawodnik



def pokaz_opcje_turnieju():
    przycisk_graj.grid_forget()
    przywitanie.configure(text='Wybierz rozmiar turnieju!')
    przycisk_4 = ttk.Button(root, text='4 Drużyny', command=lambda: pokaz_opcje_ustawienia(4))
    przycisk_8 = ttk.Button(root, text='8 Drużyn', command=lambda: pokaz_opcje_ustawienia(8))
    przycisk_16 = ttk.Button(root, text='16 Drużyn', command=lambda: pokaz_opcje_ustawienia(16))
    przycisk_4.grid(row=6, column=8, rowspan=1, columnspan=3, sticky='news')
    przycisk_8.grid(row=8, column=8, rowspan=1, columnspan=3, sticky='news')
    przycisk_16.grid(row=10, column=8, rowspan=1, columnspan=3, sticky='news')


def pokaz_opcje_ustawienia(ilosc_druzyn):
    global rozmiar
    rozmiar = ilosc_druzyn
    for przyciski in root.winfo_children():
        przyciski.destroy()
    header = ttk.Label(root, text='Wybierz formacje drużyny!', font='Calibri 24')
    header.grid(row=2, column=10)
    przycisk_form_433 = ttk.Button(root, text='4-3-3', command=form_433)
    przycisk_form_4222 = ttk.Button(root, text='4-2-2-2', command=form_4222)
    przycisk_form_532 = ttk.Button(root, text='5-3-2', command=form_532)
    przycisk_form_433.grid(row=6, column=8, rowspan=1, columnspan=3, sticky='news')
    przycisk_form_4222.grid(row=8, column=8, rowspan=1, columnspan=3, sticky='news')
    przycisk_form_532.grid(row=10, column=8, rowspan=1, columnspan=3, sticky='news')


def czy_zostaly_przyciski():
    widgets = root.grid_slaves()
    przyciski = sum(1 for przycisk in widgets if isinstance(przycisk, ttk.Button))
    if przyciski == 0:
        return True
    else:
        return False


def wyswietl_opcje(pozycja, przycisk_uzyty):
    ramka = ttk.Frame(root, height=125, width=800)
    ramka.grid(row=17, column=0, rowspan=3, columnspan=20)
    temp_zawodnicy = []
    for i in range(5):
        temp_zawodnik = Zawodnik()
        temp_zawodnik.przydziel_atrybuty()
        temp_zawodnik.pozycja = pozycja
        temp_zawodnicy.append(temp_zawodnik)
    zaw1 = ttk.Button(ramka, image=zdj, text=temp_zawodnicy[0].nazwa + " " + str(temp_zawodnicy[0].ovr), compound=ttk.BOTTOM, command=lambda: wybrano_zawodnika(ramka, temp_zawodnicy[0], przycisk_uzyty))
    zaw2 = ttk.Button(ramka, image=zdj, text=temp_zawodnicy[1].nazwa + " " + str(temp_zawodnicy[1].ovr), compound=ttk.BOTTOM, command=lambda: wybrano_zawodnika(ramka, temp_zawodnicy[1], przycisk_uzyty))
    zaw3 = ttk.Button(ramka, image=zdj, text=temp_zawodnicy[2].nazwa + " " + str(temp_zawodnicy[2].ovr), compound=ttk.BOTTOM, command=lambda: wybrano_zawodnika(ramka, temp_zawodnicy[2], przycisk_uzyty))
    zaw4 = ttk.Button(ramka, image=zdj, text=temp_zawodnicy[3].nazwa + " " + str(temp_zawodnicy[3].ovr), compound=ttk.BOTTOM, command=lambda: wybrano_zawodnika(ramka, temp_zawodnicy[3], przycisk_uzyty))
    zaw5 = ttk.Button(ramka, image=zdj, text=temp_zawodnicy[4].nazwa + " " + str(temp_zawodnicy[4].ovr), compound=ttk.BOTTOM, command=lambda: wybrano_zawodnika(ramka, temp_zawodnicy[4], przycisk_uzyty))
    zaw1.pack(side=ttk.LEFT)
    zaw2.pack(side=ttk.LEFT)
    zaw3.pack(side=ttk.LEFT)
    zaw4.pack(side=ttk.LEFT)
    zaw5.pack(side=ttk.LEFT)


def wybrano_zawodnika(ramka, zawodnik, przycisk_uzyty):
    ramka.destroy()
    info = przycisk_uzyty.grid_info()
    rzad = info['row']
    kolumna = info['column']
    przycisk_uzyty.destroy()
    sklad.append(zawodnik)
    label = ttk.Label(root, style='NoBorder.TButton', image=zdj, text=zawodnik.nazwa + " " + str(zawodnik.ovr), compound=ttk.BOTTOM)
    label.grid(row=rzad, column=kolumna, rowspan=2, columnspan=3)
    if czy_zostaly_przyciski():
        przejdz_dalej = ttk.Button(root, text="przejdz dalej")
        przejdz_dalej.grid(row=15, column=16)

def form_433():
    for przyciski in root.winfo_children():
        przyciski.destroy()
    zawodnik1_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('napastnik', zawodnik1_b))
    zawodnik2_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('napastnik', zawodnik2_b))
    zawodnik3_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('napastnik', zawodnik3_b))
    zawodnik4_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('pomocnik', zawodnik4_b))
    zawodnik5_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('pomocnik', zawodnik5_b))
    zawodnik6_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('pomocnik', zawodnik6_b))
    zawodnik7_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('obronca', zawodnik7_b))
    zawodnik8_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('obronca', zawodnik8_b))
    zawodnik9_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('obronca', zawodnik9_b))
    zawodnik10_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('obronca', zawodnik10_b))
    zawodnik11_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('bramkarz', zawodnik11_b))
    zawodnik1_b.grid(row=2, column=6, rowspan=2, columnspan=3)
    zawodnik2_b.grid(row=2, column=9, rowspan=2, columnspan=3)
    zawodnik3_b.grid(row=2, column=12, rowspan=2, columnspan=3)
    zawodnik4_b.grid(row=7, column=6, rowspan=2, columnspan=3)
    zawodnik5_b.grid(row=7, column=9, rowspan=2, columnspan=3)
    zawodnik6_b.grid(row=7, column=12, rowspan=2, columnspan=3)
    zawodnik7_b.grid(row=12, column=3, rowspan=2, columnspan=3)
    zawodnik8_b.grid(row=12, column=7, rowspan=2, columnspan=3)
    zawodnik9_b.grid(row=12, column=11, rowspan=2, columnspan=3)
    zawodnik10_b.grid(row=12, column=15, rowspan=2, columnspan=3)
    zawodnik11_b.grid(row=14, column=9, rowspan=2, columnspan=3)


def form_4222():
    for przyciski in root.winfo_children():
        przyciski.destroy()
    zawodnik1_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('napastnik', zawodnik1_b))
    zawodnik2_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('napastnik', zawodnik2_b))
    zawodnik3_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('pomocnik', zawodnik3_b))
    zawodnik4_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('pomocnik', zawodnik4_b))
    zawodnik5_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('pomocnik', zawodnik5_b))
    zawodnik6_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('pomocnik', zawodnik6_b))
    zawodnik7_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('obronca', zawodnik7_b))
    zawodnik8_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('obronca', zawodnik8_b))
    zawodnik9_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('obronca', zawodnik9_b))
    zawodnik10_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('obronca', zawodnik10_b))
    zawodnik11_b = ttk.Button(root, image=zdj, style='NoBorder.TButton', command=lambda: wyswietl_opcje('bramkarz', zawodnik11_b))
    zawodnik1_b.grid(row=1, column=7, rowspan=2, columnspan=4)
    zawodnik2_b.grid(row=1, column=11, rowspan=2, columnspan=4)
    zawodnik3_b.grid(row=5, column=7, rowspan=2, columnspan=4)
    zawodnik4_b.grid(row=5, column=11, rowspan=2, columnspan=4)
    zawodnik5_b.grid(row=7, column=5, rowspan=2, columnspan=4)
    zawodnik6_b.grid(row=7, column=13, rowspan=2, columnspan=4)
    zawodnik7_b.grid(row=12, column=3, rowspan=2, columnspan=4)
    zawodnik8_b.grid(row=12, column=7, rowspan=2, columnspan=4)
    zawodnik9_b.grid(row=12, column=11, rowspan=2, columnspan=4)
    zawodnik10_b.grid(row=12, column=15, rowspan=2, columnspan=4)
    zawodnik11_b.grid(row=14, column=9, rowspan=2, columnspan=4)


def form_532():
    for przyciski in root.winfo_children():
        przyciski.destroy()
    zawodnik1_b = ttk.Button(root, image=zdj, style='NoBorder.TButton')
    zawodnik2_b = ttk.Button(root, image=zdj, style='NoBorder.TButton')
    zawodnik3_b = ttk.Button(root, image=zdj, style='NoBorder.TButton')
    zawodnik4_b = ttk.Button(root, image=zdj, style='NoBorder.TButton')
    zawodnik5_b = ttk.Button(root, image=zdj, style='NoBorder.TButton')
    zawodnik6_b = ttk.Button(root, image=zdj, style='NoBorder.TButton')
    zawodnik7_b = ttk.Button(root, image=zdj, style='NoBorder.TButton')
    zawodnik8_b = ttk.Button(root, image=zdj, style='NoBorder.TButton')
    zawodnik9_b = ttk.Button(root, image=zdj, style='NoBorder.TButton')
    zawodnik10_b = ttk.Button(root, image=zdj, style='NoBorder.TButton')
    zawodnik11_b = ttk.Button(root, image=zdj, style='NoBorder.TButton')
    zawodnik1_b.grid(row=1, column=8)
    zawodnik2_b.grid(row=1, column=12)
    zawodnik4_b.grid(row=6, column=6)
    zawodnik5_b.grid(row=6, column=10)
    zawodnik6_b.grid(row=6, column=14)
    zawodnik7_b.grid(row=11, column=4)
    zawodnik8_b.grid(row=11, column=7)
    zawodnik9_b.grid(row=11, column=10)
    zawodnik3_b.grid(row=11, column=13)
    zawodnik10_b.grid(row=11, column=16)
    zawodnik11_b.grid(row=15, column=10)


root = ttk.Window(themename='darkly')
root.title('FUT Draft')
root.geometry('800x900')
global zdj
zdj = ttk.PhotoImage(file='blank_zawodnik.png')
global sklad
sklad = []
style1 = ttk.Style()
style1.configure('NoBorder.TButton', borderwidth=0)
for i in range(20):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)
przywitanie = ttk.Label(root, text='Witamy w symulatorze', font='Calibri 24')
przycisk_graj = ttk.Button(root, text='Symuluj!', command=pokaz_opcje_turnieju)
przywitanie.grid(row=2, column=10)
przycisk_graj.grid(row=8, column=8, rowspan=4, columnspan=3)


root.resizable(False, False)
root.mainloop()






#jest tu taka wstepna wersja rozgrywki meczu z karnymi, sprawdzałem na roznych przykladach i dziala w miare jest zroznicowanie wygranych i jezeli druzyna jest widocznie lepsza to ma duzo wiecej tyc wygranych
#po wyborze zawodnikow sprawdz sobie wynik itpo podalem nizej jakas losowa 2 druzyne
def rozklad_skladu(sklad):
    lista = []
    for zawodnik in sklad:
        lista.append(zawodnik.ovr)
    return lista

def oceny(sklad):
    nap = 0
    pom = 0
    obr = 0
    br = 0
    ocenki = []
    for zawodnik in sklad:
        if zawodnik.pozycja == "napastnik":
            nap += zawodnik.ovr
        elif zawodnik.pozycja == "pomocnik":
            pom += zawodnik.ovr
        elif zawodnik.pozycja == "obronca":
            obr += zawodnik.ovr
        elif zawodnik.pozycja == "bramkarz":
            br = zawodnik.ovr
    ocenki = [nap, pom, obr, br]
    return ocenki



def losuj_z_prawdopodobienstwem(prawdopodobienstwo_1):
    choices = [0, 1]
    wynik = random.choices(choices, weights=[1 - prawdopodobienstwo_1, prawdopodobienstwo_1])[0]
    return wynik



def karne(x, y):
    karne_1 = 0
    karne_2 = 0

    for i in range(10):
        p1 = x[i] / (x[i] + y[10])
        if losuj_z_prawdopodobienstwem(p1) == 1:
            karne_1 += 1

        p2 = y[i] / (y[i] + x[10])
        if losuj_z_prawdopodobienstwem(p2) == 1:
            karne_2 += 1

        print(f"{karne_1}:{karne_2}")
        if karne_1 > karne_2:
            wygrana_drużyna = "1"
        else:
            wygrana_drużyna = "2"

        if i >= 4 and karne_1 > karne_2:
            print("Wygrywa drużyna: ", wygrana_drużyna)
            break
        elif i >= 4 and karne_2 > karne_1:
            print("wygrywa druzyna:", wygrana_drużyna)
            break
        elif i >= 2 and abs(karne_1 - karne_2) == 3:
            print(" wygrywa drużyna:", wygrana_drużyna)
            break
        elif i >= 3 and abs(karne_1 - karne_2) >= 2:
            print("wygrywa drużyna:", wygrana_drużyna)
            break

    return karne_1, karne_2
def rozgrywka(x, y):
    gole_1 = 0
    gole_2 = 0

    for _ in range(3):
        # nap1 vs obr2
        if x[0] >= y[2]:
            p = x[0] / (x[0] + y[2])
            if losuj_z_prawdopodobienstwem(p) == 1:
                gole_1 += 1
        # pom1 vs pom2
        if x[1] >= y[1]:
            p = x[1] / (x[1] + y[1])
            if losuj_z_prawdopodobienstwem(p) == 1:
                gole_1 += 1
        if y[1] >= x[1]:
            p = y[1] / (y[1] + x[1])
            if losuj_z_prawdopodobienstwem(p) == 1:
                gole_2 += 1
        # nap2 vs obr1
        if y[0] >= x[2]:
            p = y[0] / (y[0] + x[2])
            if losuj_z_prawdopodobienstwem(p) == 1:
                gole_2 += 1



    print(f"{gole_1}:{gole_2}")
    if gole_1 > gole_2:
        print("wygrywa drużyna 1:")
    elif gole_1 < gole_2:
        print("wygrywa drużyna 2:")
    if gole_1 == gole_2:
        print("Czeka nas dogrywka!")
        karne(sklad_x,sklad_y)

sklad_x = rozklad_skladu(sklad)
sklad_y = [90, 90, 90, 80, 88, 80, 80, 80, 90, 90, 80]
x = oceny(sklad)
y = [240, 230, 330, 80]
rozgrywka(x,y)

