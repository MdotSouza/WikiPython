'''15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d. o salário líquido.
    e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
        Obs.: Salário Bruto - Descontos = Salário Líquido.'''
valor = float(input("Insira o valor da hora de trabalho: "))
horas = float(input("Insira a quantidade de horas trabalhadas no mês: "))
salario = valor * horas 
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario_liq = salario - ir - inss - sindicato
print(f'O salário bruto foi: R${salario:.2f}')
print(f'O desconto de IR foi: R${ir:.2f}')
print(f'O desconto de INSS foi: R${inss:.2f}')
print(f'O desconto do sindicato foi: R${sindicato:.2f}')
print(f'O salário líquido é: R${salario_liq:.2f}')
