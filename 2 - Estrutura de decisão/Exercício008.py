''''Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato:'''

print(f'{ ' SUPER MERCADOS GUANABARA ' :=^40}')

menor = float('inf')  # guarda o menor preço encontrado até aquele momento. # começa maior que qualquer preço que será digitado
num_menor = 0 #guarda a qual produto pertence esse menor preço.


for P in range(1, 4): #P indica qual produto está sendo analisado: 1, 2 ou 3.
    print(f"===== {P}ºProduto =====")

    valor = float(input("Qual valor do produto? R$ ")) #valor recebe o preço digitado naquela volta do laço.
   
    if valor < menor: # compara cada preço com o menor até agora
        menor = valor
        num_menor = P

print(f"Você deve comprar o {num_menor}º produto, com valor R${menor:.2f}, pois é o mais barato.")