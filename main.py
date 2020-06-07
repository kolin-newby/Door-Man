from tkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
import numpy as np

class doorFeed:
	panel = None
	win = None
	cam = None

	def __init__(self):
		self.win = Tk()
		self.win.title('Door-Man')
		self.win.attributes('-fullscreen', True)

		self.panel = Label(self.win)
		self.panel.pack(side = BOTTOM, extend = YES)

		self.cam = cv2.VideoCapture(0)
		self.camera1()
		self.win.mainloop()

	def Camera1(self):
		_,frame = self.camera.read()
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		frame = Image.fromarray(frame)
		frame = ImageTk.PhotoImage(frame)
		self.panel.configure(image = frame)
		self.panel.image = frame
		self.panel.After(1, self.Camera)


if __name__ == '__main__':
	objVideo = doorFeed()