import tkinter as tk
import cv2
import numpy as np

win = tk.Tk()
win.attributes('-fullscreen', True)
win.title('Door-Man')
# creat label widget
cam_start_btn = tk.Button(win, text = "Door Cam", height = 20, width = 40)
# pack it onto screen
cam_start_btn.grid(row = 1, column = 0)


win.mainloop()


#Functions -----------------------------
def close():
	win.destroy()

# def cam_toggle():


#----------------------------------------
win.protocol("WM_DELETE_WINDOW", close)