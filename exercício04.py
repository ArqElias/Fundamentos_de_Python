# Receba nome, peso e altura
# Calcule o IMC


nome = (input("Digite o nome: "))
# Float para numeros com casas decimais 
peso = float(input ("Digite o peso: "))
altura = float(input ("Digite a altura: "))

# Processamento
# IMC = peso (kg)

IMC = peso / (altura*altura)

# Saída
print(f"IMC: {IMC: .2f}")
