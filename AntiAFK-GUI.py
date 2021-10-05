### IMPORTS ###

import PySimpleGUI as sg
import sys
import subprocess
import os
import requests
from time import sleep as sl
from PySimpleGUI.PySimpleGUI import BUTTON_TYPE_READ_FORM, Window
from pyautogui import press, typewrite, hotkey
from time import sleep
from random import randint, randbytes
### DEFINITIONS ###
secs = 0
mins = 0 
hours = 0
minconst = 1
secconst = 0

def MESSAGE(IGN, MSG):
    press('enter')
    typewrite("/msg " + str(IGN) + " I have been afk for " + str(hours) + " hours, and " + str(mins) + " minutes, and " + str(secs) + " seconds.")
    press('enter')
    press('enter')
    if str(MSG) == str("") or str(MSG) == 'Leave blank for default.':
        typewrite('> I have been AFK for ' + str(hours) + ' hours and ' + str(mins) + ' minutes, and ' + str(secs) + ' seconds. ' + str(randbytes(15)))
    else:
        typewrite("> " + str(MSG) + " " + str(randbytes(15)))
    press('enter')
    print('Sent a message in chat.')

DefIGN = "e.g. PopBob"
### LAYOUTS ###
sg.change_look_and_feel('DarkGray')
layoutInputs = [
    [sg.Text('Please enter your username and message to send in chat. ')],
    [sg.Text('This is my first real project, so please give criticism on')],
    [sg.Text('my GitHub: github.com/Tytanium13/TysAntiAFK')],
    [sg.Text(' ')],
    [sg.Text('IGN:', size=(15, 1)), sg.InputText(DefIGN,tooltip='The username of the player to send a /MSG to.')],
    [sg.Text('Chat message*:', size =(15, 1)), sg.InputText("Leave blank for default.",tooltip='Message to send in chat (Leave blank for default).')],
        
    [sg.Submit('Run', tooltip='Run the script.'), sg.Cancel('Quit', tooltip='Kills the script and closes the window.')],
]
layoutInputError = [
    [sg.Text('Please enter your username and message to send in chat. ')],
    [sg.Text('This is my first real project, so please give criticism on')],
    [sg.Text('my GitHub: github.com/Tytanium13/TysAntiAFK')],
    [sg.Text('Error: Please enter a valid username! ')],
    [sg.Text('IGN:', size=(15, 1)), sg.InputText(DefIGN,tooltip='The username of the player to send a /MSG to.')],
    [sg.Text('Chat message*:', size =(15, 1)), sg.InputText("Leave blank for default.",tooltip='Message to send in chat (Leave blank for default).')],
        
    [sg.Submit('Run', tooltip='Run the script.'), sg.Cancel('Quit', tooltip='Kills the script and closes the window.')],
]

layoutOutputs = [
    [
        sg.Button("Quit", tooltip='Kills the script and closes the window.'),
    ],
]

### CREATING THE WINDOW AND FUNCTIONS ###

window = sg.Window("Ty's AntiAFK", layoutInputs, size=(500,210))
x = 0
while True:
    if x == 0:
        event, values = window.read()
        if event == "Run":
            event, values = window.read()
            IGN = values[0]
            MSG = values[1]

            window.close()
            window = sg.Window("RUNNING | Ty's AntiAFK", layoutOutputs, size=(200,100))
            print('IGN: ' + str(IGN))  
            print('Chat MSG: ' + str(MSG))
            x = 1

    if x == 1:         
    # Basic MSG.

        secs += 1
        if secs > 59:
            secs = 0
            mins += 1
        if mins > 59:
            mins = 0
            hours += 1


    # Printing in the terminal
        if hours < 10 and mins < 10 and secs < 10:
            print('AFK for 0' + str(hours) + ":0" + str(mins) + ".0" + str(secs))
        elif hours >= 10 and mins < 10 and secs < 10:
            print('AFK for ' + str(hours) + ":0" + str(mins) + ".0" + str(secs))
        elif hours >= 10 and mins >= 10 and secs < 10:
            print('AFK for ' + str(hours) + ":" + str(mins) + ".0" + str(secs))
        elif hours >= 10 and mins >= 10 and secs >= 10:
            print('AFK for ' + str(hours) + ":" + str(mins) + "." + str(secs))
        elif hours < 10 and mins >= 10 and secs >= 10:
            print('AFK for 0' + str(hours) + ":" + str(mins) + "." + str(secs))
        elif hours < 10 and mins >= 10 and secs < 10:
            print('AFK for 0' + str(hours) + ":" + str(mins) + ".0" + str(secs))
        elif hours < 10 and mins < 10 and secs >= 10:
            print('AFK for 0' + str(hours) + ":0" + str(mins) + "." + str(secs))


    # Sending the messages
        sleep(1)
        
        if mins == minconst + 5 and secs == secconst:
            MESSAGE(IGN, MSG)
            minconst = mins
            secconst = randint(0,59)
            secs += 1

        
    if event == "Quit" or event == sg.WIN_CLOSED:
        window.close()
        exit(0)
    
