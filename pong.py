from tkinter import *
import random
import time

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

class Ball:
	def __init__(self,canvas,raquette2,raquette,color):
		self.canvas = canvas
		self.raquette = raquette
		self.raquette2 = raquette2
		self.score_j1 = 0
		self.score_j2 = 0
		self.point_j2 = 0
		self.point_j1 = 0
		self.ball = self.canvas.create_oval(10,10,35,35,fill = color)
		self.canvas.move(self.ball,327,220)
		self.x = random.choice([-2.5,2.5])
		self.y = -2.5
		
	def checkwin5(self):
		if self.score_j1 == 5:
			time.sleep(10)
			self.x = 0
			self.y = 0
		if self.score_j2 == 5:
			time.sleep(10)

	def checkwin10(self):
		if self.score_j1 == 10:
			time.sleep(10)
			self.x = 0
			self.y = 0
		if self.score_j2 == 10:
			time.sleep(10)

	def checkwin15(self):
		if self.score_j1 == 15:
			time.sleep(10)
			self.x = 0
			self.y = 0
		if self.score_j2 == 15:
			time.sleep(10)

	
	def update(self,val):
		self.canvas.delete(self.point_j1)
		self.point_j1 = self.canvas.create_text(170,50,font=('',40),text=str(val),fill='white')
		

	def update1(self,val):
		self.canvas.delete(self.point_j2)
		self.point_j2 = self.canvas.create_text(550,50,font=('',40),text=str(val),fill='white')		
		
	def collision(self,pos):
		raq_pos = self.canvas.coords(self.raquette.raquet)
		if pos[2] >= raq_pos[0] and pos[0] <= raq_pos[2]:
			if pos[3] >= raq_pos[1] and pos[3] <= raq_pos[3]:
				return True	
			return False
			
	def collision2(self,pos):
		raq2_pos = self.canvas.coords(self.raquette2.raquet)
		if pos[2] >= raq2_pos[0] and pos[0] <= raq2_pos[2]:
			if pos[3] >= raq2_pos[1] and pos[3] <= raq2_pos[3]:
				return True	
			return False
			
	def draw(self):
		self.canvas.move(self.ball,self.x,self.y)
		ball_pos = self.canvas.coords(self.ball)
		if ball_pos[1] <= 0:
			self.y = 4
		if ball_pos[3] >= 500:
			self.y =-4
		if ball_pos[0] <= 0:
			self.score_j2 += 1
			self.canvas.move(self.ball,327,220)
			self.x = 4
			self.update1(self.score_j2)
		if ball_pos[2] >=700:
			self.score_j1 += 1
			self.canvas.move(self.ball,-327,-220)
			self.x = -4
			self.update(self.score_j1)
		if self.collision(ball_pos):
			self.x = 4
		if self.collision2(ball_pos):
			self.x = -4
		
class raquette:
	def __init__(self,canvas,color):
		self.canvas = canvas
		self.raquet = self.canvas.create_rectangle(0,200,20,310,fill=color)
		self.y = 0
		self.canvas.bind_all('z',self.haut)
		self.canvas.bind_all('s',self.bas)	
		
	def haut(self,event):
		self.y = -5
		
	def bas(self,event):
		self.y = 5
	
	def draw(self):
		self.canvas.move(self.raquet,0,self.y)
		pos = self.canvas.coords(self.raquet)
		if pos[1] <= 0:
			self.y = 0
		if pos[3] >= 500:
			self.y = -0

class raquette2:
	def __init__(self,canvas,color):
		self.canvas = canvas
		self.raquet = self.canvas.create_rectangle(680,200,710,310,fill=color)
		self.y = 0
		self.canvas.bind_all('<Up>',self.haut)
		self.canvas.bind_all('<Down>',self.bas)	
		
	def haut(self,event):
		self.y = -5
		
	def bas(self,event):
		self.y = 5
	
	def draw(self):
		self.canvas.move(self.raquet,0,self.y)
		pos = self.canvas.coords(self.raquet)
		if pos[1] <= 0:
			self.y = 0
		if pos[3] >= 500:
			self.y = 0


