'''
Decifrando Mensagens do Espaço:
Escreva um programa que simule a decodificação de mensagens alienígenas.
O usuário deve inserir uma sequência de números representando uma mensagem codificada e o programa deve "decodificar"
esses números ao subtrair o valor anterior do próximo, mostrando a diferença sequencial.
'''
print("Exercício 6 - Decifrando Mensagens do Espaço.")
print("A mensagem codificada, dessa vez, é uma sequência de números, separados por espaço.")
codificada = input("Insira sua mensagem codificada: ")
numeros = codificada.split() #.split = divide uma string em uma lista de substrings (eu amo gatos vira "eu", "amo", "gatos")
mensagem = []
for num in numeros:
    mensagem.append(int(num)) #.append = adicionar um item ao final de uma lista
decodificada = []
for numero in mensagem:
    if numero == 1:
        decodificada.append('a')
    elif numero == 2:
        decodificada.append('b')
    elif numero == 3:
        decodificada.append('c')
    elif numero == 4:
        decodificada.append('d')
    elif numero == 5:
        decodificada.append('e')
    elif numero == 6:
        decodificada.append('f')
    elif numero == 7:
        decodificada.append('g')
    elif numero == 8:
        decodificada.append('h')
    elif numero == 9:
        decodificada.append('i')
    elif numero == 10:
        decodificada.append('j')
    elif numero == 11:
        decodificada.append('k')
    elif numero == 12:
        decodificada.append('l')
    elif numero == 13:
        decodificada.append('m')
    elif numero == 14:
        decodificada.append('n')
    elif numero == 15:
        decodificada.append('o')
    elif numero == 16:
        decodificada.append('p')
    elif numero == 17:
        decodificada.append('q')
    elif numero == 18:
        decodificada.append('r')
    elif numero == 19:
        decodificada.append('s')
    elif numero == 20:
        decodificada.append('t')
    elif numero == 21:
        decodificada.append('u')
    elif numero == 22:
        decodificada.append('v')
    elif numero == 23:
        decodificada.append('w')
    elif numero == 24:
        decodificada.append('x')
    elif numero == 25:
        decodificada.append('y')
    elif numero == 26:
        decodificada.append('z')
    else:
        print("Algo deu errado, reinicie e tente novamente.")
mensdecodificada = ''.join(decodificada)
#.join = concatenar a lista de letras em uma única string sem qualquer delimitador entre as letras.
#'' indicar que não tem caractere separador entre as letras quando forem unidas.
print(f"Mensagem decodificada: {mensdecodificada}")