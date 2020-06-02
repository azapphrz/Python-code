from math import trunc                  # Importa uma funcao para pegar a parte inteira de numero

n = float(input("Numero: "))            # Número que quer converter para binario
cont = 0
inteiro = bin(trunc(n))                 # Pega binario correspondente da parte inteira do numero
numBinDec = []                          # Lista para guardar a parte decimal do numero
decimal = round(n % 1, 6)               # Pega a parte decimal do numero, com 6 casas decimais

while True:                             # Entra em "loop infinito"
    cont += 1                           # contador para mantiçar caso entre em um loop
    bit = round(decimal * 2, 6)         # Multiplica por 2, e guarda o resultado com 6 casas decimais
    numBinDec.append(trunc(bit))        # Guarda na lista a parte inteira do numero
    decimal = round(bit % 1, 6)         # Pega a parte decimal do numero, com 6 casas decimais
    if (cont == 52) or (decimal == 0):  # Testa o contador é igual a mastiçar maxima ou se o o numero tem um binario simples
        numBinDec.append(0)             # Adicionar mais um 0
        break                           # Sai do "loop infinito"

print(f"O número é {inteiro[2:]}", end = " ")
for p in numBinDec:
    print(f"{p}", end = "")
