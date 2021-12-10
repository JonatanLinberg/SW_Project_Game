import tkinter as tk
import person
import query

class MainFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.createGUI()

	def createGUI(self):
		self.config(background="#eee5dc")

		btn = tk.Button(self, text="Play Game", width=20,command=lambda: self.controller.show_frame('GameFrame'))
		btn.place(relx=0.5, rely=0.55, anchor='c')

		btn = tk.Button(self, text="Quit Game", width=20,command=self.controller.quit)
		btn.place(relx=0.5, rely=0.6, anchor='c')



class GameFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.createGUI()

	def createGUI(self):
		self.config(background="#eee5dc")

		fig1 = tk.Label(self, text='Fig1', relief=tk.GROOVE)
		fig1.place(relx=0.3, rely=0.3, relh=0.4, width=200, anchor='c')

		nmae1 = tk.Label(self, text='Name1', relief=tk.GROOVE)
		nmae1.place(relx=0.3, rely=0.55, width=200, anchor='c')

		fig2 = tk.Label(self, text='Fig2', relief=tk.GROOVE)
		fig2.place(relx=0.7, rely=0.3, relh=0.4, width=200, anchor='c')

		name2 = tk.Label(self, text='Name2', relief=tk.GROOVE)
		name2.place(relx=0.7, rely=0.55, width=200, anchor='c')

		question = tk.Label(self, text = 'Are they alive at the same time?', bg="#eee5dc", font=('Arial', 20))
		question.place(relx=0.5, rely=0.7, width=300, anchor='c')

		btn_yes = tk.Button(self, text='YES', command=self.controller.press_yes)
		btn_yes.place(relx=0.4, rely=0.8, width=75, anchor='c')

		btn_no = tk.Button(self, text='NO', command=self.controller.press_no)
		btn_no.place(relx=0.6, rely=0.8, width=75, anchor='c')




class Game():
	def __init__(self, parent):
		self.parent = parent
		self.frames = {}

		self.initGame()
		self.createGUI()

	def createGUI(self):
		self.parent.title("GAME")
		self.parent.geometry("960x720")

		container = tk.Frame(self.parent)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		for F in (MainFrame, GameFrame):
			page_name = F.__name__
			frame = F(container, self)
			self.frames[page_name] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame('MainFrame')

	def getCurrentImages(self):
		pass

	def getCurrentNames(self):
		pass

	def getPoints(self):
		pass

	def press_yes(self):
		pass

	def press_no(self):
		pass

	def show_frame(self, frame_name):
		self.frames[frame_name].tkraise()

	def start(self):
		self.parent.mainloop()

	def quit(self):
		self.parent.quit()


game = Game(tk.Tk())
game.start()