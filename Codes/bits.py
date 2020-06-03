from math import trunc                                # Importa uma funcao para pegar a parte inteira de numero

Precisao = int(input('''
[1] Precisão simples
[2] Precisão dupla
Escolha: '''))

if (Precisao == 1):
    x = 23
elif (Precisao == 2):
    x = 52
else:
    Precisao = int(input('''
Tente novamente!
[1] Precisão simples
[2] Precisão dupla
Escolha: '''))

n = float(input("Numero: "))                            # Número que quer converter para binario
cont = 0
inteiro = bin(trunc(n))                                 # Pega binario correspondente da parte inteira do numero
numBinDec = []                                          # Lista para guardar a parte decimal do numero
decimal = n % 1                                         # Pega a parte decimal do numero

while True:                                             # Entra em "loop infinito"
    cont += 1                                           # contador para mantiçar caso entre em um loop
    bit = decimal * 2                                   # Multiplica por 2, e guarda o resultado
    numBinDec.append(trunc(bit))                        # Guarda na lista a parte inteira do numero
    decimal = bit % 1                                   # Pega a parte decimal do numero
    if (cont == x):                                     # Testa o contador é igual a complemnto
        break                                           # Sai do "loop infinito"
    elif (decimal == 0):                                # Testa o numero tem um binario simples
        for c in range(cont, x):                        
            numBinDec.append(0)                         # Adicionar mais (precisão - contador) zeros
        break                                           # Sai do "loop infinito"

print(f"O número é {inteiro[2:]}", end = " ")
for p in numBinDec:
    print(f"{p}", end = "")
    
input("\nPressione ENTER para cintinuar...")