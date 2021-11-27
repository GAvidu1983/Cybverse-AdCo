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
from shell import shell
import time
from threading import Timer
import PySimpleGUI as sg
import os

import windowsTC as WTC

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
# Setting window
# ---------------------------------------------------------------------------
def settingswindow() :
    sg.theme('DarkAmber')    # Keep things interesting for your users

    layout = [[sg.Text('Setting')],
              [sg.Button('Update')],
              [sg.Button('Liste sites',key='sites')],
              [sg.Input(key='-IN-'),sg.Button('++ :-)')],
              ]#,
             

    window = sg.Window('CyberSpace - AdCo', layout,location = (500,0),grab_anywhere=True,size=(450,200))      

    while True:                             # The Event Loop
        event, values = window.read() 
        print(event, values)       
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        
        if event == 'sites' :
            os.system('chromium-browser /home/pi/Cybverse-AdCo/cybverse-AdCo.html &')

    window.close()






# ---------------------------------------------------------------------------
# Background Function
# ---------------------------------------------------------------------------
#import windowsTC as WTC


class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def dummyfn(msg="foo"):
    print(msg)
    
    
WTCinstance = WTC.WTC()
   
timer = RepeatTimer(60, WTCinstance.WTC_test)
timer.start()
#time.sleep(8)
#timer.cancel()
#print("END of Capture")

# ---------------------------------------------------------------------------
# GUI window
# ---------------------------------------------------------------------------   

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [[sg.Text('Internet temps libre')],      
          [sg.ProgressBar(WTCinstance.limit1, orientation='h', size=(20,20), key='-PROG-'),sg.Button('...',key='settings')]]#,
          #[sg.Text('Internet temps intelligent')],      
          #[sg.ProgressBar(WTCinstance.limit2, orientation='h', size=(20,20), key='-PROG2-')]]      

window = sg.Window('CyberSpace - AdCo', layout,location = (500,0),grab_anywhere=True,disable_close=True)      

while True:                             # The Event Loop
    event, values = window.read(timeout = 100) 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event == 'settings':
        settingswindow()
        
    
    window['-PROG-'].update(WTCinstance.count)
    #window['-PROG2-'].update(WTCinstance.count)

window.close()
timer.cancel()
print("END of Capture")