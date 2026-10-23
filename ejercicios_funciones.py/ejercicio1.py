base1=int(input("Ingrese la base"))
altura1=int(input("Ingrese la altura"))
base2=int(input("ingrese la base 2:"))
altura2=int(input("Ingrese la altura2: "))


def calcular_area(base,altura):
    area=(base * altura)/2
    return area


print("El area del triangulo 1 es:",calcular_area(base1,altura1),"el area del triangulo 2 es:", calcular_area(base2,altura2), "y la suma es", calcular_area(base1,altura1)+calcular_area(base2,altura2))

