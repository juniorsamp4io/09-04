salario = float(input("Digite o salário: "))

if salario < 500:
    salario = salario + (salario * 0.15)

if salario >= 500 and salario <= 1000:
    salario = salario + (salario * 0.10)

if salario > 1000:
    salario = salario + (salario * 0.05)

print("Salário ajustado: R$", salario)