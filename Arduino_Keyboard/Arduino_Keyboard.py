import serial #Serial imported for Serial communication
import time #Required to use delay functions
import pyautogui

#button Config
#   1   2   3
#   4   5   6
#   7   8   9

ArduinoSerial = serial.Serial('COM6',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 seconds for the communication to get established

while 1:
    macro = ArduinoSerial.readline() #read the serial data  

    if '1' in macro:
            pyautogui.write('Hello world!', interval=0.25)
            #pyautogui.hotkey('alt', 'f4')
            
    if '2' in macro:
        pyautogui.press('up')  

    if '3' in macro:
        pyautogui.keyDown('shift')  # hold down the shift key
        time.sleep(5)
        pyautogui.keyUp('shift')    # release the shift key

    if '4' in macro:
        pyautogui.press('left')
        #pyautogui.press('@', presses=3)
        
    if '5' in macro:
            pyautogui.press('enter')
            #pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
            #pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste
            
    if '6' in macro:
        pyautogui.press('right')  

    if '7' in macro:
        pyautogui.press('esc')
        #pyautogui.hotkey('ctrl', 'shift', 'esc')

    if '8' in macro:
        pyautogui.press('down')
            
    if '9' in macro:
        pyautogui.typewrite(['space'], 0.2)

        
