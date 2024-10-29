'''
Escala Richter em Marte:
Marte tem terremotos, ou "marsquakes".
Escreva um programa que permita ao usuário inserir a magnitude de marsquakes por 30 dias consecutivos e identifique o dia com o marsquake mais forte.
'''
print("Exercício 4 - Escala Richter em Marte.")
magnitudes = []
for dia in range(1, 5):
    magnitude = float(input(f"Insira a magnitude do marsquake no dia {dia}: "))
    magnitudes.append(magnitude) #.append = adicionar um item ao final de uma lista
maior = max(magnitudes)
forte = magnitudes.index(maior) + 1 #.index = encontrar o índice da primeira ocorrência do valor maior na lista magnitudes
'''
perguntas para fazer ao marcio sobre o código:
se tiver mais de um dia com o mesmo valor de 'maior', na saída terá o primeiro dia em que essa magnitude máxima ocorreu, pois o método '.index' sempre retorna o índice da primeira ocorrência do valor especificado.
Como faz para ter na saída todos os dias?
'''
print(f"O dia com o marsquake mais forte foi no dia {forte} com a magnitude de {maior}.")