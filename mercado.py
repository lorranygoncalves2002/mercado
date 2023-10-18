from typing import List,Dict
from time import sleep

from models.produto import produto
from utils.helper import formata_float_str_moeda

produtos: list[produto]
carrinho:[dict[produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('=' *15)
    print('escolha sua opção')
    print('1 - Cadastrar Produto')
    print('2 - Comprar Produto')
    print('3 -  Sair')
    print('=' * 15)
    opcao = int(input('Opção:'))

    if opcao == 1:
         cadastrar_produto
    elif opcao == 2:
         comprar_produto
    else:
         print('volte sempre')
         sleep(5)
         exit(0)

def cadastrar_produto() -> None:
    pass

def comprar_produto() -> None:
    pass

def visualizar_carrinho() -> None:
    pass

def fechar() -> None:
    pass

if __name__=='__main__':
    main()