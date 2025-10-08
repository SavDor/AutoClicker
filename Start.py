import os
import sys
import colorama
from colorama import Fore
from threading import Thread
from pynput import keyboard
import pyautogui
import time
import subprocess
import ctypes

subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)

colorama.init(True)

def screen_size():
    size = pyautogui.size()
    if lang == "rus":
        pr = "Разрешение экрана: X=" + str(size[0]) + " Y=" + str(size[1])
    else:
        pr = "Screen resolution: X=" + str(size[0]) + " Y=" + str(size[1])
    return pr

with open("data/saveonekey.txt","r") as key1:
    keystartstop = key1.read()

with open("data/savetwokey.txt","r") as key2:
    keystop = key2.read()

with open("data/savetime.txt","r") as timesave:
    timer = float(timesave.read())

with open("data/savethreekey.txt", 'r') as key3:
    keylock = key3.read()

with open("data/savefourkey.txt","r") as key4:
    keystartstoplock = key4.read()

with open("data/savebutmo.txt","r") as butmo:
    button_mous = butmo.read()

with open("data/savelang.txt","r") as langu:
    lang = langu.read()

with open("data/savefivekey.txt","r") as key5:
    keyhideshowconsole = key5.read()

mouse_position = {"x":"000","y":"000"}

stop = 1
console = 1

def clear():
    os.system('cls')

kart = '''                   $$_By Sav_Dor_$$
                  $___$________$___$
                  $_____$$$$$$_____$
                  $____sss___sss____$
                  $____іі_____іі_____$
                 $_______$$$________$
     $$$$$$$$_____$_______$________$
   $$________$_______$$_________$$
    $_________$_____$___$$$$$$___$
       $______$____$__$________$__$
       $_____$____$__$__________$__$
      $____$___$$$$__$__________$__$$$$
     $___$____$____$__$________$___$___$
     $__$_____$____$__$________$__$____$
    $___$______$____$__$____$_$__$____$
      $__$______$____$___$_$_____$___$
       $___$$$$$_$___$___$_$____$___$
          $$$$$_$____$____$_____$____$
                $$$_$_____$______$_$$$
                     $$$$___$$$$$'''

def firekey11(key):
    clear()
    global keystartstop
    with open("data/saveonekey.txt","w") as key11:
        key11.write(str(key))
    keystartstop = str(key)
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка клавиши старт стоп")
        print(Fore.GREEN + "Нажатая клавиша " + str(key) + " записана")
        print(Fore.GREEN + ") Любая клавиша чтобы вернутся в настройки горячих клавиш")
    else:
        print(Fore.GREEN + "Setting the start stop key")
        print(Fore.GREEN + "Pressed key " + str(key) + " recorded")
        print(Fore.GREEN + ") Any key to return to hotkey settings")
    num = input()
    return False

def firekey1():
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка клавиши старт стоп")
        print(Fore.GREEN + "Нажмите на клавишу")
    else:
        print(Fore.GREEN + "Setting the start stop key")
        print(Fore.GREEN + "Press the key")
    with keyboard.Listener(on_press=firekey11) as listener:
        listener.join()
    clear()
    firekey()

def firekey22(key):
    clear()
    global keystop
    with open("data/savetwokey.txt","w") as key22:
        key22.write(str(key))
    keystop = str(key)
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка клавиши стоп чтобы перестать считывать клавиши")
        print(Fore.GREEN + "Нажатая клавиша " + str(key) + " записана")
        print(Fore.GREEN + ") Любая клавиша чтобы вернутся в настройки горячих клавиш")
    else:
        print(Fore.GREEN + "Setting the stop key to stop reading keys")
        print(Fore.GREEN + "Pressed key " + str(key) + " recorded")
        print(Fore.GREEN + ") Any key to return to hotkey settings")
    num = input()
    return False

def firekey2():
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка клавиши стоп чтобы перестать считывать клавиши")
        print(Fore.GREEN + "Нажмите на клавишу")
    else:
        print(Fore.GREEN + "Setting the stop key to stop reading keys")
        print(Fore.GREEN + "Press the key")
    with keyboard.Listener(on_press=firekey22) as listener:
        listener.join()
    clear()
    firekey()

