# Projeto 3: Construa um programa que ajude um professor a calcular a média de três notas de um aluno. Caso o aluno entregue o trabalho extra, deverá ser adicionado 1 ponto em sua média. No final mostre a média do aluno e sua situação na disciplina, que poderá ser: aprovado, recuperação ou reprovado.

# 1. Exibir mensagem de boas vindas
print("Calculadora de média - Seja bem-vindo!\n")

# 2. Solicite que a pessoa digite as três notas do aluno
nota1 = float(input("Digite a primeira nota (0 a 10): "))
nota2 = float(input("Digite a segunda nota (0 a 10): "))
nota3 = float(input("Digite a terceira nota (0 a 10): "))

# 3. Solicite que a pessoa informe se o aluno entregou ou não o trabalho extra
trabalho_extra = input("O aluno entregou o trabalho extra? Digite S para Sim e N para Não: ")

# 4. Faça o cálculo da média e armazene em uma variável chamada 'media'
media = (nota1 + nota2 + nota3)/3

# 5. Se o aluno entregou o trabalho extra adicione 1 ponto em sua media
if trabalho_extra == "S" and media <= 9:
  media += 1

# 6. Faça impressão da média do aluno no console
print(f"\nA média do aluno é: {round(media, 2)}")

# 7. Crie uma estrutura condicional que mostre que o aluno foi aprovado se a media for maior ou igual a 7, recuperação se for 5 ou 6 e reprovado se for menor que 5
if media >= 7:
  print("O aluno está aprovado.")
elif media == 5 or media == 6:
  print("O aluno está de recuperação.")
else:
  print("O aluno está reprovado.")
