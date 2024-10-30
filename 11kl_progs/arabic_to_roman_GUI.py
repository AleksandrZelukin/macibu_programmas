import tkinter as tk

root = tk.Tk()
root.geometry("300x200")


num_arab = tk.Entry()
num_arab.pack()

def r_to_a():
    number = int(num_arab.get())
    roman_number = {'M':1000, 'CM':900, 'D':500,
                'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40,
                'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}

    roman = ''
    for letter, value in roman_number.items():
        while number >= value:
            roman += letter
            number -= value
    return(roman)

label = tk.Label(text="Konvert arabik skaitlis uz romiešu")
label.pack()

btn = tk.Button(text="Convert",command=r_to_a)
btn.pack()

root.mainloop()
