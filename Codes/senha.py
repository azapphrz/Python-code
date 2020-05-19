from random import randint
cont = 0                      # Contador para decobrir a senha
print("VOU TENTAR DESCOBRIR SUA SENHA!!!")
n = int(input("Digite a senha do seu cofre. (0 até 1000000): "))

while True:
    c = randint(0, 1000000)   # Gera um número aleatório entre 0 e 1000000
    cont += 1
    if c == n:                # Testa se o número aleatório que o computador gerou é igual ao que o usuario digitou
        break
print(f"Eu precisei de {cont} tentativas para descobrir sua senha")