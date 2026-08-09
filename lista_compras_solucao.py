# 1. Crie uma função para exibir o menu no console. O menu deve possuir as seguintes opções: adicionar item, remover item, visualizar lista e sair.

# 2. Crie uma função que será responsável por executar o programa. Nesse passo, ainda não é necessário adicionar nada na estrutura da função.

# 3. Crie uma variável dentro do método responsável por executar o programa (passo 2), para controlar se o usuário deseja continuar ou sair do programa. O valor inicial dessa variável deve ser True.

# 4. Crie um loop while para manter a exibição do menu na tela enquanto o usuário não selecionar a opção 'sair do sistema'. Use a variável criada no passo 3 como condição de execução do loop while.

# 5. Crie a estrutura condicional que será responsável por acionar cada opção do menu. Caso o usuário digite uma opção que não está no menu, deverá ser exibida uma mensagem de opção inválida.

# 6. Se o usuário escolher a opção 4 (sair do gerenciador de compras), o loop while deverá ser encerrado e uma mensagem informando que o programa foi finalizado deverá ser exibida no console.

# 7. Crie uma lista inicialmente vazia, que será responsável por armazenar os itens da lista de compras.

# 8. Crie uma função que permita adicionar um item na lista. Essa função deverá receber como argumento a lista que foi criada no passo 7. Crie dois inputs para receber os dados do usuário. Um vai receber o 'item' e o outro a 'quantidade'.

# 9. Crie uma função que faça a impressão de todos os itens da lista na tela. Se a lista estiver vazia informe isso ao usuário. Estude também uma forma de mostrar o índice de cada item na lista junto com o valor da posição (Exemplo: - 0: Arroz).

# 10. Crie uma função que permita a remoção de um item da lista (Pesquise sobra a função pop() para a remoção do item). Inclua uma chamada para a função de visualização dos itens da lista para que o usuário veja e escolha o índice do item que deseja excluir.

# 11. Importe o módulo 'logo' e utilize a logo_lista_de_compras para mostrar a logomarca do programa antes de exibir o menu.

# Logo
# logo_lista_de_compras = """
#  _     _     _              _        _____                                     
# | |   (_)   | |            | |      /  __ \                                    
# | |    _ ___| |_ __ _    __| | ___  | /  \/ ___  _ __ ___  _ __  _ __ __ _ ___ 
# | |   | / __| __/ _` |  / _` |/ _ \ | |    / _ \| '_ ` _ \| '_ \| '__/ _` / __|
# | |___| \__ \ || (_| | | (_| |  __/ | \__/\ (_) | | | | | | |_) | | | (_| \__ \

# \_____/_|___/\__\__,_|  \__,_|\___|  \____/\___/|_| |_| |_| .__/|_|  \__,_|___/
#                                                           | |                  
#                                                           |_|                  
# """

# ATENÇÃO! Lembre-se de criar o arquivo logo.py com a estrutura da logo
import logo

def exibir_menu():
    print(logo.logo_lista_de_compras)
    print("Menu:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista de compras")
    print("4. Sair")


def adicionar_item(lista):
    item = input("\nDigite o item a ser adicionado: ")
    quantidade = int(input("\nDigite a quantidade: "))
    lista.append(f"{item} (Quantidade: {quantidade})")
    print(f"\nO item '{item}' foi cadastrado com sucesso!")


def visualizar_itens(lista):
    if not lista:
        print("\nA lista de compras está vazia.")
    else:
        print("\nLista de compras:")
        for item in range(len(lista)):
            print(f"- {item}: {lista[item]}")


def remover_item(lista):
    visualizar_itens(lista)
    if lista:
        item_para_remover = int(input("\nDigite o código do item que deseja remover: "))
        item_removido = lista.pop(item_para_remover)
        print(f"\nO item '{item_removido}' foi removido com sucesso.")


def executar_programa():
    lista_compras = []
    
    continuar = True

    while continuar:

        exibir_menu()

        escolha = input("\nEscolha uma opção do menu: ")
        
        if escolha == "1":
            adicionar_item(lista_compras)
        elif escolha == "2":
            remover_item(lista_compras)
        elif escolha == "3":
            visualizar_itens(lista_compras)
        elif escolha == "4":
            continuar = False
            print("\nO programa foi encerrado.")
        else:
            print("\nOpção inválida. Por favor, tente novamente.")


executar_programa()
