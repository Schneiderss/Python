from math import floor
d = float(input('A quantos kilômetros fica o seu destino? '))
k = floor(d)
print('Até 200km o custo é de R$0,50 por km, a partir disso é R$0,45 por km')
if k<= 200:
    print('Sua passagem custará R${:.2f}'.format(0.5*k))
else:
    print('Sua passagem custará R${:.2f}'.format(0.45*k))