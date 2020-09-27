#-*- coding: UTF-8 -*-
age = 120
is_flag = True

if age>=0 and age<=120:
    print("0-120")
else:
    print("不符合条件")

if age>=1000 or not is_flag:
    print("大于零或false")
else:
    print("不满足")