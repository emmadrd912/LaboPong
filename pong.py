from tkinter import *

def deplacement():
    global dx, dy
    canvas.move(ball,dx,dy)
    fenetre.after(20,deplacement)

def bas1(event):
    canvas.move(raquette, 0, 10)

def bas2(event):
    canvas.move(raquette2, 0, 10)

def haut1(event):
    canvas.move(raquette, 0, -10)

def haut2(event):
    canvas.move(raquette2, 0, -10)

dx = 0
dy = 5
Pos_X=60
Pos_Y=10

fenetre = Tk()
canvas = Canvas(fenetre, width=1080, height=720, bg='black')
canvas.pack(padx=10, pady=10)
ball = canvas.create_oval(Pos_X, Pos_Y, Pos_X+20, Pos_Y+20, fill='white')
raquette = canvas.create_rectangle(70, 300, 60, 420, fill='white')
raquette2 = canvas.create_rectangle(1010, 300, 1020, 420, fill='white')

canvas.bind_all('<s>', bas1)
canvas.bind_all('<Down>', bas2)
canvas.bind_all('<z>', haut1)
canvas.bind_all('<Up>', haut2)

deplacement()

fenetre.mainloop()