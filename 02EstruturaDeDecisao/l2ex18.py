#18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia = int(input("Apresentação de data. Informe o dia: "))
mes = int(input("Apresentação de data. Informe o mês: "))
ano = int(input("Apresentação de data. Informe o ano: "))
if (dia > 31 or mes > 12):
    print("Data Inválida!")
elif (mes == 2 and ano%4 != 0 and dia > 28) or (mes == 2 and ano%4 == 0 and dia > 29):
    print("Data Inválida!")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
    print("Data Inválida!")
else:
    print("Data Válida")