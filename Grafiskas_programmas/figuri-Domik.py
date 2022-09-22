from tkinter import *
root=Tk()
root.geometry("450x300+300+300")

canvas= Canvas(root, width=400, height=250, bg="salmon") # fona krasa
canvas.create_rectangle(110, 160, 290, 250, outline="black", fill="yellow") #fasade
points = [100, 160, 300, 160, 200, 90]
canvas.create_polygon(points, outline="black", fill="red", width=2) #Jumta
canvas.create_oval(10, 10, 80, 80, outline="gray", fill="yellow", width=4) #Saule
canvas.create_rectangle(180, 200, 220, 170, outline="black", fill="black") #Logs
#Saules stars
canvas.create_line(90, 45, 150, 50, width=6, fill="yellow")
canvas.create_line(90, 60, 140, 80, width=6, fill="yellow")
canvas.create_line(80, 75, 140, 110, width=6, fill="yellow")
canvas.create_line(70, 85, 110, 130, width=6, fill="yellow")
canvas.create_line(50, 90, 80, 150, width=6, fill="#00ffff")



def lodzins ():
    canvas.create_rectangle(180, 200, 220, 170, outline="black", fill="white")
    
def lodzins2 ():
    canvas.create_rectangle(180, 200, 220, 170, outline="black", fill="black")
    #canvas.delete(ALL)


canvas.create_text(200, 125, text="RĪGAS\n92.\vidusskola",justify=CENTER, font="Arial 14", fill="lightblue")
canvas.create_text(200, 250, text="Autors 10.b skolnieks",justify=CENTER, anchor=S, fill="lightgrey")


canvas.pack()

poga=Button(text="Light on!", command=lodzins)
poga2=Button(text="Light off!", command=lodzins2)

poga.pack()
poga2.pack()


root.mainloop()
