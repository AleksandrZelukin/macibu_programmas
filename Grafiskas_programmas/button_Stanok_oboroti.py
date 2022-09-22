from tkinter import Tk, Button, Label, LabelFrame, mainloop
from functools import partial


SIGNAL = int

class App(Tk):
    normal_engine_speed = 1500
    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self):
        self.title("Управление станком")
        self["bg"] = "gray22"
        self.geometry("300x150+500+300")
        self.resizable(False, False)

        title_label = Label(self, text="Обороты двигателя")
        title_label.config(font="Times 18 bold", fg="green")
        title_label.place(x=40)

        button_reduce_speed = Button(self, text="-10")
        button_reduce_speed.config(font="Times 13 bold", fg="blue")
        button_reduce_speed.bind('<Button-1>', partial(self.button_click_handler, 0))
        button_reduce_speed.place(x=0, y=0)

        button_add_speed = Button(self, text="+10")
        button_add_speed.config(font="Times 13 bold", fg="blue")
        button_add_speed.bind('<Button-1>', partial(self.button_click_handler, 1))
        button_add_speed.place(x=261, y=0)

        self.show_engine_speed = Label(self, text=self.normal_engine_speed)
        self.show_engine_speed.config(font="Times 30 bold", bg="black", fg="green")
        self.show_engine_speed.config(width=13, height=2)
        self.show_engine_speed.place(y=40)

    def button_click_handler(self, SIGNAL, event):
        if SIGNAL == 0:
            self.normal_engine_speed -= 10
        elif SIGNAL == 1:
            self.normal_engine_speed += 10
        self.show_engine_speed["text"] = self.normal_engine_speed


if __name__ == "__main__":
    app = App()
    app.mainloop()
