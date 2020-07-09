from Modulos.cadastro import *
from Modulos.arquivo import *
from time import sleep


def chamaPrograma():
    while True:
        cabecalho(sit=True)
        x = leiaInt("\033[0;33mDigite um opção: \033[m")
        if (0 < x < 4):
            opcoes(x)
            if (x == 3):
                break
        else:
            print("\033[0;31mERRO: Digite um valor valido!.\033[m")

        sleep(1)


def opcoes(x):
    if (x == 1):
        pessoasCadastradas()
    elif(x == 2):
        cadastrarPessoa()
    elif (x == 3):
        sairSistema()