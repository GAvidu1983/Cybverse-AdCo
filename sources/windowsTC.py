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
#import pyscreenshot as ImageGrab
import numpy as np
from datetime import datetime
import cv2
import pytesseract

class WTC :
    def __init__(self):

        self.tmp = "/tmp/.wdCybVAdCo/"
        
        self.local = "/home/pi/.CybVAdCo/"

        self.Lrestrictions = ['Firefox','Chromium']
        self.Lexceptions = ['wikipedia','frischool','gomath','duolingo','scratch',
                            'raspberry','ultimaker','linux','junior','studentzone','cambridge','office.com','tutodraw',
                            'je progresse en dessin','heliox','les découvreurs','thingiverse','turtle',
                            'framboise314','vikidia','codeclubworld','il était une fois','c\'est pas sorcier',
                            'Davi Draw', 'DaviDraw','educlasse','funweb.epfl','studio.youtube','Cybverse-AdCo','Cybverse',
                            ]
        
        self.count = 0
        self.limit1 = 50
        self.limit2 = 20
        
        shell('mkdir ' + self.local)
        
        now = datetime.now()
        self.day = now.strftime("%Y%m%d")
        
        try :
            f = open(self.local + self.day + ".txt",'r')
            self.count = int(f.read())
            f.close()
        except :
            pass




    def WTC_capture(self):
        res = False
        l = shell("sudo wmctrl -l")
        return l

    def ScreenCapture(self):
        img = ImageGrab.grab(bbox=(100, 90, 1400, 150)) #x, y, w, h  zone 1 navigator adresse html
        img2 = ImageGrab.grab(bbox=(100, 1000, 1400, 1080)) #x, y, w, h # zone 2 Youtbeur name
        img_np = np.array(img)
        print(img_np.shape)
        img_np2 = np.array(img2)
        print(img_np2.shape)
        imgtot = cv2.vconcat([img_np,img_np2])
        #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        frame = cv2.cvtColor(imgtot, cv2.COLOR_BGR2GRAY)
        cv2.Canny(frame, 100, 200)
        #now = datetime.now()
        #date_time = now.strftime("%Y%m%d-%H%M%S")
        f = self.tmp + "currentscreenshot" + '.png'
        cv2.imwrite(f,frame)
        print(f)
        return frame


    def tesseranalysis(self,img) :
        custom_config = r'--oem 3 --psm 6'
        stri = pytesseract.image_to_string(img, config=custom_config)
        #print('-------\n')
        #print(stri)
        #print('-------\n')
        test2 = any(Lexcept in stri.lower() for Lexcept in self.Lexceptions)
        #print('test2'+str(test2))
        if test2 :
            print('OK')
            return True
        else :
            return False
    
    
    def WTC_test(self):
        #placement of restricted windows in good position
        shell('wmctrl -r "Firefox" -b add,maximized_vert,maximized_horz')
        shell('wmctrl -r "chromium" -b add,maximized_vert,maximized_horz')
        time.sleep(0.5)
            
        l = self.WTC_capture()
        for f in l.output() :
            print(f)
            test = any (Lrestriction in f for Lrestriction in self.Lrestrictions)
            
            if test :
                print('TEST1 positif')
                img = self.ScreenCapture()
                test2 = self.tesseranalysis(img)
                if test2 :
                    test = not test
                else :
                    test = test
                    self.count += 1
                    print('counter : ' + str(self.count))
                    
                    f = open(self.local + self.day + ".txt",'w')
                    f.write(str(self.count))
                    f.close()
                    
                    if self.count >= self.limit1 :
                        for i in self.Lrestrictions :
                            shell("sudo wmctrl -c" + i)
            print('Resultat final: '+str(test))
        return test



if __name__=="__main__":
    
    WTCinstance = WTC()
    
    shell('sudo rm -r'+ WTCinstance.tmp)
    shell('mkdir ' + WTCinstance.tmp)
    
    
    
    WTCinstance.WTC_test()