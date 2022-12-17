import os
os.system("cls")

nota_de_practica1= float(input("ingrese el vavor de la practica 1:"))
nota_de_practica2= float(input("ingrese el valor de la practica 2:"))
nota_de_practica3= float(input("ingrese el valor de la practica 3:"))
promedio_final= nota_de_practica1 + nota_de_practica2 +nota_de_practica3

if nota_de_practica1 >= 10 and nota_de_practica1 < 18:
    promedio_final = promedio_final + 2
if nota_de_practica2 >= 10 and nota_de_practica2 < 18:
    promedio_final = promedio_final + 2
if nota_de_practica3 >= 10 and nota_de_practica3 < 18:
    promedio_final = promedio_final + 2

if nota_de_practica1 >= 18 and nota_de_practica1 < 20:
    promedio_final = promedio_final- nota_de_practica1 + 20
if nota_de_practica2 >= 18 and nota_de_practica2 < 20:
    promedio_final = promedio_final- nota_de_practica2 + 20
if nota_de_practica3 >= 18 and nota_de_practica3 < 20:
    promedio_final = promedio_final- nota_de_practica3 + 20

promedio_final = promedio_final/3
print("valor de promedio final:" + repr(promedio_final))
print()
