# Descrição: Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
# escolhendo a operação a ser realizada.
# Entrada: O usuário deve fornecer dois números e escolher a operação a ser realizada.
# Saída: O resultado da operação escolhida entre os dois números fornecidos.

input1 = float(input("Digite o primeiro número: "))
input2 = float(input("Digite o segundo número: "))
op = input("Digite a operação a ser realizada (+, -, *, /): ")

if op == "+":
    resultado = input1 + input2
elif op == "-":
    resultado = input1 - input2
elif op == "*":
    resultado = input1 * input2
elif op == "/":
    resultado = input1 / input2

print(f"O resultado da operação é ({op}):", resultado)
