print("")
radio=float(input("Ingrese el radio del cilindro:"))
altura=float(input("Ingrese la altura del cilindro:"))

areatotal=2*3.1416*radio*(radio+altura)
volumen=3.1416*radio*2*altura

print("El area total del cilindro es",format(areatotal,".2f"))
print("El volumen del cilindro es",format(volumen,".2f"))

