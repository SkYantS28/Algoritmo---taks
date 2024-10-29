'''
Orbitando Saturno:
Crie um programa que simule a quantidade de voltas que uma nave espacial dá em torno de Saturno.
O usuário deve especificar o número de voltas e o programa deve mostrar a cada volta completada.
'''
print("Exercício 2 - Orbitando Saturno.")
quantidade = int(input("Quantas voltas a nave espacial deu em torno de Saturno? "))
for numero in range(1, quantidade + 1):
  if numero == 1:
    print(f"A nave espacial deu {numero} volta em torno de Saturno.")
  else:
    print(f"A nave espacial deu {numero} voltas em torno de Saturno.")