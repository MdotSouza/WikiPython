'''25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.'''
n = int(input("Insira a quantidade de pessoas: "))
somatorio = 0
for i in range(1,n+1):
    idade = int(input(f'Insira a idade {i}/{n}: '))
    somatorio += idade
media = somatorio/n
if media >= 0 and media <= 25: print(f'A média é: {media:.2f}. Turma jovem.')
elif media > 25 and media <= 60: print(f'A média é: {media:.2f}. Turma adulta.')
else: print(f'A média é: {media:.2f}. Turma idosa.')