import os
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

class MenuRestaurante:
    def __init__(self):
        self.logo = """
        
fernando viadinho 
        """
        self.opcoes = [
            "Cadastrar restaurante",
            "Listar restaurantes",
            "Alternar estado do restaurante",
            "Adicionar avaliação",
            "Adicionar item ao cardápio",
            "Exibir cardápio",
            "Sair"
        ]

    def exibir(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(self.logo)
        for i, opcao in enumerate(self.opcoes, 1):
            print(f"{i}. {opcao}")
        
    def finalizar_app(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Encerrando o programa...')

def main():
    menu = MenuRestaurante()
    
    while True:
        menu.exibir()
        try:
            opcao_escolhida = int(input("\nEscolha uma opção: "))

            if opcao_escolhida == 1:
                print("\n--- Cadastro de Restaurante ---")
                nome = input("Nome do restaurante: ")
                categoria = input("Categoria: ")
                Restaurante(nome, categoria)
                print(f"Restaurante: {nome} cadastrado com sucesso!")
            
            elif opcao_escolhida == 2:
                Restaurante.listar_restaurantes()
            
            elif opcao_escolhida == 3:
                print("\n--- Alternar Estado ---")
                nome_restaurante = input("Digite o nome do restaurante: ")
                encontrado = False
                for restaurante in Restaurante.restaurantes:
                    if restaurante._nome.upper() == nome_restaurante.upper():
                        restaurante.alternar_estado()
                        encontrado = True
                        print(f"O estado do restaurante: {nome_restaurante} foi alterado.")
                if not encontrado: print("Restaurante não encontrado.")

            elif opcao_escolhida == 4:
                print("\n--- Adicionar Avaliação ---")
                nome_restaurante = input("Nome do restaurante: ")
                encontrado = False
                for restaurante in Restaurante.restaurantes:
                    if restaurante._nome.upper() == nome_restaurante.upper():
                        encontrado = True
                        cliente = input("Seu nome: ")
                        try:
                            nota = float(input(f"Nota (1 a 5) para {nome_restaurante}: "))
                            restaurante.receber_avaliacao(cliente, nota)
                            print(f"Avaliação registrada!")
                        except ValueError: print("Erro: Nota inválida.")
                if not encontrado: print("Restaurante não encontrado.")

            elif opcao_escolhida == 5:
                print("\n--- Adicionar Item ao Cardápio ---")
                nome_restaurante = input("Nome do restaurante: ")
                encontrado = False
                for restaurante in Restaurante.restaurantes:
                    if restaurante._nome.upper() == nome_restaurante.upper():
                        encontrado = True
                        print("1 - Prato | 2 - Bebida")
                        tipo = input("Opção: ")
                        nome_item = input("Nome do item: ")
                        try:
                            preco_item = float(input("Preço: ").replace(',', '.'))
                            if tipo == '1':
                                desc = input("Descrição: ")
                                restaurante.adicionar_no_cardapio(Prato(nome_item, preco_item, desc))
                            elif tipo == '2':
                                tam = input("Tamanho: ")
                                restaurante.adicionar_no_cardapio(Bebida(nome_item, preco_item, tam))
                            print("Item adicionado!")
                        except ValueError: print("Erro: Preço inválido.")
                if not encontrado: print("Restaurante não encontrado.")

            elif opcao_escolhida == 6:
                print("\n--- Exibir Cardápio ---")
                nome_restaurante = input("Nome do restaurante: ")
                encontrado = False
                for restaurante in Restaurante.restaurantes:
                    if restaurante._nome.upper() == nome_restaurante.upper():
                        restaurante.exibir_cardapio()
                        encontrado = True
                if not encontrado: print("Restaurante não encontrado.")

            elif opcao_escolhida == 7:
                menu.finalizar_app()
                break
            else: print("Opção inválida!")

            input("\nPressione Enter para continuar...")
        except ValueError:
            print("Erro: Digite um número.")
            input("\nPressione Enter para tentar novamente...")

if __name__ == '__main__':
    main()