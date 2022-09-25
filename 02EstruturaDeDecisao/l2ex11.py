'''11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    - salários até R$ 280,00 (incluindo) : aumento de 20%
    - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    - salários de R$ 1500,00 em diante : aumento de 5%
    Após o aumento ser realizado, informe na tela:
        - o salário antes do reajuste;
        - o percentual de aumento aplicado;
        - o valor do aumento;
        - o novo salário, após o aumento.'''
salario = float(input("Insira o valor do salário: "))
if salario >= 1500.0:
    salarioReajustado = salario*1.05
    percentual = "5%"
elif salario < 1500.0 and salario >= 700.0:
    salarioReajustado = salario*1.10
    percentual = "10%"
elif salario < 700.0 and salario >= 280.0:
    salarioReajustado = salario*1.15
    percentual = "15%"
else:
    salarioReajustado = salario*1.20
    percentual = "20%"
print(f'Salário antes do reajuste: R$ {salario:.2f}')
print(f'Percentual do aumento aplicado: {percentual}')
print(f'Valor do aumento: R$ {salarioReajustado-salario:.2f}')
print(f'Salário após aumento: R$ {salarioReajustado:.2f}')
