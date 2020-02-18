#Questão 2

dias = {"1":"domingo","2":"Segunda","3":"Terça", "4":"Quarta","5":"Quinta","6":"Sexta","7":"Sábado"}

num = input("escolha um dia: ")
if int(num) <=7:
    print(dias.get(num))
else:
    print("dia invalido")



