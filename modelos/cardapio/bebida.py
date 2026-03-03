from modelos.cardapio.item_cardapio import ItemCardapio

class  Bebida(ItemCardapio):

    def __init__(self, nome, preco, tamanho):
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho

    def __str__(self):
        return f'{self.nome} | {self.preco} | {self.tamanho}'
    
guarana = Bebida('guaraná', '10', 'o mais melhor')
print(guarana)