import viddil
from math import log10

def input_number(str):
    while True:
        try:
            n = int(input(str))
            break
        except:
            print("try again; only numbers")
    return abs(n)

def input_word(str):
    while True:
        w = input(str)
        if w.isalpha()== True: break
        else: print("try again; only letters")
    return w

def input_with_smth(str, some):
    while True:
        w = input(str)
        if some in w:
            break
        else: print("try again; only letters")
    return w

def input_number_lenght(str, long):
    while True:
        n=input_number(str)
        if int(log10(n))+1 == long : break
        else: print("length must be", long)
    return abs(n)



def check_viddil(viddil):
    result = True
    if str(viddil.ID).isdigit() == False: result = False
    if viddil.title.isalpha()== False: result=False
    if viddil.director_name.isalpha()==False: result=False
    size_phone = int(log10(int(viddil.phone_number)))+1
    if str(viddil.phone_number).isdigit()==False or size_phone!=12: result=False
    if str(viddil.monthly_budget).isdigit()==False: result=False
    if str(viddil.yearly_budget).isdigit()==False : result= False

    return result