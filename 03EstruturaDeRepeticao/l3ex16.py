#16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
# Faça um programa que gere a série até que o valor seja maior que 500.
ultimo = penultimo = termo = 0
i = 1
while termo < 500:
    if i == 1:
        termo = 0
    elif i == 1 or i == 2:
        termo = ultimo = termo = 1
    else:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
    i += 1
print(termo)