def firekey33(key):
    clear()
    global keylock
    with open("data/savethreekey.txt","w") as key33:
        key33.write(str(key))
    keylock = str(key)
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка клавиши чтобы запомнить позицию мыши")
        print(Fore.GREEN + "Нажатая клавиша " + str(key) + " записана")
        print(Fore.GREEN + ") Любая клавиша чтобы вернутся в настройки горячих клавиш")
    else:
        print(Fore.GREEN + "Setting up a key to remember the mouse position")
        print(Fore.GREEN + "Pressed key " + str(key) + " recorded")
        print(Fore.GREEN + ") Any key to return to hotkey settings")
    num = input()
    return False

def firekey3():
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка клавиши чтобы запомнить позицию мыши")
        print(Fore.GREEN + "Нажмите на клавишу")
    else:
        print(Fore.GREEN + "Setting up a key to remember the mouse position")
        print(Fore.GREEN + "Press the key")
    with keyboard.Listener(on_press=firekey33) as listener:
        listener.join()
    clear()
    firekey()

def firekey44(key):
    clear()
    global keystartstoplock
    with open("data/savefourkey.txt","w") as key44:
        key44.write(str(key))
    keystartstoplock = str(key)
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка клавиши стоп чтобы перестать считывать клавиши")
        print(Fore.GREEN + "Нажатая клавиша " + str(key) + " записана")
        print(Fore.GREEN + ") Любая клавиша чтобы вернутся в настройки горячих клавиш")
    else:
        print(Fore.GREEN + "Setting the stop key to stop reading keys")
        print(Fore.GREEN + "Pressed key " + str(key) + " recorded")
        print(Fore.GREEN + ") Any key to return to hotkey settings")
    num = input()
    return False

def firekey4():
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка клавиши старт стоп с локом на позицию мыши")
        print(Fore.GREEN + "Нажмите на клавишу")
    else:
        print(Fore.GREEN + "Setting up the start/stop key with a lock on the mouse position")
        print(Fore.GREEN + "Press the key")
    with keyboard.Listener(on_press=firekey44) as listener:
        listener.join()
    clear()
    firekey()

def firekey55(key):
    clear()
    global keyhideshowconsole
    with open("data/savefivekey.txt","w") as key55:
        key55.write(str(key))
    keyhideshowconsole = str(key)
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка клавиши чтобы скрыть-показать консоль")
        print(Fore.GREEN + "Нажатая клавиша " + str(key) + " записана")
        print(Fore.GREEN + ") Любая клавиша чтобы вернутся в настройки горячих клавиш")
    else:
        print(Fore.GREEN + "Setting up a key to hide and show the console")
        print(Fore.GREEN + "Pressed key " + str(key) + " recorded")
        print(Fore.GREEN + ") Any key to return to hotkey settings")
    num = input()
    return False

def firekey5():
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка клавиши чтобы скрыть-показать консоль")
        print(Fore.GREEN + "Нажмите на клавишу")
    else:
        print(Fore.GREEN + "Setting up a key to hide and show the console")
        print(Fore.GREEN + "Press the key")
    with keyboard.Listener(on_press=firekey55) as listener:
        listener.join()
    clear()
    firekey()

