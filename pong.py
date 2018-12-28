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

score = 0
score2 = 0

def jouer():
    global menu
    
    def bas1(event):
        canvas.move(raquette, 0, 30)

    def bas2(event):
        canvas.move(raquette2, 0, 30)

    def haut1(event):
        canvas.move(raquette, 0, -30)

    def haut2(event):
        canvas.move(raquette2, 0, -30)

    def deplacement():
        global dx, dy, score, button7
        if canvas.coords(ball)[3]>720:
            dy = -1*dy
        if canvas.coords(ball)[3]<10:
            dy = -1*dy 
        if canvas.coords(ball)[3]>canvas.coords(raquette)[1] and canvas.coords(ball)[0]<canvas.coords(raquette)[2] and canvas.coords(ball)[2]>canvas.coords(raquette)[0]:
            dx=-1*dx
        if canvas.coords(ball)[3]>canvas.coords(raquette2)[1] and canvas.coords(ball)[0]<canvas.coords(raquette2)[2] and canvas.coords(ball)[2]>canvas.coords(raquette2)[0]:
            dx=-1*dx 
        if canvas.coords(ball)[0]<10:
            score = score + 1
            TextGame.set("Joueur 1 : "+ str(score)) 
        canvas.move(ball,dx,dy)
        jouer.after(20,deplacement)

    
    jouer = Tk()
    jouer.title("Jeu Pong")

    canvas = Canvas(jouer, width=1080, height=720, bg='black')
    canvas.pack(padx=10, pady=10)
    canvas.create_line(540,0,540,720, fill='white') 
    ball = canvas.create_oval(Pos_X, Pos_Y, Pos_X+20, Pos_Y+20, fill='white')
    raquette = canvas.create_rectangle(raqx0, raqy0, raqx1, raqy1, fill='white')
    raquette2 = canvas.create_rectangle(raq2x0, raq2y0, raq2x1, raq2y1, fill='white')

    canvas.bind_all('<s>', bas1)
    canvas.bind_all('<Down>', bas2)
    canvas.bind_all('<z>', haut1)
    canvas.bind_all('<Up>', haut2)

    TextGame = StringVar()
    LabelGame = Label(jouer, textvariable = TextGame , bg ="grey")
    TextGame.set("Joueur 1 : "+ str(score))
    LabelGame.pack(padx = 15, pady = 5)

    deplacement()
    jouer.mainloop()

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
    ButtonFermer = Button(fenetre, text ="   Fermer    ", command = fenetre.destroy)
    ButtonFermer.pack(padx = 5, pady = 5)

def pointpartie(): 
    menu.destroy()
    partie = Tk()
    partie.title("Personnalisation")
    label = Label(partie, text="Sélectionnez le nombre de points de la partie : ", bg="grey")
    label.pack()
    value = StringVar() 
    bouton1 = Radiobutton(partie, text="5 points", variable=value, value=1)
    bouton2 = Radiobutton(partie, text="10 points", variable=value, value=2)
    bouton3 = Radiobutton(partie, text="15 points", variable=value, value=3)
    bouton1.pack()
    bouton2.pack()
    bouton3.pack()
    label = Label(partie, text=" Vitesse de la balle : ", bg="grey")
    label.pack()
    value2 = StringVar() 
    bouton4 = Radiobutton(partie, text="Facile", variable=value2, value=4)
    bouton5 = Radiobutton(partie, text="Moyen", variable=value2, value=5)
    bouton6 = Radiobutton(partie, text="Difficile", variable=value2, value=6)
    bouton4.pack()
    bouton5.pack()
    bouton6.pack()
    label = Label(partie, text=" Couleur de la balle : ", bg="grey")
    label.pack()
    value3 = StringVar() 
    bouton7 = Radiobutton(partie, text="Rouge", variable=value3, value=7)
    bouton8 = Radiobutton(partie, text="Vert", variable=value3, value=8)
    bouton9 = Radiobutton(partie, text="jaune", variable=value3, value=9)
    bouton10 = Radiobutton(partie, text="violet", variable=value3, value=10)
    bouton7.pack()
    bouton8.pack()
    bouton9.pack()
    bouton10.pack()
    label = Label(partie, text=" Couleur de la raquette joueur 1 : ", bg="grey")
    label.pack()
    value4 = StringVar() 
    bouton11 = Radiobutton(partie, text="Rouge", variable=value4, value=11)
    bouton12 = Radiobutton(partie, text="Vert", variable=value4, value=12)
    bouton13 = Radiobutton(partie, text="jaune", variable=value4, value=13)
    bouton14 = Radiobutton(partie, text="violet", variable=value4, value=14)
    bouton11.pack()
    bouton12.pack()
    bouton13.pack()
    bouton14.pack()
    label = Label(partie, text=" Couleur de la raquette joueur 2 : ", bg="grey")
    label.pack()
    value5 = StringVar() 
    bouton15 = Radiobutton(partie, text="Rouge", variable=value5, value=15)
    bouton16 = Radiobutton(partie, text="Vert", variable=value5, value=16)
    bouton17 = Radiobutton(partie, text="jaune", variable=value5, value=17)
    bouton18 = Radiobutton(partie, text="violet", variable=value5, value=18)
    bouton15.pack()
    bouton16.pack()
    bouton17.pack()
    bouton18.pack()
    ButtonValider = Button(partie,text="Valider", command= jouer)
    ButtonValider.pack(padx = 10, pady = 5)


menu = Tk()
menu.title("[Pong]")
menu.geometry("260x120")
 
ButtonJouer = Button(menu, text ="   Jouer   ", command = pointpartie)
ButtonJouer.pack(padx = 5, pady = 5)
ButtonInstruction = Button(menu,text="Instruction et Commande", command= instruction)
ButtonInstruction.pack(padx = 10, pady = 5)

ButtonQuitter = Button(menu, text ="   Quitter    ", command = menu.destroy)
ButtonQuitter.pack(padx = 5, pady = 5)

menu.mainloop()