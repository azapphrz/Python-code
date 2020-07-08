from random import randint
print("VOU TENTAR DESCOBRIR A SENHA DO SEU COFRE!!!")
cont = contTotal = tentativa = 0    # Contador para decobrir a senha
n = int(input("Digite a senha do seu cofre. (000 até 999): "))
# Senha hipotetica 123
n1 = n % 10              # Pega o número na primeira posição, no caso da senha (3)
n2 = n // 10 % 10      # Pega o número na segunda posição, no caso da senha (2)
n3 = n // 100 % 10     # Pega o número na teceira posição, no caso da senha (1)

while True:
    while True:
        c1 = randint(0, 9)
        c2 = randint(0, 9)
        c3 = randint(0, 9)
        cont += 1
        if (c1 == n1) and (c2 == n2) and (c3 == n3):
            break
    print(cont)
    contTotal += cont
    tentativa += 1
    if (cont <= 3):
        break
    if (cont != 3):
        cont = 0
print(f"Sua senha é: {c3} {c2} {c1}") 
print(f"Eu precisei de {contTotal} tentativas para descobrir sua senha")
print(f"Eu precisei de {tentativa} tentativas para para acertar sua senha com até 3 tentativas")