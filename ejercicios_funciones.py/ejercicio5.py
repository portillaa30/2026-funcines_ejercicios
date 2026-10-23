def calcular_subtotal(base: float, descuento: float) -> float:
  subtotal = base * (1 - descuento / 100)
  return subtotal


def calcular_total_con_impuesto(subtotal: float, impuesto: float) -> float:
  total = subtotal * (1 + impuesto / 100)
  return total


base = float(input("Ingrese la base en pesos: "))
descuento = float(input("Ingrese el porcentaje de descuento (0 a 100): "))
impuesto = float(input("Ingrese el porcentaje de impuesto: "))

subtotal = calcular_subtotal(base, descuento)
total = calcular_total_con_impuesto(subtotal, impuesto)

print(f"Subtotal: {subtotal}; total: {total} pesos")