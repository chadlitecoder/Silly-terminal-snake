import keyboard
from collections import deque
from playsound3 import playsound
import time
print('''          
             |            Welcome!              |
             |       press 'esc' to exit        |
             |  press 'space' to make new snake |\n
             ''')
def snake():
    snakeinfo=input("\nProvide snake speed and size:")
    speed=float(snakeinfo.split(" ")[0])
    snakesize="x"*int(snakeinfo.split(" ")[1])
    snakestr="("+snakesize+")"
    right=deque([" "]*60)
    right.append(snakestr)
    print(''' Enjoy the realistic snake simulator''')
    while True:
        if keyboard.is_pressed('right'):
            if len(right)<=135:
                right.appendleft(" ")
                print(''.join(right))
                time.sleep(speed)


        if keyboard.is_pressed('left'):
            if right.count(snakestr)and right.count(" ")>=1:
                right.popleft()
                print(''.join(right))
                time.sleep(speed)
        if keyboard.is_pressed('space'):
            print("                                       snake died, make new snake")
            snake()
        if keyboard.is_pressed('esc'):
            print("                                       ALL THE SNAKES ARE FUCKING DEAD")
            break
        elif keyboard.is_pressed('right') is False:
            if keyboard.is_pressed('left') is False:
                for i in range(5):
                    right.appendleft(" ")
                    print(''.join(right))
                    time.sleep(speed)
                for i in range(5):
                    right.popleft()
                    print(''.join(right))
                    time.sleep(speed)
snake()