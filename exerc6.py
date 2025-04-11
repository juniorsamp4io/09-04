letra = input("Digite uma letra: ").lower()

if len(letra) != 1 or not letra.isalpha():
    print("Digite apenas uma letra do alfabeto.")
elif letra in ['a', 'e', 'i', 'o', 'u']:
    print("É uma vogal.")
else:
    print("É uma consoante.")
