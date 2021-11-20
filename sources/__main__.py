#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Alain David Geiser 
# Created Date: 19/11/2021
# version ='0.1'
# ---------------------------------------------------------------------------
""" Cybverse-AdCo is a little tool to help kids to improve the quality
of their activities passed behind the computer. The main Objective is to
let a given time of free surfing and an unlimited access to excellent
ressources.

MAIN Program

"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from PIL import ImageGrab
import numpy as np
from datetime import datetime
import cv2
import pytesseract
from shell import shell
import time
from threading import Timer
import PySimpleGUI as sg

#
# Classes Declarations
#

class Global :
    pass

G=Global()

G.running = True
G.wtrig = False

G.tmp = "/tmp/.wdCybVAdCo/"

shell('sudo rm -r'+ G.tmp)
shell('mkdir ' + G.tmp)


# ---------------------------------------------------------------------------
# Background Function
# ---------------------------------------------------------------------------
def ScreenCapture(G=G):
    img = ImageGrab.grab(bbox=(0, 0, 1400, 450)) #x, y, w, h
    img_np = np.array(img)
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.Canny(frame, 100, 200)
    now = datetime.now()
    date_time = now.strftime("%Y%m%d-%H%M%S")
    f = G.tmp + date_time + '.png'
    cv2.imwrite(f,frame)
    print(f)



class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def dummyfn(msg="foo"):
    print(msg)

timer = RepeatTimer(2, ScreenCapture)
timer.start()
#time.sleep(8)
#timer.cancel()
#print("END of Capture")


# ---------------------------------------------------------------------------
# GUI window
# ---------------------------------------------------------------------------   

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [[sg.Text('Persistent window')],      
          [sg.Input(key='-IN-')],      
          [sg.Button('Read'), sg.Exit()]]      

window = sg.Window('Window that stays open', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      

window.close()
timer.cancel()
print("END of Capture")