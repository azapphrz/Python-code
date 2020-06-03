from math import trunc                                # Importa uma funcao para pegar a parte inteira de numero
prec = int(input("Quantas casas decimais de precisao? "))
complemento = int(input(
'''[1]Complemento simples
[2]Complemento complexo
Escolha: '''))

if (complemento == 1):
    x = 23
elif (complemento == 2):
    x = 52
else:
    complemento = int(input(''' Tente novamente!
[1] Complemento simples
[2] Complemento duplo
Escolha: '''))

n = float(input("Numero: "))                            # Número que quer converter para binario
cont = 0
inteiro = bin(trunc(n))                                 # Pega binario correspondente da parte inteira do numero
numBinDec = []                                          # Lista para guardar a parte decimal do numero
decimal = round(n % 1, prec)                            # Pega a parte decimal do numero, com n casas decimais

while True:                                             # Entra em "loop infinito"
    cont += 1                                           # contador para mantiçar caso entre em um loop
    bit = round(decimal * 2, prec)                      # Multiplica por 2, e guarda o resultado com 6 casas decimais
    numBinDec.append(trunc(bit))                        # Guarda na lista a parte inteira do numero
    decimal = round(bit % 1, prec)                      # Pega a parte decimal do numero, com n casas decimais
    if (cont == x):                                     # Testa o contador é igual a complemnto
        break                                           # Sai do "loop infinito"
    elif (decimal == 0):                                # Testa o numero tem um binario simples
        for c in range(cont, x):                        
            numBinDec.append(0)                         # Adicionar mais (complemento - contador) zeros
        break                                           # Sai do "loop infinito"

print(f"O número é {inteiro[2:]}", end = " ")
for p in numBinDec:
    print(f"{p}", end = "")
