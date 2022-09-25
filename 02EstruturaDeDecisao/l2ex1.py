#1. Faça um Programa que peça dois números e imprima o maior deles.
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
if num1 > num2:
    print(f'Você inseriu os números {num1} e {num2}. O maior deles é {num1}')
elif num1 < num2:
    print(f'Você inseriu os números {num1} e {num2}. O maior deles é {num2}')
else:
    print(f'Os números são iguais')