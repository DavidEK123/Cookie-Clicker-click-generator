
import pynput
from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
import subprocess
import time
mouse = Controller()
x = int(input("Enter the amount of cookies you want generated: "))
time.sleep(5)

for i in range (x):
    
    time.sleep(0.05)
    mouse = Controller()
    mouse.click(Button.left, 1)

     
print(x ,"cookies generated")
