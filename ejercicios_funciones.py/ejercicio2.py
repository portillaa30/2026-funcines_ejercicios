costo1=int(input("Ingrese el costo del primer producto: "))
peso1=int(input("Ingrese el peso del primer producto: "))
costo2=int(input("Ingrese el costo del segundo prodcuto: "))
peso2=int(input("Ingrese el peso del segundo producto: "))

def precio_por_gramo(costo,peso):
    precio=costo/peso
    return precio

if precio_por_gramo(costo1,peso1) < precio_por_gramo(costo2,peso2):
    print("Precio por gramo", precio_por_gramo(costo1,peso1),"y", precio_por_gramo(costo2,peso2),"conviene producto 1")
else:
    print("Precio por gramo", precio_por_gramo(costo1,peso1),"y", precio_por_gramo(costo2,peso2), "conviene producto 2")
