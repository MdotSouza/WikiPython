#17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
ano = int(input("Informe um ano (formato AAAA): "))
if ano%4 == 0: print("Ano bissexto")
else: print("Não é ano bissexto")