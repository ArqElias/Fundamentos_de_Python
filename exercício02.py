# Receba ano de nascimento e ano atual
# Calcule idade e semanas

# Entrada
anoNascimento = int(input("Digite o ano de Nascimento: "))
anoAtual = int(input("Digite o ano atual"))


# Processamento
idade = anoAtual - anoNascimento
idadeSemanas = 4 * 12 * anoAtual

# saída
print(f"Sua idade é: {idade} anos(s)")
print(f"Sua idade em semanas: {idadeSemanas} semana(s)")
