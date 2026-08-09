# 1. Crie uma função que será responsável por exibir o menu do sistema com as opções: cadastro, pesquisa e remoção de cadastro e sair.

# 2. Crie um loop while que será responsável por exibir as opções de sistema enquanto o usuário não escolher a opção '4. Sair'.

# 3. Crie uma variável que ficará responsável por receber a opção de menu escolhida pelo usuário.

# 4. Crie uma estrutura condicional para tornar o menu criado funcional. Utilize prints para simular as escolhas do menu.

# 5. Faça o encerramento do programa se o usuário escolher a opção '4. Sair'.

# 6. Criar um dicionário vazio que será responsável por armazenar os contatos.

# 7. Crie uma função que será responsável por adicionar contatos ao dicionário criado no passo anterior. Campos para o contato: nome, telefone, email, endereço.

# 8. Crie uma função que será responsável por consultar um contato. Caso este contato exista seus dados deverão sermostrados no console.

# 9. Crie uma função responsável por remover um contato.

def exibir_menu():
  print("\nMenu:\n")
  print("1. Cadastrar contato")
  print("2. Consultar contato")
  print("3. Remover contato")
  print("4. Sair")


def adicionar_contato(contatos):
  print("\nDados para o novo contato:")
  nome = input("Nome: ")
  telefone = input("Telefone: ")
  email = input("E-mail: ")
  endereco = input("Endereço: ")

  contatos[nome] = {
    "telefone": telefone,
    "email": email,
    "endereco": endereco
  }

  print("\nO contato foi salvo com sucesso!")


def consultar_contato(contatos):
  nome_pesquisa = input("\nDigite um nome para pesquisar: ")

  if nome_pesquisa in contatos:
    print(f"\nNome: {nome_pesquisa}")
    print(f"Telefone: {contatos[nome_pesquisa]['telefone']}")
    print(f"E-mail: {contatos[nome_pesquisa]['email']}")
    print(f"Endereço: {contatos[nome_pesquisa]['endereco']}")
  else:
    print("\nContato não encontrado! Tente novamente.")


def remover_contato(contatos):
  nome_remocao = input("\nDigite o nome do contato que deseja remover: ")

  if nome_remocao in contatos:
    del contatos[nome_remocao]
    print("\nO contato foi removido com sucesso!")
  else:
    print("\nContato não encontrado. Tente novamente!")

continuar_execucao = True

contatos = {}

while continuar_execucao:
  exibir_menu()
  opcao_escolhida_menu = input("\nDigite uma opção: ")

  if opcao_escolhida_menu == "1":
    adicionar_contato(contatos)
  elif opcao_escolhida_menu == "2":
    consultar_contato(contatos)
  elif opcao_escolhida_menu == "3":
    remover_contato(contatos)
  elif opcao_escolhida_menu == "4":
    continuar_execucao = False
    print("\nPrograma finalizado com sucesso!")
  else:
    print("\nOpção inválida. Tente novamente!")
