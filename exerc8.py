
p1 = float(input("Digite o preço do primeiro produto: "))
p2 = float(input("Digite o preço do segundo produto: "))
p3 = float(input("Digite o preço do terceiro produto: "))


mais_barato = p1
produto = "primeiro"


if p2 < mais_barato:
    mais_barato = p2
    produto = "segundo"


if p3 < mais_barato:
    mais_barato = p3
    produto = "terceiro"


print(f"Você deve comprar o {produto} produto, que custa R$ {mais_barato:.2f}")
