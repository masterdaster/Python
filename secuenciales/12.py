import os 
os.system("cls")

print("")
num_segundos=int(input("Digite un numero expresado en segundos: "))

dias=((num_segundos//60)//60)//24
hora=((num_segundos//60)//60)%24
minutos=(num_segundos//60)%60
segundos=num_segundos%60

print("Dias: ",dias)
print("horas: ",hora)
print("Minutos: ",minutos)
print("Segundos: ",segundos)
print("")
