'''14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.'''
peso = float(input("Informe o peso dos peixes pescados: "))
multa = excesso = 0.0
if peso > 50.0:
    excesso = peso - 50.0
    multa =  excesso * 4
    print(f'O excesso foi de {excesso:.1f} kg e o valor da multa foi de R${multa:.1f}')
else: print("Não houve excesso.")
