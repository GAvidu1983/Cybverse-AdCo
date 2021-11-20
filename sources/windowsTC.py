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

Lrestrictions = ['Firefox','Chromium']
Lexcept = ['wikipedia.com','frischool.ch']

def WTC_capture():
    res = False
    l = shell("sudo wmctrl -l")
    for f in l.output() :
        print(f)
        out = any (Lrestriction in f for Lrestriction in Lrestrictions)
        print(out)
if __name__=="__main__":
    WTC_capture()