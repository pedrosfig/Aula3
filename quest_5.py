
#Questão 5
import math as mt

def circulo(raio):
    texto = str(raio)
    if texto.isnumeric():
        A = float(texto) * mt.pi**2
        C = 2 * mt.pi * float(texto)
        resposta = "Círculo de raio " +texto + " terá área igual a " + str(round(A,2)) + " e perímetro igual a " + str(round(C,2))
        return resposta
    else:
        return "passar valor numérico"

x = "cinco"
print(circulo(x))


y = 10
print(circulo(y))
