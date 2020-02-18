
#Questão 5
import math as mt

raio = input("Raio: ")
if raio.isnumeric:
    A = float(raio) * mt.pi**2
    C = 2 * mt.pi * float(raio)
    print("Círculo de raio ", float(raio), " terá área igual a ", round(A,2), " e perímetro igual a ", round(C,2))
else:
    "passar valor numérico"


