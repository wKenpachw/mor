import random

def rund_varLir(n_cubs, val_cubs, max_vals_count):
    val_list =list()
    for i in range(0, n_cubs):
        val_list.append(random.randint(1,val_cubs))
    val_list.sort(reverse = True)
    summ = val_list[0] + val_list[1] + val_list[2] + val_list[3] + val_list[4] + val_list[5]
    return summ

print ("Урон: " +str( rund_varLir(12, 12, 6)))