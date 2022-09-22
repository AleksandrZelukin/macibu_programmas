import tkinter as tk
import time

root = tk.Tk()
app = Application(master=root)
root.geometry("600x600")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, font="Verdana", bg="red", fg="black", width=7, height=4)
        self.hi_there["text"] = "Hello User\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", font="Arial", fg="red", bg="white",  width=7,height=4, command=root.destroy)
        self.quit.pack(side="bottom")

        self.button = tk.Button(self)
        self.button['text'] = time.strftime('%H:%M:%S')
        self.button['command'] = self.button_clicked
        self.button.pack(side="bottom")

    def say_hi(self):
        print("text after press the button")

    def button_clicked(self):
        self.button['text'] = time.strftime('%H:%M:%S')



app.mainloop()
