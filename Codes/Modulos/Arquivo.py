def chamaArq():
    return "cadastroPessoas.txt"
    

def criarArq(nome):
    try:
        x = open(nome, "wt+")
        x.close()
    except:
        print("\033[0;31mHouve um erro na criação do arquivo!\033[m")
    else:
        print(f"Aquivo  {nome}  criado com sucesso!")


def arqExiste(nome):
    try:
        x = open(nome, "rt")
        x.close()
    except FileNotFoundError:
        return False 
    else:
        return True 


def lerArq(nome):
    try:
        x = open(nome, "rt")
    except:
        print("\033[0;31mERRO ao ler o arquivo!\033[m")
    else:
        cabecalho(msg="PESSOAS CADASTRADAS")
        print(x.read())
    finally:
        x.close()

def cadastrar(arq, nome="DESCONHECIDO", idade=0):
    try:
        x = open(arq, "at")
    except:
        print("\033[0;31mHouve um erro na abertura do arquivo\033[m")
    else:
        try:
            x.write(f"{nome:<35} {idade:>3} anos\n")
        except:
            print("\033[0;31mHouve um erro na hora de escrever no arquivo\033[m")
        else:
            print(f"\033[0;33m{nome} foi adicionado com sucesso!\033[m")
            x.close()

            

def linha():
    print('-' * 50)

def cabecalho(msg='MENU PRINCIPAL', sit=False):
    linha()
    print(f"{msg:^50}")
    linha()
    if sit:
        print("\033[0;32m[1] - Para ver pessoas cadastradas\033[m")
        print("\033[0;32m[2] - Para cadastrar uma nova pessoa\033[m")
        print("\033[0;32m[3] - Sair do prongrama\033[m")
        linha()

def leiaInt(msg):

    while True:
        try:
            n = int(input(f"\033[0;36m{msg}\033[m"))
            break
        except (ValueError, TypeError):    
            print("\033[0;31mERRO: Digite um valor valido!.\033[m")
        except KeyboardInterrupt:
            print("\033[0;31mPrograma interronpido pelo usúario.\033[m")
            return 0

    return n