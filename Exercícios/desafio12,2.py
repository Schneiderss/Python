n = float(input('Qual é o preço do produto? R$'))
print('O preço à vista tem 10% de desconto {}> {}'.format('-'*2,n*0.9))
print('O preço à prazo tem um acréscimo de 15% {}> {:.2f}'.format('-',n*1.15))