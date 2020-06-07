import tkinter as tk
import cv2
import numpy as np

win = tk.Tk()
win.title('Door-Man')
# creat label widget
myLabel = tk.Label(win, text = "The Door-Man Cam!")
# pack it onto screen
myLabel.place(relx = 0, rely = 0.5)


win.mainloop()


#Functions -----------------------------
def close():
	win.destroy()



#----------------------------------------
win.protocol("WM_DELETE_WINDOW", close)