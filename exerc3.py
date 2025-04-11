a = float(input("Digite a primeira nota:   "))
b = float(input("Digite a segunda nota:    "))

soma = (a + b) / 2

if soma > 7:
    print(f"sua nota é {soma}, voce está aprovado")
else:
    print(f"sua nota é {soma}, voce esta reprovado")