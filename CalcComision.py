nombre = input("Cual es tu nombre? ")
ventas = input("cuanto vendiste este mes? ")
ventas = int(ventas)
comision = ventas*13/100

print(f"Ok {nombre} este mes ganaste ${comision}")