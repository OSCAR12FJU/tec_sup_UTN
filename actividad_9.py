# Solicitamos la magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto (escala de Richter): "))

# Clasificamos el terremoto según su magnitud
if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"

# Mostramos el resultado
print(f"\nPara una magnitud de {magnitud} en la escala de Richter:")
print(f"Clasificación: {categoria}")