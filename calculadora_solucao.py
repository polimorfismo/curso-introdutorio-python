# 1. Crie quatro funções que serão responsáveis por realizar as operações básicas de cálculo: soma, subtração, multiplicação e divisão. Cada uma dessas operações deverá receber 2 números como argumentos quando chamadas.

# 2. Crie um dicionário chamado operacoes. Esse dicionário deverá fazer uma relação chave/valor de símbolos (+, -, * e /) com os nomes das funções que foram criadas.

# 3. Utilize um input para receber o primeiro número do usuário.

# 4. Crie um loop for para mostrar todas as operações disponíveis para o usuário e na sequência solicite que ele escolha uma das operações.

# 5. Crie um input para receber o segundo número do usuário.

# 6. Faça a chamada para a função de acordo com a operação escolhida pelo usuário. Utilize o 'valor' referente ao operador 'chave' do dicionário para chamar a função.

# 7. Mostre o resultado da operação no console.

def soma(n1,n2):
  return n1 + n2

def subtracao(n1,n2):
  return n1 - n2

def multiplicacao(n1,n2):
  return n1 * n2

def divisao(n1,n2):
  return n1 / n2

operacoes = {
  '+': soma,
  '-': subtracao,
  '*': multiplicacao,
  '/': divisao
}

num1 = int(input("Digite o primeiro número: "))

operacoes_disponiveis = ""
for op in operacoes:
  operacoes_disponiveis = ", ".join(operacoes.keys())

operacao_escolhida = input(f"Digite uma operação ({operacoes_disponiveis}): ")

num2 = int(input("Digite o segundo número: "))

resultado = operacoes[operacao_escolhida](num1,num2)

print(f"\nResultado: {num1} {operacao_escolhida} {num2} = {resultado}")
