# Solicitamos los datos al usuario
hemisferio = input("¿En qué hemisferio te encuentras? (N para Norte / S para Sur): ").upper()
mes = int(input("Ingresa el mes actual (1-12): "))
dia = int(input("Ingresa el día actual (1-31): "))

# Determinamos la estación según hemisferio
if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
else:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

# Mostramos el resultado según el hemisferio
if hemisferio == "N":
    print(f"\nActualmente es {estacion_norte} en el hemisferio Norte")
elif hemisferio == "S":
    print(f"\nActualmente es {estacion_sur} en el hemisferio Sur")
else:
    print("\nHemisferio no válido. Debe ser N (Norte) o S (Sur)")