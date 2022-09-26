#1. Faça um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = int(input("Insira uma nota, entre zero e dez: "))
while True:
    if nota >= 0 and nota <= 10:
        print("Nota Válida")
        break
    else:
        print("Nota inválida")
        nota = int(input("Insira nova nota, entre zero e dez: "))
