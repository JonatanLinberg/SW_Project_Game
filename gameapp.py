import tkinter as tk

class MainFrame(tk.Frame):
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		self.createGUI()

	def createGUI(self):
		self.config(background="#4477bb")

		btn = tk.Button(self, text="Play Game", width=20,command=lambda: self.controller.show_frame('GameFrame'))
		btn.place(relx=0.5, rely=0.5, anchor='c')

		btn = tk.Button(self, text="Quit Game", width=20,command=self.controller.quit)
		btn.place(relx=0.5, rely=0.5, anchor='c')


class GameFrame(tk.Frame):
	def __init__(self, parent, controller):
		self.controller = controller
		tk.Frame.__init__(self, parent)
		self.createGUI()

	def createGUI(self):
		pass



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

		for F in (MainFrame, GameFrame):
			page_name = F.__name__
			frame = F(container, self)
			self.frames[page_name] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame('MainFrame')

	def show_frame(self, frame_name):
		self.frames[frame_name].tkraise()

	def start(self):
		self.parent.mainloop()

	def quit(self):
		self.parent.quit()


game = Game(tk.Tk())
game.start()