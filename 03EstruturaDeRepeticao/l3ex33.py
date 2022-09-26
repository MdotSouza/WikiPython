'''33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas. '''
n = int(input("Insira a quantidade de temperatura medidas: "))
maior = menor = somatorio = 0
for i in range (1,n+1):
    temp = float(input(f'Digite a temperatura {i}/{n} em °C : '))
    if i == 1: menor = maior = temp
    elif temp > maior: maior = temp
    elif temp < menor: menor = temp
    somatorio += temp
print(f'''TEMPERATURA MÁXIMA = {maior:.1f} °C
TEMPERATURA MÍNIMA = {menor:.1f} °C
MÉDIA = {somatorio/n:.1f} °C''')
