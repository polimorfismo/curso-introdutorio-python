# 1. importar o móduo random
import random

# 2. exibir uma mensagem de saudação para o jogador
print("Seja bem vindo ao jogo 'Adivinhe o número'\n")

# 3. sortear um número aleatório entre 1 e 100
numero_sorteado = random.randint(1, 100)

# 4. crie um loop while que deverá perguntar um palpite de número para o jogador, até que ele acerte o número sorteado. Se o jogador acertar o número informe sobre o acerto e finalize o jogo. Se ele errar diga que o palpite está incorreto e também se ele está quente (quando o palpite estiver até cinco posições acima ou abaixo do número) ou frio (quando o palpite estiver mais de cinco posições acima ou abaixo do número).

palpite = 0

while palpite != numero_sorteado:
  # Recebe o palpite de número do jogador
  palpite = int(input("Digite um palpite para ver se adivinha o número sorteado: "))

  # Verificações condicionais
  if palpite < numero_sorteado:
    diferenca = numero_sorteado - palpite
    if diferenca <= 5:
      print("Você errou o número, mas está quente!")
    else:
      print("Você errou o número e está frio!")

  elif palpite > numero_sorteado:
    diferenca = palpite - numero_sorteado
    if diferenca <= 5:
      print("Você errou o número, mas está quente!")
    else:
      print("Você errou o número e está frio!")

  else:
    print(f"Você venceu! O número sorteado foi o número: {numero_sorteado}")