def firekey():
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройки горячих клавиш")
        print(Fore.GREEN + "1) Настройка клавиши старт стоп " + str(keystartstop))
        print(Fore.GREEN + "2) Настройка клавиши стоп чтобы перестать считывать клавиши " + str(keystop))
        print(Fore.GREEN + "3) Настройка клавиши чтобы запомнить позицию мыши " + str(keylock))
        print(Fore.GREEN + "4) Настройка клавиши старт стоп с локом на позицию мыши " + str(keystartstoplock))
        print(Fore.GREEN + "5) Настройка клавиши чтобы скрыть-показать консоль " + str(keyhideshowconsole))
        print(Fore.GREEN + "9) Назад")
    else:
        print(Fore.GREEN + "Hotkey settings")
        print(Fore.GREEN + "1) Setting the start stop key " + str(keystartstop))
        print(Fore.GREEN + "2) Setting the stop key to stop reading keys " + str(keystop))
        print(Fore.GREEN + "3) Setting up a key to remember the mouse position " + str(keylock))
        print(Fore.GREEN + "4) Setting up the start/stop key with a lock on the mouse position " + str(keystartstoplock))
        print(Fore.GREEN + "5) Setting up a key to hide and show the console " + str(keyhideshowconsole))
        print(Fore.GREEN + "9) Back")
    try:
        num = int(input(Fore.MAGENTA + ">> "))
        if num == 9:
            clear()
            nastra()
        elif num == 1:
            clear()
            firekey1()
        elif num == 2:
            clear()
            firekey2()
        elif num == 3:
            clear()
            firekey3()
        elif num == 4:
            clear()
            firekey4()
        elif num == 5:
            clear()
            firekey5()
        else:
            clear()
            firekey()
    except ValueError:
        clear()
        firekey()

def goodinter():
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка интервала")
        print(Fore.GREEN + "Интервал " + str(timer) + " записан")
        print(Fore.GREEN + ") Любая клавиша чтобы вернутся в настройки")
    else:
        print(Fore.GREEN + "Setting the interval")
        print(Fore.GREEN + "Interval " + str(timer) + " recorded")
        print(Fore.GREEN + ") Any key to return to settings")
    num1 = input()
    clear()
    nastra()

def intervaltime():
    global timer
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка интервала в сек.")
        print(Fore.GREEN + "Ведите число. Рекомендованное минимальное значение 0.0002")
    else:
        print(Fore.GREEN + "Setting the interval in sec.")
        print(Fore.GREEN + "Enter a number. Recommended minimum value 0.0002")
    try:
        num = float(input(Fore.MAGENTA + ">> "))
        timer = num
        with open("data/savetime.txt","w") as timerr:
            timerr.write(str(num))
        clear()
        goodinter()
    except ValueError:
        clear()
        intervaltime()

def button_mouse():
    global button_mous
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка AUTOCLICKER")
        print(Fore.GREEN + "1) Left")
        print(Fore.GREEN + "2) Middle")
        print(Fore.GREEN + "3) Right")
        print(Fore.GREEN + "9) Назад")
    else:
        print(Fore.GREEN + "Setting up AUTOCLICKER")
        print(Fore.GREEN + "1) Left")
        print(Fore.GREEN + "2) Middle")
        print(Fore.GREEN + "3) Right")
        print(Fore.GREEN + "9) Back")
    try:
        num = int(input(Fore.MAGENTA + ">> "))
        if num == 1:
            with open("data/savebutmo.txt","w") as butmo:
                butmo.write("left")
            button_mous = "left"
            clear()
            nastra()
        elif num == 2:
            with open("data/savebutmo.txt","w") as butmo:
                butmo.write("middle")
            button_mous = "middle"
            clear()
            nastra()
        elif num == 3:
            with open("data/savebutmo.txt","w") as butmo:
                butmo.write("right")
            button_mous = "right"
            clear()
            nastra()
        elif num == 9:
            clear()
            nastra()
        else:
            clear()
            button_mouse()
    except ValueError:
        clear()

def languu():
    global lang
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "Настройка языка")
        print(Fore.GREEN + "1) English")
        print(Fore.GREEN + "2) Русский")
        print(Fore.GREEN + "9) Назад")
    else:
        print(Fore.GREEN + "Language settings")
        print(Fore.GREEN + "1) English")
        print(Fore.GREEN + "2) Русский")
        print(Fore.GREEN + "9) Back")
    try:
        num = int(input(Fore.MAGENTA + ">> "))
        if num == 1:
            lang = "eng"
            with open("data/savelang.txt","w") as langua:
                langua.write("eng")
            clear()
            nastra()
        elif num == 2:
            lang = "rus"
            with open("data/savelang.txt","w") as langua:
                langua.write("rus")
            clear()
            nastra()
        elif num == 9:
            clear()
            nastra()
        else:
            clear()
            languu()
    except ValueError:
        clear()
        languu()

