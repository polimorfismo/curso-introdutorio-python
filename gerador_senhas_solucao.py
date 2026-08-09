# 1. Importar o módulo random
import random

letras = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 2. Mostre uma mensagem de boas vindas para o usuário
print("Seja bem-vindo ao Gerador de Senhas!\n")

# 3. Pergunte ao usuário quantas letras ele deseja que a senha possua e armazene em uma variável
qtd_letras = int(input("Quantas letras você quer que sua senha possua? "))

# 4. Pergunte ao usuário quantos símbolos ele deseja que a senha possua e armazene em uma variável
qtd_simbolos = int(input("Quantos símbolos você quer que sua senha possua? "))

# 5. Pergunte ao usuário quantos números ele deseja que a senha possua e armazene em uma variável
qtd_numeros = int(input("Quantos números você quer que sua senha possua? "))

# 6. Criar uma lista para armazenar todos os caracteres de senha gerados
senha_lista = []

# 7. Criar um loop que percorra o intervalo entre 1 e o total de letras definido pelo usuário. A cada vez que o loop for executado sortear uma letra com o módulo random e armazená-la na lista.
for caractere in range(1, qtd_letras + 1):
  senha_lista.append(random.choice(letras))

# 8. Criar um loop que percorra o intervalo entre 1 e o total de símbolos definido pelo usuário. A cada vez que o loop for executado sortear um símbolo com o módulo random e armazená-la na lista.
for caractere in range(1, qtd_simbolos + 1):
  senha_lista.append(random.choice(simbolos))

# 9. Criar um loop que percorra o intervalo entre 1 e o total de números definido pelo usuário. A cada vez que o loop for executado sortear um número com o módulo random e armazená-la na lista.
for caractere in range(1, qtd_numeros + 1):
  senha_lista.append(random.choice(numeros))

# 10. Embaralhar os caracteres armazenados na lista
random.shuffle(senha_lista)

# 11. Criar uma variável para receber uma string concatenada
senha = ""

# 12. Percorrer cada posição da lista e concatená-las. Os valores deverão ser salvos na variável criada no passo anterior.
for caractere in senha_lista:
  senha += caractere

# 13. Imprimir a senha no console
print(f"\nSua senha é: {senha}")
