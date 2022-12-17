import os 
os.system("cls")

print("")
dinero_juan=float(input("Dinero de Juan: $"))
dinero_rosa=float(input("Dinero de rosa: $"))
dinero_daniel=float(input("Dinero de Daniel: S/."))

dolares_daniel=dinero_daniel/3
capital_total=dinero_juan+dinero_rosa+dolares_daniel
porcentaje_juan=(dinero_juan*100)/capital_total
porcentaje_rosa=(dinero_rosa*100)/capital_total
porcentaje_daniel=(dolares_daniel*100)/capital_total

print("El capital total es: $",format(capital_total,".2f"))
print("juan dio el",format(porcentaje_juan,".2f"),"%")
print("Rosa dio el",format(porcentaje_rosa,".2f"),"%")
print("Daniel dio el",format(porcentaje_daniel,".2f"),"%")
