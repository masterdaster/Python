import os 
os.system("cls")

unidades = int(input("unidades adquiridas: "))
Precio = 25
if unidades <= 25 : Precio = 27
elif unidades >= 51 : Precio = 23

compra = unidades * Precio
descuento = (0.12 if unidades < 50 else 0.05)* compra

print(f"precio = {Precio}\n ")
print(f"compra = {compra}\n ")
print(f"descuento = {descuento}\n ")
print(f"total = {compra - descuento}\n ")

