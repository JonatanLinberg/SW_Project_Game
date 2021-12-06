import tkinter as tk

class Game():
	def __init__(self, parent):
		self.parent = parent
		self.frame = tk.Frame(parent)

	def start(self):
		self.parent.mainloop()

game = Game(tk.Tk())
game.start()