import os
import sys
import colorama
from colorama import Fore
from threading import Thread
from pynput import keyboard
import pyautogui
import time
import subprocess

subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)

colorama.init(True)

def screen_size():
    size = pyautogui.size()
    pr = "Разрешение экрана: X=" + str(size[0]) + " Y=" + str(size[1])
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

mouse_position = {"x":"15","y":"15"}

stop = 1

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
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    with open("data/saveonekey.txt","w") as key11:
        key11.write(str(key))
    keystartstop = str(key)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройка клавиши старт стоп")
    print(Fore.GREEN + "Нажатая клавиша " + str(key) + " записана")
    print(Fore.GREEN + ") Любая клавиша чтобы вернутся в настройки горячих клавиш")
    num = input()
    return False

def firekey1():
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройка клавиши старт стоп")
    print(Fore.GREEN + "Нажмите на клавишу")
    with keyboard.Listener(on_press=firekey11) as listener:
        listener.join()
    clear()
    firekey()

def firekey22(key):
    clear()
    global keystop
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    with open("data/savetwokey.txt","w") as key22:
        key22.write(str(key))
    keystop = str(key)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройка клавиши стоп чтобы перестать считывать клавиши")
    print(Fore.GREEN + "Нажатая клавиша " + str(key) + " записана")
    print(Fore.GREEN + ") Любая клавиша чтобы вернутся в настройки горячих клавиш")
    num = input()
    return False

def firekey2():
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройка клавиши стоп чтобы перестать считывать клавиши")
    print(Fore.GREEN + "Нажмите на клавишу")
    with keyboard.Listener(on_press=firekey22) as listener:
        listener.join()
    clear()
    firekey()

def firekey33(key):
    clear()
    global keylock
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    with open("data/savethreekey.txt","w") as key33:
        key33.write(str(key))
    keylock = str(key)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройка клавиши стоп чтобы перестать считывать клавиши")
    print(Fore.GREEN + "Нажатая клавиша " + str(key) + " записана")
    print(Fore.GREEN + ") Любая клавиша чтобы вернутся в настройки горячих клавиш")
    num = input()
    return False

def firekey3():
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройка клавиши чтобы запомнить позицию мыши")
    print(Fore.GREEN + "Нажмите на клавишу")
    with keyboard.Listener(on_press=firekey33) as listener:
        listener.join()
    clear()
    firekey()

def firekey44(key):
    clear()
    global keystartstoplock
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    with open("data/savethreekey.txt","w") as key44:
        key44.write(str(key))
    keystartstoplock = str(key)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройка клавиши стоп чтобы перестать считывать клавиши")
    print(Fore.GREEN + "Нажатая клавиша " + str(key) + " записана")
    print(Fore.GREEN + ") Любая клавиша чтобы вернутся в настройки горячих клавиш")
    num = input()
    return False

def firekey4():
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройка клавиши старт стоп с локом на позицию мыши")
    print(Fore.GREEN + "Нажмите на клавишу")
    with keyboard.Listener(on_press=firekey44) as listener:
        listener.join()
    clear()
    firekey()

def firekey():
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройки горячих клавиш")
    print(Fore.GREEN + "1) Настройка клавиши старт стоп " + str(keystartstop))
    print(Fore.GREEN + "2) Настройка клавиши стоп чтобы перестать считывать клавиши " + str(keystop))
    print(Fore.GREEN + "3) Настройка клавиши чтобы запомнить позицию мыши " + str(keylock))
    print(Fore.GREEN + "4) Настройка клавиши старт стоп с локом на позицию мыши " + str(keystartstoplock))
    print(Fore.GREEN + "9) Назад")
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
        else:
            clear()
            firekey()
    except ValueError:
        clear()
        firekey()

def goodinter():
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройка интервала")
    print(Fore.GREEN + "Интервал " + str(timer) + " записан")
    print(Fore.GREEN + ") Любая клавиша чтобы вернутся в настройки")
    num1 = input()
    clear()
    nastra()

