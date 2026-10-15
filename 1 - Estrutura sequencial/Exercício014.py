''''João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
 Imprima os dados do programa com as mensagens adequadas.
 
 50kg max - 4,00 por excedente

 '''

P = float(input('Quantos Kg de peixe?'))

if P <= 50:
    print('Você está dentro dos limites')

else:
    print(f'O valor da Multa pelo excedente é : {(P - 50)*4}')


''''


P = float(input('Quantos Kg de peixe?'))

if P <= 50:
    print('Você está dentro dos limites')

else:
    print(f'O valor da Multa pelo excedente é : {(P - 50)*4}')


    ///////////////////////////////////////////////////////////////////


peso = float(input("Digite o peso dos peixes em quilos: "))

excesso = max(0, peso - 50)
multa = excesso * 4

print(f"Excesso: {excesso:.2f} kg")
print(f"Multa a pagar: R$ {multa:.2f}")






'''