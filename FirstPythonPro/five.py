#-*- coding: UTF-8 -*-
"""
*
**
***
****
*****
"""

row = 1

# 5行
while row <= 5:
    column = 1
    while column <= row:
        column += 1
        print("*", end="")

    row += 1

    print ("")