# Importar os módulos
import random
import logo

# Definir as constantes responsáveis por armazenar os níveis de jogo (fácil, moderado e dificil)
NIVEL_FACIL = 10
NIVEL_MODERADO = 5
NIVEL_DIFICIL = 2

# Criar função para gerar um número aleatório
def gerar_numero():
  return random.randint(1,100)

# Criar função para permitir a escolha do nível de dificuldade de jogo
def escolher_dificuldade():
  nivel = input("Escolha uma dificuldade. Digite 'facil', 'moderado' ou 'dificil': ")
  if nivel == "facil":
    return NIVEL_FACIL
  elif nivel == "moderado":
    return NIVEL_MODERADO
  else:
    return NIVEL_DIFICIL
  

# Criar uma função para verificar se o jogador acertou ou não o número
def verificar_tentativa(n_tentativa, n_sorteado, n_jogada):
  if n_tentativa > n_sorteado:
    print("\nErrado! O número que você escolheu é maior que o número sorteado.")
    return n_jogada - 1
  elif n_tentativa < n_sorteado:
    print("\nErrado! O número que você escolheu é menor que o número sorteado.")
    return n_jogada - 1
  else:
    print(f"Você acertou! O número sorteado era realmente o número {n_sorteado}")

# definir uma função principal que será responsável por executar o jogo
def jogar():
  # Mensagens iniciais/saudação
  print(logo.logo_jogo)
  print("Bem-vindo ao jogo Adivinhe o Número!")
  print("Pensei em um número entre 1 e 100, será que você consegue adivinhar?")

  numero_sorteado = gerar_numero()
  print(numero_sorteado)

  quantidade_de_jogadas = escolher_dificuldade()

  numero_tentativa = 0

  print(f"\nO jogo vai começar! Você terá {quantidade_de_jogadas} chances para tentar acertar o número sorteado.")

  while numero_tentativa !=  numero_sorteado:
    print(f"\nQuantidade de tentativas restantes: {quantidade_de_jogadas}")
    numero_tentativa = int(input("Dê o seu palpite: "))
    
    quantidade_de_jogadas = verificar_tentativa(numero_tentativa, numero_sorteado, quantidade_de_jogadas)

    if quantidade_de_jogadas == 0:
      print("\nVocê realizou todas as tentativas e não conseguiu acertar o número sorteado!")
      return
    elif numero_tentativa != numero_sorteado:
      print("Tente novamente.")
      
jogar()
