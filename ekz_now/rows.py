import math
f = open('c:/Users/Лёха/Documents/PyCharm/MorozovAP/ekz_now/text.txt', 'r')
safe_dict = {"^":"**", "cos":"math.cos", "sin":"math.sin", "tan":"math.tan"}
for line in f:
    print(line)
    for item in safe_dict.items() :
        if (line.find(item[0]) != -1):
            line = line.replace(item[0], item[1])

    def check_to_null(line):
        curent_line = line.replace("x", "10000")
        y = eval(curent_line)
        print (eval(curent_line))
        if (y > 0.0000001):
            print("Сотый член не стремится к нулю")
        else:
            print("Сотый член стремится к нулю => ряд расходится")

    def compare_with_another(line):
        def current_garm_value(x_garm, y_garm):
            try:
                res =  1/(x_garm**y_garm)
            except ZeroDivisionError:
                res = 9999
            return res
        for i in range(10, 0, -1):
            count = 0
            for z in range(5):
                try:
                    
                    curent_line = line.replace("x", str(z))
                    if(current_garm_value(z, i/10) > eval(curent_line)):
                        #print("гармоничный больше!!")
                        count +=1
                    #else:
                        #print("гармоничный меньше!!")
                except ZeroDivisionError:
                    print("деление на ноль")
            if(count == 4 ):
                print("4 члена ряда подряд меньше гармонического ряда")
                #break


    for i in range(0, 5):
        curent_line = line.replace("x", str(i))
        try:
            print (eval(curent_line))
        except ZeroDivisionError:
            print("деление на ноль")

    check_to_null(line)
    print("\n")
    compare_with_another(line)

