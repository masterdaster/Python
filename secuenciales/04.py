import os

os.system("cls")

pies=float(input("pies:"))
pulgadas=float(input("pulgadas:"))

estatura=(((pies*12)+ pulgadas)*2.54)/100

print("La estatura en metros es:",format(estatura,".2f"),"m")
