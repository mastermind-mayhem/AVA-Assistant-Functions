import os, time, playsound, urllib.parse, urllib.error, datetime
import speech_recognition as sr
from gtts import gTTS
from datetime import date
import calendar
import bs4 as bs
import urllib.request, sys, stdiomask, subprocess, webbrowser, pyperclip
from collections import Counter

def encrypt(text):
    full = ""
    alg = {
        "z": "a",
        "y": "b",
        "x": "c",
        "w": "d",
        "v": "e",
        "u": "f",
        "t": "g",
        "s": "h",
        "r": "i",
        "q": "j",
        "p": "k",
        "o": "l",
        "n": "m",
        "m": "n",
        "l": "o",
        "k": "p",
        "j": "q",
        "i": "r",
        "h": "s",
        "g": "t",
        "f": "u",
        "e": "v",
        "d": "w",
        "c": "x",
        "b": "y",
        "a": "z",
        " ": " ",
        "?": "?",
        "!": "!",
        ",": ",",
    }
    for decode in text:
        #respond(alg[decode])
        if decode not in alg:
            full += decode
        else:
            full += alg[decode]
    return full

def respond(output):
    print(output)

def login(admin):
    v = 0
    cuser = None
    cpass = None
    match = 'false'
    cuser = input('Username: ')
    cpass = stdiomask.getpass(prompt='Password: ', mask='#')
    try:
        with open(r"C:\Users\maste\OneDrive\Documents\Atom\AVA7.beta\user.txt","r")as r:
            users = r.readlines()
    except:
        print('error')
        time.sleep(60)

    for user in users:
        try:
            useru = user[user.index("}")+1:user.index("]")-1]
            useru = encrypt(useru)
            userp = user[user.index("]")+1:user.index(".")]
            userp = encrypt(userp)

        except:
            continue
        # print(userp, useru)
        if cuser == "admin":
            cpass = encrypt(cpass)
            if cpass == "znh":
                print("Admin user has been accessed")
                print('WELCOME - ADMIN')
                print("AVA, Andromeda Virtual Assistant")
                print("Version 7.8.3")
                admin = "True"
                match = 'true'
                break
            else:
                admin = "False"
        elif useru == cuser:
            match = 'true'
            time.sleep(1.5)
            if userp == cpass:
                time.sleep(1.5)
                print("logging in...")
                time.sleep(2)
                respond("WELCOME - "+cuser)
                print("AVA, Andromeda Virtual Assistant")
                print("Version 7.8.3")
                admin = "False"
                break
            else:
                respond("I'm sorry, that username and password are incorrect")
                exit()

    if match == 'false':
        respond("I'm sorry, that username and password are incorrect.")
        exit()
    # print('finished')
    return admin

def newuser():
    new = 0
    while True:
        name = input("New User Name?: ")
        pswrd = stdiomask.getpass(prompt='Password?: ', mask='#')
        name = encrypt(name)
        pswrd = encrypt(pswrd)
        if (" " in name)or(" " in pswrd):
            respond("No Spaces Please")
        else:
            break
    cpa = stdiomask.getpass(prompt='Admin Password: ', mask='#')
    cpa = encrypt(cpa)
    if cpa == "znh":
        print("Creating New User . . .")
        new = 'True'
    else:
        respond("I'm sorry you don't have permission to create a new user")
        exit()

    with open("user.txt","a")as r:
        r.writelines("}"+name+" ]"+pswrd+".\n")

def startup():
    while True:
        admin = 0
        text = input("Returning or New: ")
        if "new" in text or "New" in text:
            newuser()
            admin = login(admin)
            break
        else:
            admin = login(admin)
            break
    return admin
