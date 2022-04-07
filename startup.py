import os, time, playsound, urllib.parse, urllib.error, datetime
import speech_recognition as sr
from gtts import gTTS
from datetime import date
import calendar
import bs4 as bs
import urllib.request, sys, stdiomask, subprocess, webbrowser, pyperclip
from collections import Counter

from start import startup
while True:
    admin = startup()
    # print(admin)
    if admin == 0:
        continue
    else:
        break
subprocess.run('python main.py', shell=True)
