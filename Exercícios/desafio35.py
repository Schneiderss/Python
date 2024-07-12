a = float(input('Digite o valor do comprimento de uma semirreta: '))
b = float(input('Digite o valor do comprimento de outra semirreta: '))
c = float(input('Digite o valor do comprimento de outra semirreta: '))
#if a > b and a > c:
    #if a < b + c:
        #print('Forma triangulo')
    #else:
        #print('Não forma triângulo')
#if b > a and b > c:
    #if b < a + c:
        #print('Forma triângulo')
    #else:
        #print('Não forma triângulo')
#if c > a and c > b:
    #if c < a + b:
        #print('Forma triângulo')
    #else:
        #print('Não forma triângulo')
if a<b+c and b<a+c and c<a+b:
    print('Forma triângulo')
else:
    print('Não forma triângulo')
    