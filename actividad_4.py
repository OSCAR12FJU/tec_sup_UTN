edad = input("Ingresa tu edad")

if numero and int(edad) < 12:
    print("Sos un miño/a")
elif numero and int(edad) >=12 and int(edad) < 18:
    print("Sos un adolecente")
elif numero and int(edad) >= 18 and int(edad) < 30:
    print("Sos un adulto/a joven")
else:
    print("Sos un adulto/a")