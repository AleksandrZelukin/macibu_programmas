import tkinter as tk

root = tk.Tk()
root.geometry("300x200+800+400")


num_arab = tk.Entry()
roman_number = {'M':1000, 'CM':900, 'D':500,
                'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40,
                'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}

def r_to_a(number):
    number = int(num_arab.get())
    roman = ''
    for letter, value in roman_number.items():
        while number >= value:
            roman += letter
            number -= value
    return roman

label = tk.Label(text="Konvert arabik skaitlis uz romiešu")
label.pack()

num_arab.pack()
btn = tk.Button(text="Convert",command=r_to_a)
btn.pack()

root.mainloop()
