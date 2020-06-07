from tkinter import *
import cv2
import numpy as np

win = Tk()
win.attributes('-fullscreen', True)
win.title('Door-Man')
# creat label widget
cam_start_btn = Button(win, text = "Door Cam", height = 10, width = 40)
# pack it onto screen
cam_start_btn.pack(side=BOTTOM)


win.mainloop()


#Functions -----------------------------
def close():
	win.destroy()

# def cam_toggle():


#----------------------------------------
win.protocol("WM_DELETE_WINDOW", close)