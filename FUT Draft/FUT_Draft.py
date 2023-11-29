import tkinter as tk
import ttkbootstrap as ttk


root = ttk.Window(themename='darkly')
root.title('FUT Draft')
root.geometry('800x900')
for i in range(20):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)
przywitanie = ttk.Label(root, text='Witamy w symulatorze', font='Calibri 24')
przycisk_graj = ttk.Button(root, text='Symuluj!')
przywitanie.grid(row=2, column=10)
przycisk_graj.grid(row=8, column=8, rowspan=4, columnspan=3)
root.resizable(False, False)
root.mainloop()
