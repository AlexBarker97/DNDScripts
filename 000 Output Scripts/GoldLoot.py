import math
import time

players = int(input("Number of players: "))
baseGP = int(input("Base gold each: "))
maxBonus = int(input("Maximum extra each: "))
if maxBonus < 4:
    dice = 2
elif maxBonus < 6:
    dice = 4
elif maxBonus < 8:
    dice = 6
elif maxBonus < 10:
    dice = 8
elif maxBonus < 12:
    dice = 10
elif maxBonus < 100:
    dice = 20
else:
    dice = 100
print("/r ",math.floor((maxBonus/dice))*players,"d",dice,"+",baseGP*players,sep='')

time.sleep(10)