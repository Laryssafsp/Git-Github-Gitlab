#Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

input1 = float(input("Digite a primeira nota: "))
input2 = float(input("Digite a segunda nota: "))
input3 = float(input("Digite a terceira nota: "))
media = (input1 + input2 + input3) / 3
print(f"A média das notas é: {media}")

# Inseriondo os valoes separados por ","
input1, input2, input3 = map(float, input("Digite as três notas separadas por vírgula: ").split(","))
media = (input1 + input2 + input3) / 3
print(f"A média das notas é: {media}")

