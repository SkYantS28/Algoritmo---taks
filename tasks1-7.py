'''
A Viagem de Ulisses:
Baseado na Odisseia, crie um programa onde Ulisses precisa navegar entre várias ilhas representadas por números de 1 a 10.
O usuário define a ordem de visita e o programa deve calcular a distância total percorrida por Ulisses.
'''
print("Exercício 7 - A Viagem de Ulisses.")
print("Ulisses precisa navegar entre várias ilhas representadas por números de 1 a 10.")
print("Você deve definir a ordem de visita. Exemplo: 1 3 5 2")
ordem = []
visita = input("Digite a ordem de visita das ilhas, separadas por espaço: ")
ordem = list(map(int, visita.split()))  #map + int = tranforma em numeros inteiros
for ilha in ordem:
    if ilha < 1 or ilha > 10:
        print(f"Ilha {ilha} inválida! Use números de 1 a 10.")
total = 0
i = 0
while i < len(ordem) - 1:
    atual = ordem[i]
    proxima = ordem[i + 1]
    if atual == proxima:
        distancia = 0
    else:
        distancia = 2 * abs(proxima - atual)
    total += distancia
    i += 1
print(f"A distância total percorrida por Ulisses é: {total} km")