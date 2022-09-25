#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit [F = (C*1,8)+32].
temp_c = float(input("Insira a temperatura em graus Celsius: "))
temp_f = (temp_c*1.8)+32
print(f'A temperatura em graus Fahrenheit é: {temp_f:.2f}')