def menu2():
	menu.destroy()
	point = Tk ()
	point.title('Points')
	label = Label(point, text=" Sélectionnez le nombre de points : ", bg="grey")
	label.pack()
	ButtonJouer1 = Button(point, text ="   5 points   ", command = couleur5)
	ButtonJouer1.pack(padx = 5, pady = 5)
	ButtonJouer2 = Button(point, text ="   10 points   ", command = couleur10)
	ButtonJouer2.pack(padx = 5, pady = 5)
	ButtonJouer3 = Button(point, text ="   15 points   ", command = couleur15)
	ButtonJouer3.pack(padx = 5, pady = 5)

def jouerblanche():
	jouer = Tk()
	jouer.title('Pong')
	jouer.resizable(0,0)
	canvas = Canvas(jouer,width=700,height=500, bg='black')
	canvas.pack()
	jouer.update()
	canvas.create_line(350,0,350,500,fill='white')

	paddle = raquette(canvas,'white')
	paddle1 = raquette2(canvas,'white')		
	ball = Ball(canvas,paddle1,paddle,'white')
		
	while 1:
		ball.draw()
		paddle.draw()
		paddle1.draw()
		ball.checkwin5()
		jouer.update_idletasks()
		jouer.update()
		time.sleep(0.01)
	quit()

def jouerrouge():
	jouer = Tk()
	jouer.title('Pong')
	jouer.resizable(0,0)
	canvas = Canvas(jouer,width=700,height=500, bg='black')
	canvas.pack()
	jouer.update()
	canvas.create_line(350,0,350,500,fill='white')

	paddle = raquette(canvas,'white')
	paddle1 = raquette2(canvas,'white')		
	ball = Ball(canvas,paddle1,paddle,'red')
		
	while 1:
		ball.draw()
		paddle.draw()
		paddle1.draw()
		ball.checkwin5()
		jouer.update_idletasks()
		jouer.update()
		time.sleep(0.01)
	quit()

def jouerverte():
	jouer = Tk()
	jouer.title('Pong')
	jouer.resizable(0,0)
	canvas = Canvas(jouer,width=700,height=500, bg='black')
	canvas.pack()
	jouer.update()
	canvas.create_line(350,0,350,500,fill='white')

	paddle = raquette(canvas,'white')
	paddle1 = raquette2(canvas,'white')		
	ball = Ball(canvas,paddle1,paddle,'green')
		
	while 1:
		ball.draw()
		paddle.draw()
		paddle1.draw()
		ball.checkwin5()
		jouer.update_idletasks()
		jouer.update()
		time.sleep(0.01)
	quit()

def couleur5():
	couleur = Tk ()
	couleur.title('Couleur')
	label = Label(couleur, text=" Sélectionnez la couleur de la balle : ", bg="grey")
	label.pack()
	ButtonJouer1 = Button(couleur, text ="   Blanche   ", command = jouerblanche)
	ButtonJouer1.pack(padx = 5, pady = 5)
	ButtonJouer2 = Button(couleur, text ="   Verte   ", command = jouerverte)
	ButtonJouer2.pack(padx = 5, pady = 5)
	ButtonJouer3 = Button(couleur, text ="   Rouge   ", command = jouerrouge)
	ButtonJouer3.pack(padx = 5, pady = 5)

def couleur10():
	couleur = Tk ()
	couleur.title('Couleur')
	label = Label(couleur, text=" Sélectionnez la couleur de la balle : ", bg="grey")
	label.pack()
	ButtonJouer1 = Button(couleur, text ="   Blanche   ", command = jouer2blanche)
	ButtonJouer1.pack(padx = 5, pady = 5)
	ButtonJouer2 = Button(couleur, text ="   Verte   ", command = jouer2verte)
	ButtonJouer2.pack(padx = 5, pady = 5)
	ButtonJouer3 = Button(couleur, text ="   Rouge   ", command = jouer2rouge)
	ButtonJouer3.pack(padx = 5, pady = 5)

def couleur15():
	couleur = Tk ()
	couleur.title('Couleur')
	label = Label(couleur, text=" Sélectionnez la couleur de la balle : ", bg="grey")
	label.pack()
	ButtonJouer1 = Button(couleur, text ="   Blanche   ", command = jouer3blanche)
	ButtonJouer1.pack(padx = 5, pady = 5)
	ButtonJouer2 = Button(couleur, text ="   Verte   ", command = jouer3verte)
	ButtonJouer2.pack(padx = 5, pady = 5)
	ButtonJouer3 = Button(couleur, text ="   Rouge   ", command = jouer3rouge)
	ButtonJouer3.pack(padx = 5, pady = 5)


