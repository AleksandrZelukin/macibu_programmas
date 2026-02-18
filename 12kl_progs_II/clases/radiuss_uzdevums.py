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
    
    def XXXXXXXX(self, radiuss):  #konstruktors ar parametru radiuss
        self.radiuss = radiuss   #konstruktorā inicializēt parametru sākumvērtību.

    def XXXXXXXXX(self, radiuss):
        if(radiuss <0 or radiuss == 0):  #ja rādiuss ir nulle vai negatīvs
            self.radiuss = 1  #tad uzstāda noklusējuma rādiusu 1
        else:                
            self.radiuss = radiuss # citādi rādiuss ir metodē dotais rādiuss

    def XXXXXXXXXX(self): #izvada rādiusu
        print(self.radiuss)

    def XXXXXXXXXX(self):   #aprēķina diametru
         print(2 * self.radiuss)

default_radius = 1

class Rinkis:
    def __init__(self, radiuss=default_radius):
        self.radiuss = radiuss

    def iestatit_radiusu(self, radiuss):
        if radiuss <= 0:
            self.radiuss = default_radius
        else:
            self.radiuss = radiuss

    def izvadit_radiusu(self):
        return self.radiuss

    def diametrs(self):
        return 2 * self.radiuss

# --- Tkinter GUI ---
def update_circle():
    try:
        r = float(radius_entry.get())
    except ValueError:
        messagebox.showerror("Kļūda", "Lūdzu, ievadiet skaitlisku rādiusu!")
        return
    rinkis.iestatit_radiusu(r)
    radius_var.set(f"Rādiuss: {rinkis.izvadit_radiusu()}")
    diameter_var.set(f"Diametrs: {rinkis.diametrs()}")

rinkis = Rinkis()

root = tk.Tk()
root.title("Riņķa kalkulators")
root.geometry("300x200")

tk.Label(root, text="Ievadiet rādiusu:").pack(pady=5)
radius_entry = tk.Entry(root)
radius_entry.pack(pady=5)

tk.Button(root, text="Aprēķināt", command=update_circle).pack(pady=5)

radius_var = tk.StringVar()
diameter_var = tk.StringVar()
radius_var.set("Rādiuss: ")
diameter_var.set("Diametrs: ")

tk.Label(root, textvariable=radius_var).pack(pady=2)
tk.Label(root, textvariable=diameter_var).pack(pady=2)

root.mainloop()

