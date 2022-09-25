#9.Faça um Programa que leia três números e mostre-os em ordem decrescente.
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))
pos1 = num1
pos2 = num2
pos3 = num3
if num1 > num2 and num1 > num3:
    pos1 = num1
    if num2 > num3:
        pos2 = num2
        pos3 = num3
    else:
        pos2 = num3
        pos3 = num2
elif num2 > num3:
    pos1 = num2
    if num1 > num3:
        pos2 = num1
        pos3 = num3
    else:
        pos2 = num3
        pos3 = num1
elif num3 > num2:
    pos1 = num3
    if num1 > num2:
        pos2 = num1
        pos3 = num2
    else:
        pos2 = num2
        pos3 = num1
else:
    print(f'Os números são iguais')
print(f'Números em ordem decrescente: {pos1}, {pos2} e {pos3}')
