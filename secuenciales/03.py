import os

os.system("cls")

kilometros=float(input("Longitud del primer tramo (kilometro):"))
pies=float(input("Longitud del segundo tramo (Pies):"))
millas=float(input("Longitud del tercer tramo (millas)"))

primer_tramo=kilometros*1000
segundo_tramo=pies/3.2808
tercer_tramo=millas*1609
total_metros=primer_tramo+segundo_tramo+tercer_tramo
total_yardas=((total_metros*3.2808)/3)

print("Total en metros:",format(total_metros,".2f"),"m")
print("Total en yardas:",format(total_yardas,".2f"),"yd")