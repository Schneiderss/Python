from datetime import date
ano = int(input('Descubra se determinado ano é bissexto! '))
k = ano%4
if ano==0:
    ano=date.today().year
if k == 0 and ano%100!=0 or ano%400==0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))