import os
os.system ("cls")

unidades=int(input("unidades adquiridas:"))
precio = 20
caramelos = 5 <= 15

if unidades <= 50: precio = 20*5
elif unidades >= 100: precio = 20*5

compra = unidades*precio 
descuento = (0.16 if unidades< 51 else 0.12)*compra 

print(f"precio ={precio}\n")
print(f"compra = {compra}\n")
print(f"descuento = {descuento}\n")
print(f"total = {compra - descuento}\n")
