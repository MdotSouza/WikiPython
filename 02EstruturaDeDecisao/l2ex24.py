'''24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    - par ou ímpar;
    - positivo ou negativo;
    - inteiro ou decimal.'''
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
op = input("Selecione a operação ('+' para soma; '-' para subtração, '*' para multiplicação e '/' para divisão): ")
erro = False
resultado = 0
#cálculos
if op == "+":
    resultado = num1+num2
elif op == "-":
    resultado = num1-num2
elif op == "*":
    resultado = num1*num2
elif op == "/":
    resultado = num1/num2
else:
    erro = True
    print('Seleção incorreta!')    
#verifica paridade
if resultado%2 == 0: paridade = "par"
else: paridade = "ímpar"
#verifica sinal
if resultado > 0: sinal = "positivo"
elif resultado < 0: sinal = "negativo"
else: sinal = "nulo"
#verifica tipo numérico
if resultado//1 == resultado: tipo = "inteiro"
else: tipo = "decimal"
#resposta
if erro == False: print(f'Resultado = {resultado}: número {paridade}, {sinal} e {tipo}')
