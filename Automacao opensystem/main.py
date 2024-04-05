from PySimpleGUI import PySimpleGUI as sg
import pyautogui
from time import sleep


def criar_janela():
    sg.theme('DarkBlack')

    col1 = [
        [sg.Text('ABRIR SISTEMA HAPVIDA', font='Arial 13 bold')],
        [sg.Text('ABRIR EMAIL', font='Arial 13 bold')],
        [sg.Text('ABRIR SISTEMA SOFIA', font='Arial 13 bold')],
        [sg.Text('ABRIR WHATSAPP', font='Arial 13 bold')],
        [sg.Text('ABRIR SISTEMA ARYA', font='Arial 13 bold')],
        [sg.Text('BLOCO DE NOTAS', font='Arial 13 bold')]
    ]

    col2 = [
        [sg.Button('HAPVIDA', size=10)],
        [sg.Button('EMAIL', size=10)],
        [sg.Button('SOFIA', size=10)],
        [sg.Button('WHATSAPP', size=10)],
        [sg.Button('ARYA', size=10)],
        [sg.Button('BLOCO DE NOTAS', size=10)]
    ]

    layout = [
        [sg.Column(col1), sg.Column(col2)]
    ]

    return sg.Window('OPEN SYSTEM', layout=layout, finalize=True, resizable=True)

criar_janela()
while True:
    window, events, values = sg.read_all_windows()
    if events == sg.WINDOW_CLOSED:
        window.close()
        break
    
    if events == 'HAPVIDA':
        ...
    
    if events == 'EMAIL':
        pyautogui.hotkey('win', 'r')
        pyautogui.write('opera')
        pyautogui.hotkey('enter')
        sleep(1)
        pyautogui.write('https://login.live.com/')
        pyautogui.hotkey('enter')
    
    if events == 'SOFIA':
        pyautogui.hotkey('win', 'r')
        pyautogui.write('opera')
        pyautogui.hotkey('enter')
        sleep(1)
        pyautogui.write('sofia.med.br')
        pyautogui.hotkey('enter')
    
    if events == 'WHATSAPP':
        pyautogui.hotkey('winleft', 'r')
        pyautogui.write('opera')
        pyautogui.hotkey('enter')
        sleep(5)
        # pyautogui.hotkey('f6')
        pyautogui.write('web.whatsapp.com')
        pyautogui.hotkey('enter')
    
    if events == 'ARYA':
        ...
    
    if events == 'BLOCO DE NOTAS':
        pyautogui.hotkey('winleft', 'r')
        # sleep(1)
        pyautogui.write('notepad')
        # sleep(1)
        pyautogui.hotkey('enter')
