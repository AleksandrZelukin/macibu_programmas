import tkinter as tk
from tkinter import messagebox

'''
1. uzdevums

Izveidot klasi "Rinkis", ar atribūtu "radiuss". 
Konstruktorā inicializēt parametru sākumvērtību. 
Ja metodē nepadod argumentus, tas sākumvērtības pēc noklusējuma uzstāda uz 1.

Jārealizē sekojošas metodes:  

1. Konstruktors #konstruktors ar parametru radiuss
2. iestatit_radiusu(radiuss) #uzstāda jaunu rādiusu, 
    ja rādiuss ir nulle vai negatīvs, tad uzstāda noklusējuma rādiusu 1.
3. izvadit_radiusu()  #izvada rādiusu
4. diametrs() # aprēķina diametru un izdrukā to

'''

class Rinkis:   #Izveidot klasi "Rinkis"
    
    def __init__(self, radiuss):  #konstruktors ar parametru radiuss
        self.radiuss = radiuss   #konstruktorā inicializēt parametru sākumvērtību.

    def iestatit_radiusu(self, radiuss):
        if(radiuss <0 or radiuss == 0):  #ja rādiuss ir nulle vai negatīvs
            self.radiuss = 1  #tad uzstāda noklusējuma rādiusu 1
        else:                
            self.radiuss = radiuss # citādi rādiuss ir metodē dotais rādiuss

    def izvadit_radiusu(self): #izvada rādiusu
        print(self.radiuss)

    def diametrs(self):   #aprēķina diametru
         print(2 * self.radiuss)

# rad1=Rinkis(0)
# rad1.diametrs()
# rad1.iestatit_radiusu()
# rad1.izvadit_radiusu()

def set_radius():
    try:
        r = float(radius_entry.get())
        rad1.iestatit_radiusu(r)
        messagebox.showinfo("Info", f"Rādiuss uzstādīts uz {rad1.radiuss}")
    except ValueError:
        messagebox.showerror("Kļūda", "Lūdzu, ievadiet skaitlisku vērtību!")

def show_radius():
    messagebox.showinfo("Rādiuss", f"Rādiuss: {rad1.radiuss}")

def show_diameter():
    diam = 2 * rad1.radiuss
    messagebox.showinfo("Diametrs", f"Diametrs: {diam}")

root = tk.Tk()
root.title("Riņķa kalkulators")

tk.Label(root, text="Ievadiet rādiusu:").pack(pady=5)
radius_entry = tk.Entry(root)
radius_entry.pack(pady=5)

tk.Button(root, text="Uzstādīt rādiusu", command=set_radius).pack(pady=5)
tk.Button(root, text="Parādīt rādiusu", command=show_radius).pack(pady=5)
tk.Button(root, text="Parādīt diametru", command=show_diameter).pack(pady=5)

root.mainloop()
    
