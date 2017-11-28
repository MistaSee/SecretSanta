#!/usr/bin/python

import random
from time import sleep
from  gpiozero import Button, LED

import random
import sys
import pygame
import cups
from PIL import Image, ImageEnhance
from signal import pause


pygame.init()

names = ['alex','andrew','annemarie','caitlyn','courtney','craig','dan','e-bop','edward','emily','giustina','helen','james','kat','kated','katew','laura','lauren','louisa','lucy','lynne','magda','maria','oly','penny','pete','richard','spacedave','ben','tom','clare','janina']
lastPick= "nobody"
button1 = Button(2)
button2 = Button(3)
red=LED(4)
green=LED(17)
person = "nobody"
first_pick=False

#Define the function which picks a Secret Santa recipient.

def pick():
    global names
    global lastPick
    global person
    global first_pick
    global red
    global green
    first_pick=True
    green.on()
    random.shuffle(names)
    person=names.pop()
    lastPick = person
    sounda=pygame.mixer.Sound('/home/pi/Downloads/hohoho.wav')
    sounda.play()
    print('You got ' + person)
    print_picture()
    green.off()
    sleep(1)
    if names == []:
        green.on()
        print('All done...Happy Holidays!')
        person="santa"
        print_picture()
        green.off()
        red.off()
        sys.exit(0)

#Define the function that will add your name back to the list and give you another recipient (in case you receive yourself!)
def redo():
    global names
    global lastPick
    global person
    global first_pick
    global green
    if first_pick==True:
        green.on()
        sounda=pygame.mixer.Sound('/home/pi/Downloads/hohoho.wav')
        sounda.play()
        names.append(lastPick)
        print('Wait, not '+lastPick)
        sleep(1)
        random.shuffle(names)
        person=names.pop()
        lastPick = person
        print('Actually, you got ' +lastPick)
        print_picture()
        green.off()
        sleep(1)
    else:
        green.on()
        print("You haven't picked anyone yet!")
        print_picture()
        green.off()
        
def print_picture():
    global names
    global person
    global lastPick
    global first_pick
    conn = cups.Connection()
    printers = conn.getPrinters()
    printer_name = list(printers.keys())[0]
    cups.setUser('pi')
 
    latest_print = Image.new('RGBA', (683, 384))
    latest_print.paste(Image.open("/home/pi/SSanta/"+str(person)+".jpg").resize((683, 384)), ( 0, 0, 683, 384))
   
    output = "/home/pi/SSanta/"+str(person)+".jpg"
 
    print_id = conn.printFile(printer_name, output, "Photo Booth", {})
    while conn.getJobs().get(print_id, None):
        sleep(1)
    #unlink(output)
 

try:
    red.on()
    button1.when_pressed=pick
    button2.when_pressed=redo
    pause()

except IndexError:
    pass
    print('All Done! Happy Holidays!')
    red.off()
