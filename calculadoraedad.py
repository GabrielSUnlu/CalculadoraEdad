from datetime import date

edad = input("ingresa tu edad: ")
edad1 = int(edad)
todays_date = date.today()
anio = int(todays_date.year)
print(("Tu año de nacimiento es"),(anio - edad1))