# Receba um nome, cargo e salário a acrescente 10%

#Entrada (Nome, Cargo, Salário)

nome = input("Digite o seu nome: ")
print()
cargo = input("Digite o seu cargo: ")
print()
salário = float(input("Digite o seu salário: "))
print()

# Processamento

acrescimo = salário / 10 + salário

# Saída

print(f"salário final 10%: {acrescimo: .2f}")