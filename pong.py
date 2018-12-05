from tkinter import *

def deplacement():
    global Pos_X, Pos_Y
    canvas.move(ball, Pos_X, Pos_Y)
    fenetre.after(20, deplacement)

def bas1(event):
    canvas.move(raquette, 0, 20)

def bas2(event):
    canvas.move(raquette2, 0, 20)

def haut1(event):
    canvas.move(raquette, 0, -20)

def haut2(event):
    canvas.move(raquette2, 0, -20)

raqx0 = 70
raqy0 = 300
raqx1 = 60
raqy1 = 420

raq2x0 = 1010
raq2y0 = 300
raq2x1 = 1020
raq2y1 = 420

Pos_X = 500
Pos_Y = 300

fenetre = Tk()
canvas = Canvas(fenetre, width=1080, height=720, bg='black')
canvas.pack(padx=10, pady=10)
ball = canvas.create_oval(Pos_X, Pos_Y, Pos_X+20, Pos_Y+20, fill='white')
raquette = canvas.create_rectangle(raqx0, raqy0, raqx1, raqy1, fill='white')
raquette2 = canvas.create_rectangle(raq2x0, raq2y0, raq2x1, raq2y1, fill='white')

canvas.bind_all('<s>', bas1)
canvas.bind_all('<Down>', bas2)
canvas.bind_all('<z>', haut1)
canvas.bind_all('<Up>', haut2)

deplacement()

fenetre.mainloop()