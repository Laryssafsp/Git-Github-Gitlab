# Descrição: Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.
# Entrada: O usuário irá digitar uma string, por exemplo: "Python" e um número inteiro, por exemplo: 3
# Saída: O programa irá repetir a string o número de vezes informado e exibir a

string = input("Digite uma string: ")
vezes = int(input("Digite um número inteiro: "))

for i in range(vezes):
    print(string)

# # imprimir um ao lado do outro, sem espaço entre eles
print(string * vezes)
print(string + " " * vezes)

# imprimir um ao lado do outro, com espaço entre eles
print((string + " ") * vezes)
