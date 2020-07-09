from Modulos.sistema import *
from Modulos.arquivo import *


def pessoasCadastradas():
    x = chamaArq()
    if not arqExiste(x):
        criarArq(x)
    lerArq(x)    


def cadastrarPessoa():
    cabecalho(msg="NOVO CADASTRO")
    nome = str(input("\033[0;36mNome: \033[m"))
    idade = leiaInt("Idade: ")
    cadastrar(chamaArq(), nome, idade)


def sairSistema():
    cabecalho(msg='OBRIGADO! VOLTE LOGO')