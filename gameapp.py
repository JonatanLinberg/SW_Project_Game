import tkinter as tk
import urllib
from PIL import Image, ImageTk
import io
import person
import query

class MainFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.createGUI()

	def createGUI(self):
		self.config(background="#eee5dc")

		btn = tk.Button(self, text="Play Game", width=20,command=self.playGame)
		btn.place(relx=0.5, rely=0.55, anchor='c')

		btn = tk.Button(self, text="Quit Game", width=20,command=self.controller.quit)
		btn.place(relx=0.5, rely=0.6, anchor='c')

		self.loadlbl = tk.Label(self, text="Loading Game...", width=20, font=('Arial', 20))
		

	def playGame(self):
		self.isLoading(True)
		self.controller.parent.after(10, self.controller.playGame)

	def isLoading(self, bool):
		if (bool):
			self.loadlbl.place(relx=0.5, rely=0.3, anchor='c')
		else:
			self.loadlbl.place_forget()

class ResultFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.createGUI()

	def createGUI(self):

		self.result = tk.Label(self, text='Name2', relief=tk.GROOVE)
		self.result.place(relx=0.5, rely=0.4, width=200, anchor='c')

		btn = tk.Button(self, text="Game finished", width=200, command=lambda: self.controller.show_frame("MainFrame"))
		btn.place(relx=0.5, rely=0.6, anchor='c')

	def updateGame(self):
		self.result.config(text="Total Points: " + str(self.controller.getPoints()))



class GameFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.createGUI()

	def createGUI(self):
		self.config(background="#eee5dc")

		self.fig1 = tk.Label(self, relief=tk.GROOVE)
		self.fig1.place(relx=0.3, rely=0.3, height=300, width=200, anchor='c')

		self.name1 = tk.Label(self, text='Name1', relief=tk.GROOVE)
		self.name1.place(relx=0.3, rely=0.55, width=200, anchor='c')

		self.fig2 = tk.Label(self, relief=tk.GROOVE)
		self.fig2.place(relx=0.7, rely=0.3, height=300, width=200, anchor='c')

		self.name2 = tk.Label(self, text='Name2', relief=tk.GROOVE)
		self.name2.place(relx=0.7, rely=0.55, width=200, anchor='c')

		question = tk.Label(self, text='Are they alive at the same time?', bg="#eee5dc", font=('Arial', 20))
		question.place(relx=0.5, rely=0.7, width=300, anchor='c')

		btn_yes = tk.Button(self, text='YES', command=self.controller.press_yes)
		btn_yes.place(relx=0.4, rely=0.8, width=75, anchor='c')

		btn_no = tk.Button(self, text='NO', command=self.controller.press_no)
		btn_no.place(relx=0.6, rely=0.8, width=75, anchor='c')

	def updateGame(self):
		self.name1.config(text=self.controller.getCurrentNames(1))
		self.name2.config(text=self.controller.getCurrentNames(2))
		self.fig1.config(image=self.controller.getCurrentImages(1))
		self.fig2.config(image=self.controller.getCurrentImages(2))



class Game():
	def __init__(self, parent):
		self.parent = parent
		self.frames = {}

		self.createGUI()

	def createGUI(self):
		self.parent.title("GAME")
		self.parent.geometry("960x720")

		container = tk.Frame(self.parent)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		for F in (MainFrame, GameFrame, ResultFrame):
			page_name = F.__name__
			frame = F(container, self)
			self.frames[page_name] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame('MainFrame')

	def playGame(self):
		self.initGame()
		self.frames['GameFrame'].updateGame()
		self.frames['MainFrame'].isLoading(False)
		self.show_frame('GameFrame')

	def initGame(self):
		self.points = 0
		self.persons = []

		while (len(self.persons) < 20):
			persons = query.get_dbpedia_persons()
			persons = query.find_images_for(persons)

			for i in range(len(persons)):
				if (persons[i].image is not None):
					self.persons.append(persons[i])

		self.nextRound()

	def nextRound(self):
		if (len(self.persons) >= 2):
			self.currentPersons = [self.persons.pop(), self.persons.pop()]
			self.currentImages = [None, None]
		else:
			self.show_frame('MainFrame')

	def getCurrentImages(self, person):
		if (self.currentImages[person-1] is None):
			raw_data = urllib.request.urlopen(self.currentPersons[person-1].image).read()
			im = Image.open(io.BytesIO(raw_data))
			self.currentImages[person-1] = ImageTk.PhotoImage(im.resize((200, 300), Image.BILINEAR))
		return self.currentImages[person-1]

	def getCurrentNames(self, person):
		return self.currentPersons[person-1].name

	def getPoints(self):
		return self.points

	def press_yes(self):
		self.points += 1
		self.nextRound()
		self.frames['GameFrame'].updateGame()

	def press_no(self):
		self.nextRound()
		self.frames['GameFrame'].updateGame()

	def show_frame(self, frame_name):
		self.frames[frame_name].tkraise()

	def start(self):
		self.parent.mainloop()

	def quit(self):
		self.parent.quit()


game = Game(tk.Tk())
game.start()