from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

        def __str__(self):
            return f'{self.nome} | {self.preco} | {self.descricao}'

arroz = Prato('Arroz', '10', 'o mais melhor de tudim')
print(arroz)