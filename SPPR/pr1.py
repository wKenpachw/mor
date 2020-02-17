import math
import random

pak_1 = 10
pak_2 = 10
pak_3 = 20

have_1 = 0
have_2 = 0
have_3 = 0

k_1 = 5
k_2 = 10

need_1 = 20
need_2 = 25
need_3 = 35

flag = True
wait = "1"
i = 1

b1 = 0
b2 = 0

def broke_1():
    global need_1
    global need_2
    global need_3
    need_1 += 2
    need_2 += 1
    need_3 += 1

def broke_2():
    global need_1
    global need_2
    global need_3
    need_1 += 1
    need_2 += 2
    need_3 += 3
def set_standatrt_need():
    global need_1
    global need_2
    global need_3
    need_1 = 20
    need_2 = 25
    need_3 = 35

def result(need, have, pak):
    print("Имеется " + str(have) )
    print("Нужно " + str(need) )
    #print("Размер пака " + str(pak) )
    return math.ceil((need - have)/pak)
while (flag):

    for z in range(1, 5):
        if (random.randint(1, 10)  == 1):
            broke_1()
            print("Брак_1")
            b1 +=1
    for z in range(1, 10):
        if (random.randint(1, 10)  == 1):
         #   broke_2()
            print("Брак_2")
            b2 +=1
    print("заказ № " + str(i))
    print(b1)
    print(b2)
    need_1 += b1*2 + b2 
    need_2 += b1 + b2*2 
    need_3 += b1 + b2*3 

    res_1 = result(need_1,have_1, pak_1)
    if (res_1 > 0):
        have_1 = pak_1 * res_1 -need_1 + have_1
    print( "паков копмонентов №1 необходимо " + str(res_1) + "\n") 
    
    res_2 = result(need_2,have_2, pak_2)
    if (res_2 > 0):
        have_2 = pak_2 * res_2 -need_2 + have_2
    print( "паков копмонентов №2 необходимо " + str(res_2) + "\n") 

    res_3 = result(need_3,have_3, pak_3)
    if (res_3 > 0):
        have_3 = pak_3 * res_3 -need_3 + have_3
    print( "паков копмонентов №3 необходимо " + str(res_3) + "\n")
    set_standatrt_need()
    b1 = 0
    b2 = 0
    wait = input("PRESS 1 and ENTER\n")
    i+=1
    if (wait != "1"): flag = False
"""
    def funck_1(need, have, pak):
        res = math.ceil((need - have)/pak)
        if (res > 0):
            have = pak * res - need + have
        print( "need to have res = " + str(res) + "\n")
"""