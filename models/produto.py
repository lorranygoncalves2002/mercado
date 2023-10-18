#usage
from utils.helper import formata_float_str_moeda
#from pacote.arquivo import funcão

class produto:
    contador: int = 1

    #construtor do objeto
    def __init__(self: object, nome: str, preco:float ) ->None:
        self.__codigo: int = produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        produto.contador += 1

#propriedades define retorno de cada propriedade ao ser chamada
@property
def codigo(self:object) -> int:
    return self.__codigo

@property
def nome(self:object) -> int:
    return self.__nome

@property
def preco(self:object) -> int:
    return self.__preco

def __str(self) -> str:
    return f'codigo{self.codigo} \npreco:{formata_float_str_moeda(self.preco)}'

