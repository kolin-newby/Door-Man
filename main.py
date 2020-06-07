from tkinter import *
import cv2
import numpy as np

win = Tk()
win.attributes('-fullscreen', True)
win.title('Door-Man App')

cam_toggle_btn = Button(win, text = 'Door Cam', height = 5, width = 20)
cam_toggle_btn.pack(side = BOTTOM, expand = YES)

win.mainloop()

def doorFeed():
	cap = cv2.VideoCapture(0)
	while(cap.isOpened()):
		ret, frame = cap.read()

		cv2.imshow('output', frame)
		if(cv2.waitKey(1) & 0xFF == ord('q')):
			break

	cap.release()
	cv2.destroyAllWindows()

def close():
	win.destroy()



feed = Frame(win)


win.protocol("WM_DELETE_WINDOW", close)

