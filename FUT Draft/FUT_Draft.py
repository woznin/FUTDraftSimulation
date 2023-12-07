import tkinter as tk
import ttkbootstrap as ttk


def pokaz_opcje():
    przycisk_graj.grid_forget()
    przywitanie.configure(text='Wybierz rozmiar turnieju!')
    przycisk_4 = ttk.Button(root, text='4 Drużyny')
    przycisk_8 = ttk.Button(root, text='8 Drużyn')
    przycisk_16 = ttk.Button(root, text='16 Drużyn')
    przycisk_4.grid(row=6, column=8, rowspan=1, columnspan=3, sticky='news')
    przycisk_8.grid(row=8, column=8, rowspan=1, columnspan=3, sticky='news')
    przycisk_16.grid(row=10, column=8, rowspan=1, columnspan=3, sticky='news')


root = ttk.Window(themename='darkly')
root.title('FUT Draft')
root.geometry('800x900')
for i in range(20):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)
przywitanie = ttk.Label(root, text='Witamy w symulatorze', font='Calibri 24')
przycisk_graj = ttk.Button(root, text='Symuluj!', command=pokaz_opcje)
przywitanie.grid(row=2, column=10)
przycisk_graj.grid(row=8, column=8, rowspan=4, columnspan=3)



root.resizable(False, False)
root.mainloop()
