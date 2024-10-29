'''
Sistema de Evacuação de Prometeus:
No filme "Prometheus", a tripulação precisa ser evacuada rapidamente.
Crie um programa que simule a contagem regressiva para a evacuação, onde o tempo inicial é
definido pelo usuário e cada "segundo" é mostrado na tela até que a contagem atinja zero.
'''
print("Exercício 5 - Sistema de Evacuação de Prometeus.")
inicial = int(input("Quanto tempo, em segundos, falta para a evacuação? "))
tempo = list(range(inicial, 0, -1)) #lista em ordem decrescente
indice = 0
while indice < len(tempo): #len = retorna o número de itens em um objeto
    if tempo[indice]== 1:
        print(f"Tempo restante: {tempo[indice]} segundo.")
    else:
        print(f"Tempo restante: {tempo[indice]} segundos.")
    indice += 1
print("Tempo esgotado!")