def intervaltime():
    global timer
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройка интервала в сек.")
    print(Fore.GREEN + "Ведите число. Рекомендованное минимальное значение 0.0002")
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
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "Настройка AUTOCLICKER")
    print(Fore.GREEN + "1) Left")
    print(Fore.GREEN + "2) Middle")
    print(Fore.GREEN + "3) Right")
    print(Fore.GREEN + "9) Назад")
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

def nastra():
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "            " + screen_size())
    print(Fore.GREEN + "    Настройки")
    print(Fore.GREEN + "1) Горячие клавиши")
    print(Fore.GREEN + "2) Интервал между кликами. Текущий " + str(timer))
    print(Fore.GREEN + "3) Кнопка мыши " + str(button_mous))
    print(Fore.GREEN + "9) Назад")
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
    global stop
    global mouse_position
    if str(key) == keystartstop:
        if stop == 1:
            stop = 0
            th = Thread(target=autoclicker)
            th.start()
            subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
            print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
            print(Fore.GREEN + "Нажмите " + keystop + " чтобы остоновить считывание клавиш")
            print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
            print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
            print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
            print(Fore.GREEN + "Интервал между кликами: " + str(timer))
            print(Fore.GREEN + "RUN AUTOCLICKER")
        else:
            stop = 1
            subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
            print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
            print(Fore.GREEN + "Нажмите " + keystop + " чтобы остонивить считывание клавиш")
            print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
            print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
            print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
            print(Fore.GREEN + "Интервал между кликами: " + str(timer))
            print(Fore.RED + "STOP AUTOCLICKER")
    elif str(key) == keystop:
        if stop == 0:
            stop = 1
        time.sleep(0.3)
        return False
    elif str(key) == keylock:
        pos = pyautogui.position()
        mouse_position = {"x":pos[0],"y":pos[1]}
        subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
        print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
        print(Fore.GREEN + "Нажмите " + keystop + " чтобы остонивить считывание клавиш")
        print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
        print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
        print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
        print(Fore.GREEN + "Интервал между кликами: " + str(timer))
        print(Fore.GREEN + "Позиция мыши записана X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
    elif str(key) == keystartstoplock:
        if stop == 1:
            stop = 0
            th = Thread(target=autoclickerlock)
            th.start()
            subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
            print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
            print(Fore.GREEN + "Нажмите " + keystop + " чтобы остонивить считывание клавиш")
            print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
            print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
            print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
            print(Fore.GREEN + "Интервал между кликами: " + str(timer))
            print(Fore.GREEN + "RUN AUTOCLICKER LOCK")
        else:
            stop = 1
            subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
            print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
            print(Fore.GREEN + "Нажмите " + keystop + " чтобы остонивить считывание клавиш")
            print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
            print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
            print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
            print(Fore.GREEN + "Интервал между кликами: " + str(timer))
            print(Fore.RED + "STOP AUTOCLICKER")

def autoclickerone():
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + "Нажмите " + keystartstop + " чтобы запустить и остановить AUTOCLICKER")
    print(Fore.GREEN + "Нажмите " + keystop + " чтобы остонивить считывание клавиш")
    print(Fore.GREEN + "Нажмите " + keylock + " чтобы записать позицию мыши")
    print(Fore.GREEN + "Нажмите " + keystartstoplock + " чтобы запустить и остановить AUTOCLICKER но с локом позиции на мыши")
    print(Fore.GREEN + "Записанная позиция мыши: X=" + str(mouse_position["x"]) + " Y=" + str(mouse_position["y"]))
    print(Fore.GREEN + "Интервал между кликами: " + str(timer))
    with keyboard.Listener(on_press=autoclickertwo) as listener:
        listener.join()
    clear()
    menu()

def menu():
    subprocess.run(['mode', 'con:', 'cols=45', 'lines=30'], shell=True)
    print(Fore.GREEN + kart)
    print(Fore.GREEN + "1) Настройки")
    print(Fore.GREEN + "2) Начать считывать нажатия")
    print(Fore.GREEN + "9) Выход")
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