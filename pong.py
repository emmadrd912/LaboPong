from tkinter import *

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
dx = -3
dy = 6

score=0

def jouer():
    def bas1(event):
        canvas.move(raquette, 0, 30)

    def bas2(event):
        canvas.move(raquette2, 0, 30)

    def haut1(event):
        canvas.move(raquette, 0, -30)

    def haut2(event):
        canvas.move(raquette2, 0, -30)

    def deplacement():
        global dx, dy
        if canvas.coords(ball)[3]>720:
            dy = -1*dy
        if canvas.coords(ball)[3]<10:
            dy = -1*dy 
        if canvas.coords(ball)[3]>canvas.coords(raquette)[1] and canvas.coords(ball)[0]<canvas.coords(raquette)[2] and canvas.coords(ball)[2]>canvas.coords(raquette)[0]:
            dx=-1*dx
        if canvas.coords(ball)[3]>canvas.coords(raquette2)[1] and canvas.coords(ball)[0]<canvas.coords(raquette2)[2] and canvas.coords(ball)[2]>canvas.coords(raquette2)[0]:
            dx=-1*dx       
        canvas.move(ball,dx,dy)
        fenetre.after(20,deplacement)

    menu.destroy()
    fenetre = Tk()
    fenetre.title("Jeu Pong")


    canvas = Canvas(fenetre, width=1080, height=720, bg='black')
    canvas.pack(padx=10, pady=10)
    canvas.create_line(540,0,540,720, fill='white') 
    ball = canvas.create_oval(Pos_X, Pos_Y, Pos_X+20, Pos_Y+20, fill='white')
    raquette = canvas.create_rectangle(raqx0, raqy0, raqx1, raqy1, fill='white')
    raquette2 = canvas.create_rectangle(raq2x0, raq2y0, raq2x1, raq2y1, fill='white')

    canvas.bind_all('<s>', bas1)
    canvas.bind_all('<Down>', bas2)
    canvas.bind_all('<z>', haut1)
    canvas.bind_all('<Up>', haut2)

    deplacement()
    fenetre.mainloop()

def instruction():
    fenetre = Tk()
    fenetre.title("Instruction et commande")
    label = Label(fenetre, text="Commande : ", bg="grey")
    label.pack()
    label = Label(fenetre, text=" Joueur 1 = z & s")
    label.pack()
    label = Label(fenetre, text=" Joueur 2 = ↑ & ↓ ")
    label.pack()
    label = Label(fenetre, text="Instruction: ", bg="grey")
    label.pack()
    label = Label(fenetre, text="Le but du jeu est de faire rebondir la balle sur les raquettes de chaque joueur (comme un tennis de table).")
    label.pack()
    label = Label(fenetre, text="Les raquettes se déplacent de haut en bas. Lorsqu'un joueur laisse passer la balle, l'autre joueur gagne 1 point.")
    label.pack()

menu = Tk()
menu.title("[Pong]")
menu.geometry("260x120")
 
ButtonJouer = Button(menu, text ="   Jouer   ", command = jouer)
ButtonJouer.pack(padx = 5, pady = 5)
 
ButtonInstruction = Button(menu,text="Instruction et Commande", command= instruction)
ButtonInstruction.pack(padx = 10, pady = 5)

ButtonQuitter = Button(menu, text ="   Quitter    ", command = menu.destroy)
ButtonQuitter.pack(padx = 5, pady = 5)

menu.mainloop()