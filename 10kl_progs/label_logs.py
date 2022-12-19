from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400+800+300')
root.title('Mans pirmais logs')

def start():
    name = atbilde.get()
    #messagebox.showinfo('Sveiki!', '{name}'.format(name=name))
    messagebox.showinfo('Sveiki',name)

info = Label(root,text="Sveiki, draugs!")
info.pack()

jautajums = Label(root, text="Ka tevi sauc?")
jautajums.pack(padx=10, pady=10)

atbilde = Entry(root)
atbilde.pack()

btn = Button(root, text='nospiež mani', command=start)
btn.pack(padx=10, pady=10)
btn2 = Button(root, text='Iziet no progrāmmas', command=root.destroy )
btn2.pack()

root.mainloop()

'''
# Python program to create a close button
# using destroy Non-Class method
from tkinter import *

# Creating the tkinter window
root = Tk()
root.geometry("200x100")

# Button for closing
exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)

root.mainloop()
===========================================================

# Python program to create a close button
# using destroy Non-Class method
from tkinter import *

# Creating the tkinter window
root = Tk()
root.geometry("200x100")

# Function for closing window


def Close():
	root.destroy()


# Button for closing
exit_button = Button(root, text="Exit", command=Close)
exit_button.pack(pady=20)

root.mainloop()
==============================================================

# Python program to create a close button
# using destroy Class method
from tkinter import *

# Class for tkinter window


class Window():
	def __init__(self):

		# Creating the tkinter Window
		self.root = Tk()
		self.root.geometry("200x100")

		# Button for closing
		exit_button = Button(self.root, text="Exit", command=self.root.destroy)
		exit_button.pack(pady=20)

		self.root.mainloop()


# Running test window
test = Window()

====================================================================
# Python program to create a close button
# using destroy Class method
from tkinter import *

# Class for tkinter window


class Window():
	def __init__(self):

		# Creating the tkinter Window
		self.root = Tk()
		self.root.geometry("200x100")

		# Button for closing
		exit_button = Button(self.root, text="Exit", command=self.Close)
		exit_button.pack(pady=20)

		self.root.mainloop()

	# Function for closing window
	def Close(self):
		self.root.destroy()


# Running test window
test = Window()

========================================================================
# Python program to create a close button
# using quit method
from tkinter import *

# Creating the tkinter window
root = Tk()
root.geometry("200x100")

# Button for closing
exit_button = Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=20)

root.mainloop()
exit(0)


'''