def nastra():
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "            " + screen_size())
    if lang == "rus":
        print(Fore.GREEN + "    Настройки")
        print(Fore.GREEN + "1) Горячие клавиши")
        print(Fore.GREEN + "2) Интервал между кликами. Текущий " + str(timer))
        print(Fore.GREEN + "3) Кнопка мыши " + str(button_mous))
        print(Fore.GREEN + "4) Язык")
        print(Fore.GREEN + "9) Назад")
    else:
        print(Fore.GREEN + "    Settings")
        print(Fore.GREEN + "1) Hotkeys")
        print(Fore.GREEN + "2) Interval between clicks. Current " + str(timer))
        print(Fore.GREEN + "3) Mouse button " + str(button_mous))
        print(Fore.GREEN + "4) Language")
        print(Fore.GREEN + "9) Back")
    try:
        num = int(input(Fore.MAGENTA + ">> "))
        if num == 1:
            clear()
            firekey()
        elif num == 2:
            clear()
            intervaltime()
        elif num == 3:
            clear()
            button_mouse()
        elif num == 4:
            clear()
            languu()
        elif num == 9:
            clear()
            menu()
        else:
            clear()
            nastra()
    except ValueError:
        clear()
        nastra()

def autoclicker():
    while stop == 0:
        pyautogui.click(button=button_mous)
        time.sleep(timer)

def autoclickerlock():
    while stop == 0:
        pyautogui.click(x=mouse_position["x"],y=mouse_position["y"],button=button_mous)
        time.sleep(timer)

