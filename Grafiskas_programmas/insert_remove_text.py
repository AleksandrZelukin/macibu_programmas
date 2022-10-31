from tkinter import *
from tkinter import ttk
 
def clear():
    entry.delete(0, END)   # удаление введенного текста
 
def display():
    label["text"] = entry.get()   # получение введенного текста
 
root = Tk()
root.title("Piemers")
root.geometry("600x600")
 
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
 
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
 
# вставка начальных данных
entry.insert(0, "Hello World")
 
display_button = ttk.Button(text="Display", command=display)
display_button.pack(side=LEFT, anchor=N, padx=6, pady=6)
 
clear_button = ttk.Button(text="Clear", command=clear)
clear_button.pack(side=LEFT, anchor=N, padx=6, pady=6)
 
root.mainloop()