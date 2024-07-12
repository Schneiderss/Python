print('Quanto você irá pagar pelo uso do carro!')
d = float(input('Quantos dias você utilizou o carro? '))
km = float(input('Quantos km você rodou com ele? '))
print('O preço a ser pago é: R${:.2f}'.format(d*60+km*0.15))