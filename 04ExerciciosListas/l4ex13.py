'''13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''
dictMedias = {'1 - Janeiro':0.0,'2 - Fevereiro':0.0,'3 - Março':0.0,'4 - Abril':0.0,'5 - Maio':0.0,'6- Junho':0.0,'7 - Julho':0.0,'8 - Agosto':0.0, \
'9 - Setembro':0.0,'10 - Outubro':0.0,'11 - Novembro':0.0,'12 - Dezembro':0.0}
for mes in dictMedias.keys():
    dictMedias[mes] = float(input(f'Insira a temperatura média do mês {mes} (em °C): '))
media = sum(dictMedias.values())/len(dictMedias)
print(f'Média anual = {media:.1f}°C')
print('Meses com Temperatura acima da média:')
for mes, temp in dictMedias.items():
    if temp > media: print(f'{mes} = {temp:.1f}°C')
