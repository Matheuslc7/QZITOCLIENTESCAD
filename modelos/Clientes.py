from modelos.avaliacao import Avaliacao

class Cliente:

    clientes = []

    def __init__(self, nome, cidade):
        self._nome = nome.title()
        self._cidade = cidade.title()
        self._ativo = False
        self._avaliacao = []
        Cliente.clientes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._cidade}'
    
    @classmethod
    def listar_clientes(cls):
        print( f"\n{'Nome do cliente'.ljust(25).rjust(35)} | {'Cidade'.ljust(25).rjust(35)} | {'Total comprado'.ljust(25).rjust(35)} | {'Status'.rjust(10)} \n")
        for cliente in cls.clientes:
            print(f'{cliente._nome.ljust(25).rjust(35)} | {cliente._cidade.ljust(25).rjust(35)} | {str(cliente.total_compra).ljust(25).rjust(35)} | {cliente.ativo.ljust(15).rjust(20)}\n')

    @property
    def ativo(self):
        return 'Ativo ✔️' if self._ativo else 'Desativado ❌'
    
    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, vendedor, quantidade_compra):
        avaliacao = Avaliacao(vendedor, quantidade_compra)
        self._avaliacao.append(avaliacao)

    @property
    def total_compra (self):
        if not self._avaliacao:
            return 0
        soma_quantidade = sum(avaliacao._quantidade_compra for avaliacao in self._avaliacao)
        return soma_quantidade


