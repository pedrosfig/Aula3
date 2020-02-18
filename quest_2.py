#Questão 2

dias = {"1":"domingo","2":"Segunda","3":"Terça"}

num = input("escolha um dia: ")
if int(num) <=3:
    print(dias.get(num))
else:
    print("dia invalido")



