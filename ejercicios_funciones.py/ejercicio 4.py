horas1=int(input("Ingrese las horas laboradas del primer trabajador:  "))
horas2=int(input("Ingrese las horas laboradas del segundo trabajador:"))
tarifa=int(input("Ingrese la tarifa del trabajador"))

def pago_semana(horas:int,tarifa:int)->int:
    if horas<=40:
        pago=horas*tarifa
    elif horas>40:
        pago=40*tarifa+(horas-40)*tarifa*1.5
    return pago

total=pago_semana(horas1,tarifa)+pago_semana(horas2,tarifa)

print("Pagos:",pago_semana(horas1,tarifa),"y", pago_semana(horas2,tarifa),", total:", total)
