from tkinter import *

def deplacement():
    global dx, dy
    if canvas.coords(ball)[3]>400:
        dy=-1*dy
    canvas.move(ball,dx,dy)
    fenetre.after(20,deplacement)

dx = 0
dy = 5
Pos_X=60
Pos_Y=10

fenetre = Tk()
canvas = Canvas(fenetre, width=1080, height=720)
canvas.pack(padx=10, pady=10)
ball = canvas.create_oval(Pos_X,Pos_Y,Pos_X+20,Pos_Y+20, fill='red')

deplacement()

fenetre.mainloop()