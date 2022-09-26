#11. Altere o programa anterior para mostrar no final a soma dos números.
start = int(input("Digite um número: "))
end = int(input("Digite um número: "))
soma = 0
for i in range(start+1,end,1):
    print(i)
    soma += i
print(soma)
