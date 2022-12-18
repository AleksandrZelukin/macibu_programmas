from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Ieeja programma')
root.geometry('400x300')
root.resizable(width=False, height=False)
root['bg'] = 'black'

def ieeja():
    username = username_entry.get()
    parole = password_entry.get()

    messagebox.showinfo(username, parole)

main_label = Label(root, text='Autorizacija', bg='black', fg='white')
main_label.pack()

username_label = Label(root, text='User', bg='black', fg='white', padx=10, pady=8)
username_label.pack()

username_entry = Entry(root, bg='black', fg='lime')
username_entry.pack()

password_label = Label(root, text='Parole', bg='black', fg='white', padx=10, pady=8)
password_label.pack()

password_entry = Entry(root, bg='black', fg='lime')
password_entry.pack()

send_btn = Button(root, text='Ieeja', bg='red', fg='blue', command=ieeja)
send_btn.pack(padx=10, pady=10)

root.mainloop()