def jouer2blanche():
	jouer = Tk()
	jouer.title('Pong')
	jouer.resizable(0,0)
	canvas = Canvas(jouer,width=700,height=500, bg='black')
	canvas.pack()
	jouer.update()
	canvas.create_line(350,0,350,500,fill='white')

	paddle = raquette(canvas,'white')
	paddle1 = raquette2(canvas,'white')		
	ball = Ball(canvas,paddle1,paddle,'white')
		
	while 1:
		ball.draw()
		paddle.draw()
		paddle1.draw()
		ball.checkwin10()
		jouer.update_idletasks()
		jouer.update()
		time.sleep(0.01)
	quit()

def jouer2verte():
	jouer = Tk()
	jouer.title('Pong')
	jouer.resizable(0,0)
	canvas = Canvas(jouer,width=700,height=500, bg='black')
	canvas.pack()
	jouer.update()
	canvas.create_line(350,0,350,500,fill='white')

	paddle = raquette(canvas,'white')
	paddle1 = raquette2(canvas,'white')		
	ball = Ball(canvas,paddle1,paddle,'green')
		
	while 1:
		ball.draw()
		paddle.draw()
		paddle1.draw()
		ball.checkwin10()
		jouer.update_idletasks()
		jouer.update()
		time.sleep(0.01)
	quit()

def jouer2rouge():
	jouer = Tk()
	jouer.title('Pong')
	jouer.resizable(0,0)
	canvas = Canvas(jouer,width=700,height=500, bg='black')
	canvas.pack()
	jouer.update()
	canvas.create_line(350,0,350,500,fill='white')

	paddle = raquette(canvas,'white')
	paddle1 = raquette2(canvas,'white')		
	ball = Ball(canvas,paddle1,paddle,'red')
		
	while 1:
		ball.draw()
		paddle.draw()
		paddle1.draw()
		ball.checkwin10()
		jouer.update_idletasks()
		jouer.update()
		time.sleep(0.01)
	quit()

def jouer3blanche():
	jouer = Tk()
	jouer.title('Pong')
	jouer.resizable(0,0)
	canvas = Canvas(jouer,width=700,height=500, bg='black')
	canvas.pack()
	jouer.update()
	canvas.create_line(350,0,350,500,fill='white')

	paddle = raquette(canvas,'white')
	paddle1 = raquette2(canvas,'white')		
	ball = Ball(canvas,paddle1,paddle,'white')
		
	while 1:
		ball.draw()
		paddle.draw()
		paddle1.draw()
		ball.checkwin15()
		jouer.update_idletasks()
		jouer.update()
		time.sleep(0.01)
	quit()	

def jouer3rouge():
	jouer = Tk()
	jouer.title('Pong')
	jouer.resizable(0,0)
	canvas = Canvas(jouer,width=700,height=500, bg='black')
	canvas.pack()
	jouer.update()
	canvas.create_line(350,0,350,500,fill='white')

	paddle = raquette(canvas,'white')
	paddle1 = raquette2(canvas,'white')		
	ball = Ball(canvas,paddle1,paddle,'red')
		
	while 1:
		ball.draw()
		paddle.draw()
		paddle1.draw()
		ball.checkwin15()
		jouer.update_idletasks()
		jouer.update()
		time.sleep(0.01)
	quit()	

def jouer3verte():
	jouer = Tk()
	jouer.title('Pong')
	jouer.resizable(0,0)
	canvas = Canvas(jouer,width=700,height=500, bg='black')
	canvas.pack()
	jouer.update()
	canvas.create_line(350,0,350,500,fill='white')

	paddle = raquette(canvas,'white')
	paddle1 = raquette2(canvas,'white')		
	ball = Ball(canvas,paddle1,paddle,'green')
		
	while 1:
		ball.draw()
		paddle.draw()
		paddle1.draw()
		ball.checkwin15()
		jouer.update_idletasks()
		jouer.update()
		time.sleep(0.01)
	quit()	

menu = Tk()
menu.title("[Pong]")
menu.geometry("260x120")

ButtonJouer = Button(menu, text ="   Jouer   ", command = menu2)
ButtonJouer.pack(padx = 5, pady = 5)
ButtonInstruction = Button(menu,text="Instruction et Commande", command= instruction)
ButtonInstruction.pack(padx = 10, pady = 5)

ButtonQuitter = Button(menu, text ="   Quitter    ", command = menu.destroy)
ButtonQuitter.pack(padx = 5, pady = 5)

menu.mainloop()