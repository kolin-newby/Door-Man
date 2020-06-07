import tkinter as tk
import cv2
import numpy as np

win = tk.Tk()
# creat label widget
myLabel = tk.Label(win, text = "The Door-Man Cam!")
# pack it onto screen
myLabel.place(relx = 0.5, rely = 0.5)


win.mainloop()


#Functions
def close():
	win.destroy()


win.protocol("WM_DELETE_WINDOW", close)