# Solicitamos los datos al usuario
nombre = input("Ingrese su nombre: ")
opcion = input("Seleccione una opción (1, 2 o 3):\n"
               "1. Nombre en MAYÚSCULAS\n"
               "2. nombre en minúsculas\n"
               "3. Nombre con primera letra mayúscula\n"
               "Opción: ")

# Procesamos según la opción seleccionada
if opcion == "1":
    resultado = nombre.upper()  # Convierte todo a mayúsculas
elif opcion == "2":
    resultado = nombre.lower()  # Convierte todo a minúsculas
elif opcion == "3":
    resultado = nombre.title()  # Primera letra mayúscula, resto minúsculas
else:
    resultado = "Opción no válida. Debe ser 1, 2 o 3."

# Mostramos el resultado
print("\nResultado:", resultado)