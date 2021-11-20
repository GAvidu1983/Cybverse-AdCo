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

Windows Titlebar Check Tool

"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from shell import shell
import time

from PIL import ImageGrab
import numpy as np
from datetime import datetime
import cv2
import pytesseract

class Global :
    pass

G=Global()
G.tmp = "/tmp/.wdCybVAdCo/"

Lrestrictions = ['Firefox','Chromium']
Lexceptions = ['wikipedia','frischool.ch']




def WTC_capture(G=G):
    res = False
    l = shell("sudo wmctrl -l")
    for f in l.output() :
        print(f)
        test = any (Lrestriction in f for Lrestriction in Lrestrictions)
        
        if test :
            print('TEST1 positif')
            img = ScreenCapture(G)
            test2 = tesseranalysis(img)
            if test2 :
                test = not test
            else :
                test = test
                for i in Lrestrictions :
                    shell("sudo wmctrl -c" + i)
        print('Resultat final: '+str(test))
    return test

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
    return frame


def tesseranalysis(img) :
    custom_config = r'--oem 3 --psm 6'
    stri = pytesseract.image_to_string(img, config=custom_config)
    #print('-------\n')
    #print(stri)
    #print('-------\n')
    test2 = any(Lexcept in stri.lower() for Lexcept in Lexceptions)
    #print('test2'+str(test2))
    if test2 :
        print('OK')
        return True
    else :
        return False



if __name__=="__main__":
    
    shell('sudo rm -r'+ G.tmp)
    shell('mkdir ' + G.tmp)
    
    WTC_capture()