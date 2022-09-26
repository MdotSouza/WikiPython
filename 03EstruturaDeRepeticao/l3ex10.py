#10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
start = int(input("Digite um número: "))
end = int(input("Digite um número: "))
for i in range(start+1,end,1):
    print(i)
