# Solicitamos la frase al usuario
frase = input("Ingresa cualquier frase: ")

# Verificamos si la frase termina con vocal
if len(frase) > 0:  # Comprobamos que no esté vacía
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"  # Incluimos mayúsculas y acentuadas
    ultimo_caracter = frase[-1]  # Obtenemos el último carácter
    
    if ultimo_caracter in vocales:
        print(frase + "!")
    else:
        print(frase)
else:
    print("Escribí una frase")