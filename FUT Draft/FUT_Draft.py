import tkinter as tk
import ttkbootstrap as ttk


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


def form_433():
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
    zawodnik1_b.grid(row=3, column=6)
    zawodnik2_b.grid(row=3, column=10)
    zawodnik3_b.grid(row=3, column=14)
    zawodnik4_b.grid(row=8, column=6)
    zawodnik5_b.grid(row=8, column=10)
    zawodnik6_b.grid(row=8, column=14)
    zawodnik7_b.grid(row=11, column=5)
    zawodnik8_b.grid(row=11, column=8)
    zawodnik9_b.grid(row=11, column=12)
    zawodnik10_b.grid(row=11, column=15)
    zawodnik11_b.grid(row=15, column=10)


def form_4222():
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
    zawodnik3_b.grid(row=5, column=8)
    zawodnik4_b.grid(row=5, column=12)
    zawodnik5_b.grid(row=8, column=6)
    zawodnik6_b.grid(row=8, column=14)
    zawodnik7_b.grid(row=11, column=5)
    zawodnik8_b.grid(row=11, column=8)
    zawodnik9_b.grid(row=11, column=12)
    zawodnik10_b.grid(row=11, column=15)
    zawodnik11_b.grid(row=15, column=10)


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
