'''
Viagem ao Passado em "Interestelar":
Simule o processo de envelhecimento observado no filme "Interestelar" devido à dilatação do tempo próximo a um buraco negro.
Peça ao usuário para inserir a quantidade de horas passadas próximo ao buraco negro e mostre quantos anos teriam passado na Terra.
'''
print("Exercício 3 - Viagem ao Passado em Interestelar.")
horas = int(input("Quantas horas foram passadas próximo ao buraco negro? "))
terra = horas * 7
if horas == 1:
    print(f"Cada 1 hora próximo ao buraco negro equivale a 7 anos na Terra. Após {horas} hora, já se passaram {terra} anos na Terra.")
else:
    print(f"Cada 1 hora próximo ao buraco negro equivale a 7 anos na Terra. Após {horas} horas, já se passaram {terra} anos na Terra.")