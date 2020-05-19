from random import choice   # Importa um random para as opções
from time import sleep 

print("-=-" * 8)
print("\033[1;44m VAMOS JOGAR JOKENPÔ!!! \033[m")
print("-=-" * 8)
novaJogada = ""

while novaJogada != "n":   # Executa o programa n vezes
    lista = ["Pedra", "Papel", "Tesoura"]   # Cria um vetor com as opções possíveis
    escolhaPC = choice(lista)   # Escolhe umas da opções do vetor

    escolha = input("Escolha entre pedra, papel e tesoura: ").strip().lower()

    print("\033[1;34mJO") 
    sleep(1)
    print("KEN")
    sleep(1)
    print("JÔ\033[m")
    sleep(1)

# Faz as comparações para ver quem ganhou
    if (escolha == "pedra"):
        if (escolhaPC == "Pedra"):
            print("\033[1;40m EMPATE!!!!! \033[m")
        elif (escolhaPC == "Papel"):
            print("\033[1;41m VOCÊ PERDEU!!!!! \033[m")
        elif (escolhaPC == "Tesoura"):
            print("\033[1;42m VOCÊ GANHOU!!!!! \033[m")

    elif (escolha == "papel"):
        if ( escolhaPC == "Papel"):
            print("\033[1;40m EMPATE!!!!! \033[m")
        elif (escolhaPC == "Tesoura"):
            print("\033[1;41m VOCÊ PERDEU!!!!! \033[m")
        elif (escolhaPC == "Pedra"):
            print("\033[1;42m VOCÊ GANHOU!!!!! \033[m")

    elif (escolha == "tesoura"):
        if (escolhaPC == "Tesoura"):
            print("\033[1;40m EMPATE!!!!! \033[m")
        elif (escolhaPC == "Pedra"):
            print("\033[1;41m VOCÊ PERDEU!!!!! \033[m")
        elif(escolhaPC == "Papel"):
            print("\033[1;42m VOCÊ GANHOU!!!!! \033[m")
    else:
        print("Opção invalida! Tente novamente")
        escolha = input("Escolha entre pedra, papel e tesoura: ").strip().lower()
        print("\033[1;34mJO") 
        sleep(1)
        print("KEN")
        sleep(1)
        print("JÔ\033[m")
        sleep(1)

    print(f"O computador escolheu {escolhaPC} e você escolheu {escolha}")
    novaJogada = input("Deseja continuar? [S/N]: ").strip().lower()[0]
