# 1. Faça a importação do módulo random no projeto
import random

# Faces dos dados
dado_face1 = """
 _______
|       |
|   ●   |
|       |
|_______|
"""

dado_face2 = """
 _______
| ●     |
|       |
|     ● |
|_______|
"""

dado_face3 = """
 _______
| ●     |
|   ●   |
|     ● |
|_______|
"""

dado_face4 = """
 _______
| ●   ● |
|       |
| ●   ● |
|_______|
"""

dado_face5 = """
 _______
| ●   ● |
|   ●   |
| ●   ● |
|_______|
"""

dado_face6 = """
 _______
| ●   ● |
| ●   ● |
| ●   ● |
|_______|
"""

# 2. Crie uma lista que possui todas as faces do dado
dados_faces = [dado_face1, dado_face2, dado_face3, dado_face4, dado_face5, dado_face6]

# 3. Mostre uma mensagem de boas vindas e um resumo de como o jogo funciona para o usuário
print("Seja bem-vindo ao jogo de dados!\n")
print("Instruções: Cada usuário joga três dados na mesa de uma única vez. O ganhador é quem possuir o maior valor obtido da soma dos três dados.\n")

# 4. Exiba uma mensagem solicitando que o usuário digite a letra J e pressione enter para jogar seus dados na mesa
input("O jogo vai começar. Digite a letra 'J' para jogar seus dados na mesa: ")

# 5. Gerar três números aleatórios para cada dado jogado pelo usuário na mesa e armazene-os em uma lista
numero1_usuario = random.randint(1, 6)
numero2_usuario = random.randint(1, 6)
numero3_usuario = random.randint(1, 6)
lista_numeros_usuario = []
lista_numeros_usuario.extend([numero1_usuario, numero2_usuario, numero3_usuario])

# 6. Exiba os valores obtidos para o usuário
print("\nOs seus dados caíram nos números:")
print(dados_faces[numero1_usuario - 1] + dados_faces[numero2_usuario - 1] + dados_faces[numero3_usuario - 1])

# 7. Exibir uma mensagem dizendo que o computador vai jogar os dados. Na sequência, gerar os números aleatórios para o computador, armazená-los em uma lista
print("\nO computador vai jogar os dados...")
print("\nOs dados do computador caíram nos números:")
numero1_computador = random.randint(1, 6)
numero2_computador = random.randint(1, 6)
numero3_computador = random.randint(1, 6)
lista_numeros_computador = []
lista_numeros_computador.extend([numero1_computador, numero2_computador, numero3_computador])

# 8. Mostrar os números obtidos para o computador
print(dados_faces[numero1_computador - 1] + dados_faces[numero2_computador - 1] + dados_faces[numero3_computador - 1])

# 9. Utilizar as listas e os índices para calcular o total de pontos de cada jogador através da soma dos valores obtidos nos três dados
# Total de pontos usuário
total_pontos_usuario = lista_numeros_usuario[0] + lista_numeros_usuario[1] + lista_numeros_usuario[2]

# Total de pontos computador
total_pontos_computador = lista_numeros_computador[0] + lista_numeros_computador[1] + lista_numeros_computador[2]

# 10. Utilize condicionais para imprimir o resultado do jogo
# Empate
if total_pontos_usuario == total_pontos_computador:
  print("\nO jogo terminou empatado!")
  print(f"\nTotal de pontos usuário: {total_pontos_usuario} x Total de pontos computador: {total_pontos_computador}")
# Usuário vence
elif total_pontos_usuario > total_pontos_computador:
  print("\nVocê venceu!")
  print(f"\nTotal de pontos usuário: {total_pontos_usuario} x Total de pontos computador: {total_pontos_computador}")
# Computador vence
else:
  print("\nO computador venceu!")
  print(f"\nTotal de pontos usuário: {total_pontos_usuario} x Total de pontos computador: {total_pontos_computador}")
