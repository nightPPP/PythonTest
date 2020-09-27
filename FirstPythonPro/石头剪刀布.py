#-*- coding: UTF-8 -*-
import random
# 石头-1  剪刀-2    布-3
player = (int)(input(" 请输入 石头(1)  剪刀(2)  布(3)"))
computer = random.randint(1,3)

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer ==1)):
    print("player 胜出")
elif player == computer:
    print("平局")
else :
    print ("computer 胜出")