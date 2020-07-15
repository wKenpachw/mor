import math

def get_year_cost(args):
    res = 0
    try:
        res = float (args[7]) + float(args[8])
    except:
        print("error year_cost")
    return round(res, 2)

def get_izd_cost(args):
    res = 0
    try:
        res = float(args[2]) + (float (args[3]) + float (args[4]) + float (args[5]) + float (args[6]))/ float (args[1])
    except:
        print("error izd_cost")
    return round(res, 2)

def nkp12(c1,v1,c2,v2):
    res = 0.0
    try:
        res = (c2 - c1)/(v1 - v2)
    except:
        print('error nkp12')
    return round(res)

def sTeh(c, v, n):
    res = 0
    try:
        res = (c * (n -1) + v)
    except:
        print("error sTeh")
    return round(res)

def end_result(s1, s2, n):
    res = ""
    try:
        if (s1 > s2) : 
            res = "Второй процес обработки оэкономичнее при =<" + str (n) + ", первый вариант экономичнее при > " + str (n)
        elif (s1 < s2):
            res = "Первый процес обработки оэкономичнее при =<" + str (n) + ", второй вариант экономичнее при > " + str (n)
        else:
            res = " ошибка в расчётах, s равны!"
    except:
        print ("error end_result")
    return res