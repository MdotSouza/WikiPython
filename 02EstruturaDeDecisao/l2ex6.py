#6. Faça um Programa que leia três números e mostre o maior deles.
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))
if num1 > num2 and num1 > num3:
    print(f'Você inseriu os números {num1}, {num2} e {num3}. O maior deles é {num1}')
elif num2 > num3:
    print(f'Você inseriu os números {num1}, {num2} e {num3}. O maior deles é {num2}')
elif num3 > num2:
    print(f'Você inseriu os números {num1}, {num2} e {num3}. O maior deles é {num3}')
else:
    print(f'Os números são iguais')
