# Descrição: Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.
# O que um palíndromo? É uma palavra, frase ou número que pode ser lida da mesma forma de trás para frente. Por exemplo: "arara", "radar", "12321".

def verificar_palindromo(palavra):
    # Remover espaços e converter para minúsculas
    palavra = palavra.replace(" ", "").lower()

    # Inverter a palavra
    palavra_invertida = palavra[::-1]

    # Verificar se a palavra é igual à sua versão invertida
    if palavra == palavra_invertida:
        return print(f"A palavra '{palavra}' é um palíndromo.")
    else:
        return print(f"A palavra '{palavra}' não é um palíndromo.")

# Testando a função
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
verificar_palindromo(palavra)

