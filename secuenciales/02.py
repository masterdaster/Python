import os 
os.system("cls")

metros=int(input("Digite una cantidad en metros:"))

centimetros=metros*100
pulgadas=centimetros/2.54
pies=pulgadas/12
yardas=pies/3

print("Centimetros:",format(centimetros,".2f"),"cm")
print("Pulgadas:",format(pulgadas,".2f"),"in")
print("pies:",format(pies,".2f"),"ft")
print("Yardas:",format(yardas,".2f"),"yd")
 