def autoclickertwo(key):
    clear()
    global stop
    global console
    global mouse_position
    if str(key) == keystartstop:
        if stop == 1:
            stop = 0
            th = Thread(target=autoclicker)
            th.start()
            if lang == "rus":
                print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
                print(Fore.GREEN + "Нажмите " + keystop + " чтобы остановить считывание клавиш")
                print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
                print(Fore.GREEN + "Нажмите " + keyhideshowconsole + " чтобы скрыть-показать консоль")
                print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
                print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                print(Fore.GREEN + "Интервал между кликами: " + str(timer))
                print(Fore.GREEN + "RUN AUTOCLICKER")
            else:
                print(Fore.GREEN + "Press " + keystartstop + " to start and stop AUTOCLICKER")
                print(Fore.GREEN + "Press " + keystop + " to stop reading keys")
                print(Fore.GREEN + "Press " + keylock + " to record the mouse position")
                print(Fore.GREEN + "Press " + keyhideshowconsole + " to hide and show the console")
                print(Fore.GREEN + "Press " + keystartstoplock + " to start and stop AUTOCLICKER but with a mouse position lock")
                print(Fore.GREEN + "Recorded mouse position: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                print(Fore.GREEN + "Interval between clicks: " + str(timer))
                print(Fore.GREEN + "RUN AUTOCLICKER")
        else:
            stop = 1
            if lang == "rus":
                print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
                print(Fore.GREEN + "Нажмите " + keystop + " чтобы остановить считывание клавиш")
                print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
                print(Fore.GREEN + "Нажмите " + keyhideshowconsole + " чтобы скрыть-показать консоль")
                print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
                print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                print(Fore.GREEN + "Интервал между кликами: " + str(timer))
                print(Fore.RED + "STOP AUTOCLICKER")
            else:
                print(Fore.GREEN + "Press " + keystartstop + " to start and stop AUTOCLICKER")
                print(Fore.GREEN + "Press " + keystop + " to stop reading keys")
                print(Fore.GREEN + "Press " + keylock + " to record the mouse position")
                print(Fore.GREEN + "Press " + keyhideshowconsole + " to hide and show the console")
                print(Fore.GREEN + "Press " + keystartstoplock + " to start and stop AUTOCLICKER but with a mouse position lock")
                print(Fore.GREEN + "Recorded mouse position: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                print(Fore.GREEN + "Interval between clicks: " + str(timer))
                print(Fore.RED + "STOP AUTOCLICKER")
    elif str(key) == keystop:
        if stop == 0:
            stop = 1
        if console == 0:
            console = 1
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
        return False
    elif str(key) == keylock:
        pos = pyautogui.position()
        mouse_position = {"x":pos[0],"y":pos[1]}
        if lang == "rus":
            print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
            print(Fore.GREEN + "Нажмите " + keystop + " чтобы остановить считывание клавиш")
            print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
            print(Fore.GREEN + "Нажмите " + keyhideshowconsole + " чтобы скрыть-показать консоль")
            print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
            print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
            print(Fore.GREEN + "Интервал между кликами: " + str(timer))
        else:
            print(Fore.GREEN + "Press " + keystartstop + " to start and stop AUTOCLICKER")
            print(Fore.GREEN + "Press " + keystop + " to stop reading keys")
            print(Fore.GREEN + "Press " + keylock + " to record the mouse position")
            print(Fore.GREEN + "Press " + keyhideshowconsole + " to hide and show the console")
            print(Fore.GREEN + "Press " + keystartstoplock + " to start and stop AUTOCLICKER but with a mouse position lock")
            print(Fore.GREEN + "Recorded mouse position: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
            print(Fore.GREEN + "Interval between clicks: " + str(timer))
    elif str(key) == keystartstoplock:
        if str(mouse_position["x"]) == "000":
            if lang == "rus":
                pyautogui.alert('Нет записанной позиции мыши')
                print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
                print(Fore.GREEN + "Нажмите " + keystop + " чтобы остановить считывание клавиш")
                print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
                print(Fore.GREEN + "Нажмите " + keyhideshowconsole + " чтобы скрыть-показать консоль")
                print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
                print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                print(Fore.GREEN + "Интервал между кликами: " + str(timer))
            else:
                pyautogui.alert('No mouse position recorded')
                print(Fore.GREEN + "Press " + keystartstop + " to start and stop AUTOCLICKER")
                print(Fore.GREEN + "Press " + keystop + " to stop reading keys")
                print(Fore.GREEN + "Press " + keylock + " to record the mouse position")
                print(Fore.GREEN + "Press " + keyhideshowconsole + " to hide and show the console")
                print(Fore.GREEN + "Press " + keystartstoplock + " to start and stop AUTOCLICKER but with a mouse position lock")
                print(Fore.GREEN + "Recorded mouse position: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                print(Fore.GREEN + "Interval between clicks: " + str(timer))
        else:
            if stop == 1:
                stop = 0
                th = Thread(target=autoclickerlock)
                th.start()
                if lang == "rus":
                    print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
                    print(Fore.GREEN + "Нажмите " + keystop + " чтобы остановить считывание клавиш")
                    print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
                    print(Fore.GREEN + "Нажмите " + keyhideshowconsole + " чтобы скрыть-показать консоль")
                    print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
                    print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                    print(Fore.GREEN + "Интервал между кликами: " + str(timer))
                    print(Fore.GREEN + "RUN AUTOCLICKER LOCK")
                else:
                    print(Fore.GREEN + "Press " + keystartstop + " to start and stop AUTOCLICKER")
                    print(Fore.GREEN + "Press " + keystop + " to stop reading keys")
                    print(Fore.GREEN + "Press " + keylock + " to record the mouse position")
                    print(Fore.GREEN + "Press " + keyhideshowconsole + " to hide and show the console")
                    print(Fore.GREEN + "Press " + keystartstoplock + " to start and stop AUTOCLICKER but with a mouse position lock")
                    print(Fore.GREEN + "Recorded mouse position: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                    print(Fore.GREEN + "Interval between clicks: " + str(timer))
                    print(Fore.GREEN + "RUN AUTOCLICKER LOCK")
            else:
                stop = 1
                if lang == "rus":
                    print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
                    print(Fore.GREEN + "Нажмите " + keystop + " чтобы остановить считывание клавиш")
                    print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
                    print(Fore.GREEN + "Нажмите " + keyhideshowconsole + " чтобы скрыть-показать консоль")
                    print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
                    print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                    print(Fore.GREEN + "Интервал между кликами: " + str(timer))
                    print(Fore.RED + "STOP AUTOCLICKER")
                else:
                    print(Fore.GREEN + "Press " + keystartstop + " to start and stop AUTOCLICKER")
                    print(Fore.GREEN + "Press " + keystop + " to stop reading keys")
                    print(Fore.GREEN + "Press " + keylock + " to record the mouse position")
                    print(Fore.GREEN + "Press " + keyhideshowconsole + " to hide and show the console")
                    print(Fore.GREEN + "Press " + keystartstoplock + " to start and stop AUTOCLICKER but with a mouse position lock")
                    print(Fore.GREEN + "Recorded mouse position: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                    print(Fore.GREEN + "Interval between clicks: " + str(timer))
                    print(Fore.RED + "STOP AUTOCLICKER")
    elif str(key) == keyhideshowconsole:
        if console == 1:
            console = 0
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        else:
            console = 1
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
            if lang == "rus":
                print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
                print(Fore.GREEN + "Нажмите " + keystop + " чтобы остановить считывание клавиш")
                print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
                print(Fore.GREEN + "Нажмите " + keyhideshowconsole + " чтобы скрыть-показать консоль")
                print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
                print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                print(Fore.GREEN + "Интервал между кликами: " + str(timer))
            else:
                print(Fore.GREEN + "Press " + keystartstop + " to start and stop AUTOCLICKER")
                print(Fore.GREEN + "Press " + keystop + " to stop reading keys")
                print(Fore.GREEN + "Press " + keylock + " to record the mouse position")
                print(Fore.GREEN + "Press " + keyhideshowconsole + " to hide and show the console")
                print(Fore.GREEN + "Press " + keystartstoplock + " to start and stop AUTOCLICKER but with a mouse position lock")
                print(Fore.GREEN + "Recorded mouse position: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
                print(Fore.GREEN + "Interval between clicks: " + str(timer))

def autoclickerone():
    if lang == "rus":
        print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
        print(Fore.GREEN + "Нажмите " + keystop + " чтобы остановить считывание клавиш")
        print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
        print(Fore.GREEN + "Нажмите " + keyhideshowconsole + " чтобы скрыть-показать консоль")
        print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
        print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
        print(Fore.GREEN + "Интервал между кликами: " + str(timer))
    else:
        print(Fore.GREEN + "Press " + keystartstop + " to start and stop AUTOCLICKER")
        print(Fore.GREEN + "Press " + keystop + " to stop reading keys")
        print(Fore.GREEN + "Press " + keylock + " to record the mouse position")
        print(Fore.GREEN + "Press " + keyhideshowconsole + " to hide and show the console")
        print(Fore.GREEN + "Press " + keystartstoplock + " to start and stop AUTOCLICKER but with a mouse position lock")
        print(Fore.GREEN + "Recorded mouse position: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
        print(Fore.GREEN + "Interval between clicks: " + str(timer))
    with keyboard.Listener(on_press=autoclickertwo) as listener:
        listener.join()
    clear()
    menu()

def menu():
    print(Fore.GREEN + kart)
    if lang == "rus":
        print(Fore.GREEN + "1) Настройки")
        print(Fore.GREEN + "2) Начать считывать нажатия")
        print(Fore.GREEN + "9) Выход")
    else:
        print(Fore.GREEN + "1) Settings")
        print(Fore.GREEN + "2) Start counting keystrokes")
        print(Fore.GREEN + "9) Exit")
    try:
        num = int(input(Fore.MAGENTA + ">> "))
        if num == 9:
            sys.exit()
        elif num == 1:
            clear()
            nastra()
        elif num == 2:
            clear()
            autoclickerone()
        else:
            clear()
            menu()
    except ValueError:
        clear()
        menu()

menu()