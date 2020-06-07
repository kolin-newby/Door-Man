import tkinter as tk
import cv2
import numpy as np

win = tk.Tk()
win.title('Door-Man')
# creat label widget
cam_start_btn = tk.Button(win, text = "Start Camera")
# pack it onto screen
cam_start_btn.place(relx = 0.5, rely = 0.5, anchor=CENTER)


win.mainloop()


#Functions -----------------------------
def close():
	win.destroy()

def cam_toggle():


#----------------------------------------
win.protocol("WM_DELETE_WINDOW", close)