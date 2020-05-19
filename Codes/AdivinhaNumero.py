from random import randint

print("-=-" * 14)
print("\033[1;44m PENSEI EM UM NÚMERO, TENTE ADIVINHAR!!! \033[m")
print("-=-" * 14)

cont =0 
n = 11
nc = randint(0,10)
while nc != n:
    n = int(input("Digite um número entre 0 e 10: "))
    cont += 1
    if n > nc:
        print("Menos... tente de novo!")
    elif n < nc:
        print("Mais... tente de novo")

print(f"O computador pensou no número {nc} e você precisou de {cont} tentativas para acertar")