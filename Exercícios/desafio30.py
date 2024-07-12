n = int(input('Descubra se um número é par ou ímpar!'))
m = n%10
lista = [0,2,4,6,8]
if m in lista:
    print('Esse número é par!')
else:
    print('Esse número é ímpar')