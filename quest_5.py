
#Questão 5
import math as mt

def circulo(raio):
    texto = str(raio)
    if texto.isnumeric():
        A = raio * mt.pi**2
        C = 2 * mt.pi * raio
        resposta = "Círculo de raio " +texto + " terá área igual a " + str(round(A,2)) + " e perímetro igual a " + str(round(C,2))
        return resposta
    else:
        return "passar valor numérico"

x = "cinco"
print(circulo(x))


y = 10
print(circulo(y))





def circulo2(raio):
    try:
        float(raio)
    except:
        raio = 0
        print("Valor não numerico passado.")
    A = raio * mt.pi**2
    C = 2 * mt.pi * raio
    resposta = "Círculo de raio " +str(raio) + " terá área igual a " + str(round(A,2)) + " e perímetro igual a " + str(round(C,2))
    return resposta


x = "cinco"
print(circulo2(x))


y = 10
print(circulo2(y))
