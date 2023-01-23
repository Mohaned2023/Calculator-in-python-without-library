# Written by Mohaned Mohammed Sherhan 

# import operator and reduce and time 
import operator
from functools import reduce
import time 

# liste to add the numbers in the liste
liste_add_num = []

# def add numbers
def sum_num(*numbers):
    for i in numbers:
        number = i 
    return reduce(operator.add,number)

# def sub numbers 
def sub_num(*numbers):
    for i in numbers:
        number = i 
    return reduce(operator.sub,number)

# def mul numbers 
def mul_num(*numbers):
    for i in numbers:
        number = i 
    return reduce(operator.mul,number)

# def truediv numbers 
def div_num(*numbers):
    for i in numbers:
        number = i 
    return reduce(operator.truediv,number)

# def to add numebrs in the liste 
def add_to_liste (addtoliste):
    liste_add_num.append(addtoliste)

# def for loop to input the number 
def Process_num():
    chooes = int (input("The number of operatins you will perform :  "))
    for i in range(chooes):
        m = int(input("Enter the operation number > "+str(i+1)+":  "))
        add_to_liste(m)
    return liste_add_num

# def input for the user 
def chooes_the_pro():
    print ("""
        { 1 } it's for sum;{+} numbers.
        { 2 } it's for sub;{-} number.
        { 3 } it's for mul;{*} numbers.
        { 4 } it's for div;{/} numbers.
    """)
    inp_choose = int (input ("--> "))
    if inp_choose == 1:
        Process_num()
        print (sum_num(liste_add_num))
        chooes_the_pro()
    elif inp_choose == 2:
        Process_num()
        print (sub_num(liste_add_num))
        chooes_the_pro()
    elif inp_choose == 3:
        Process_num()
        print (mul_num(liste_add_num))
        chooes_the_pro()
    elif inp_choose == 4 :
        Process_num()
        print (div_num(liste_add_num))
        chooes_the_pro()
    else:
        print ("Error input ")
        time.sleep(2)
        chooes_the_pro()
chooes_the_pro()


