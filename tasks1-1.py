'''
Contagem de Estrelas:
Escreva um programa que simule a contagem de estrelas em uma constelação.
O usuário deve inserir quantas estrelas deseja contar e o programa deve mostrar cada contagem até alcançar o número desejado.
'''
print("Exercício 1 - Contagem de Estrelas.")
quantidade = int(input("Quantas estrelas deseja contar? "))
for numero in range(1, quantidade + 1):
  print(numero)