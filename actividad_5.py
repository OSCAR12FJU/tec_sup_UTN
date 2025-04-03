#Solicitamos el valor para hacer la incialización
inputContraseña = input("Ingresa tu edad")


#Ponemos una verificación simmple para ver si al variable esta incializada y pasamos hacer la conparación.
if inputContraseña and len(inputContraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")