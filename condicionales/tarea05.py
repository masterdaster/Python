import os
os.system("cls")

num_1 = float(input("ingrese el primer numero:"))
num_2 = float(input("ingrese el segundo numero:"))
num_3 = float(input("ingrese el tercer numero:"))
num_4 = float(input("ingrese el cuarto numero:"))

##num_1> num_1,num_3,num_4,num_2
##num_2> num_2,num_3,num_1,num_4
##num_3> num_4,num_1,num_2,num_3
##num_4> num_2,num_4,num_3,num_1

if num_4<num_1*num_2>num_3:
    print("los numeros mayores son el primero y segundo numero. numeros primero y segundo", num_1*num_2)
elif num_1<num_4*num_2>num_3:
    print("los numeros mayores son el cuarto y segundo numero. numeros cuarto y segundo",num_4*num_2)
elif num_2<num_3*num_4>num_1:
    print("los numeros mayores son el tercero y cuarto numero. numeros tercero y cuarto",num_3*num_4)
elif num_2<num_3*num_1>num_4:
    print("los numeros mayores son el tercero y primer numero. numeros tercero y primero", num_3*num_1)