salario = float(input("Digite o salário do colaborador: R$ "))


percentual = 0

if salario <= 280:
    percentual = 20
if salario > 280 and salario <= 700:
    percentual = 15
if salario > 700 and salario <= 1500:
    percentual = 10
if salario > 1500:
    percentual = 5


valor_aumento = salario * percentual / 100
novo_salario = salario + valor_aumento


print("\n--- REAJUSTE SALARIAL ---")
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")
