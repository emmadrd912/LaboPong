from tkinter import *

def jeupong():
    canvas.move(ball, 3, 3)
    fenetre.after(10, jeupong)
    
fenetre = Tk()
canvas = Canvas(fenetre, width=1080, height=720)
canvas.pack()
ball = canvas.create_oval(50,50,100,100)

jeupong()

fenetre.mainloop()