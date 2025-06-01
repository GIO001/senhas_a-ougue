#Calculadora simples:
#peça dois números e mostre a soma, 
# subtração, multiplicação e divisão.

numero1 = int (input("digite o primeiro numero:\n"))
numero2 = int (input("Digite o segundo numero\n"))

operacao = input ("Digite a operação +, -, *, /: \n")

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "error: divisião por zero"
else:
    resultado = "operação invalida"

print("Resultado da operação:\n", resultado)
