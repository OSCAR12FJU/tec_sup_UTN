Copy
from statistics import mode, median, mean
import random

# Generamos la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calculamos las medidas estadísticas
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Determinamos el tipo de sesgo
if media > mediana > moda:
    sesgo = "positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "negativo (a la izquierda)"
else:
    sesgo = "sin sesgo (distribución simétrica)"

# Mostramos los resultados
print(f"Lista generada: {numeros_aleatorios}\n")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media:.2f}\n")  # Mostramos la media con 2 decimales
print(f"La distribución tiene un sesgo {sesgo}.")