from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self.cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        if not cls.restaurantes:
            print("\n" + "="*55)
            print("Atenção: Nenhum restaurante cadastrado no momento.")
            print("="*55)
            return

        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(15)} | {'Avaliação'}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(15)} | {str(restaurante.media_avaliacoes)}")

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        
        soma_das_notas = sum(getattr(avaliacao, '_nota', getattr(avaliacao, 'nota', 0)) for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self.cardapio.append(item)

    def exibir_cardapio(self):
        print(f'\nCardápio do restaurante {self._nome}\n')
        if not self.cardapio:
            print("O cardápio está vazio.")
            return

        for i, item in enumerate(self.cardapio, start=1):
            
            nome = getattr(item, '_nome', getattr(item, 'nome', 'Item sem nome'))
            preco = getattr(item, '_preco', getattr(item, 'preco', 0.0))

            if hasattr(item, 'descricao'):
                mensagem = f'{i}. Nome: {nome.ljust(20)} | Preço: R${str(preco).ljust(10)} | Descrição: {item.descricao}'
                print(mensagem)
            else:
                
                tamanho = getattr(item, 'tamanho', 'N/A')
                mensagem = f'{i}. Nome: {nome.ljust(20)} | Preço: R${str(preco).ljust(10)} | Tamanho: {tamanho}'
                print(mensagem)