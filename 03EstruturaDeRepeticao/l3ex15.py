#15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
n = int(input("Digite um número: "))
ultimo = penultimo = termo = 1
if n > 2:
    for i in range(2,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
print(termo)