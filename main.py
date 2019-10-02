from tkinter import *
import cv2
import PIL.ImageTk,PIL.Image
from functools import partial
import threading
import imutils
import time

SET_WIDTH = 650
SET_HEIGHT = 358

window = Tk()
window.title("DRS System")

stream = cv2.VideoCapture("clip.mp4")
def play(speed):
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES , frame1+speed)
    grabbed,frame = stream.read()
    frame = imutils.resize(frame,width= SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame,anchor = "nw")
    canvas.create_text(100,30,text = "Decision Pending....",font = "lucida 16 bold",fill ="red")



def pending(decision):

    frame = cv2.cvtColor(cv2.imread("decision_pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image = frame,anchor ="nw")

    time.sleep(1.5)

    if decision == "out":
        decision_img = "out.png"
        frame = cv2.cvtColor(cv2.imread(decision_img), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor="nw")

    else:
        decision_img = "not_out.png"
        frame = cv2.cvtColor(cv2.imread(decision_img), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor="nw")






def out():
    thread= threading.Thread(target=pending , args = ("out",))
    thread.daemon = 1
    thread.start()
    print("out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("not out")

# reading Image
cv_img = cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)

# creating canvas
canvas = Canvas(window,width = SET_WIDTH,height = SET_HEIGHT)

photo = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(cv_img))
canvas.image = photo
image_on_canvas = canvas.create_image(0,0,anchor = "nw",image = photo)
canvas.pack()

# buttons to control playback
Button(window,text = "<< Previous (fast)",font = "lucida 16 bold",width = 50,command = partial(play,-25)).pack(padx = 10,pady = 10)

Button(window,text = "< Previous (slow)",font = "lucida 16 bold",width = 50,command = partial(play,-5)).pack(padx = 10,pady = 10)

Button(window,text = "Next (slow) >",font = "lucida 16 bold",width = 50,command = partial(play,2)).pack(padx = 10,pady = 10)

Button(window,text = "Next (fast) >>",font = "lucida 16 bold",width = 50,command = partial(play,25)).pack(padx = 10,pady = 10)

Button(window,text = "Give Out",font = "lucida 16 bold",width = 50,command = out).pack(padx = 10,pady = 10)

Button(window,text = "Give Not Out",font = "lucida 16 bold",width = 50,command = not_out).pack(padx = 10,pady = 10)




window.mainloop()

