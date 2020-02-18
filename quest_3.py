
#Questão 3
import random as rd

numeros = []
valor = int(input("Escolha quantos numeros: "))
for i in range(0,valor):
    x = int(round(rd.random()*100,0))
    numeros.append(x)
print('Essa foi a lista gerada:')
print(numeros)
    
M = max(numeros)
m = min(numeros)
print('O maior número gerado foi ', str(M), ' e o menor foi ', str(m))
    


