'''Faça um programa que leia três números e mostre-os em ordem decrescente:'''



n = [0, 0, 0]  # Cria uma lista com três espaços para guardar os números

for P in range(1, 4):  # Repete três vezes; P vale 1, depois 2 e depois 3
    n[P - 1] = int(input(f"Digite o {P}º número: "))  # Pede um número e guarda na lista

if n[0] >= n[1] and n[1] >= n[2]:  # Verifica se o 1º é maior que o 2º e o 2º que o 3º
    print(n[0], n[1], n[2])  # Mostra do maior para o menor
elif n[0] >= n[2] and n[2] >= n[1]:  # Verifica outra ordem possível
    print(n[0], n[2], n[1])  # Mostra do maior para o menor
elif n[1] >= n[0] and n[0] >= n[2]:  # Verifica se o 2º é maior, seguido do 1º e do 3º
    print(n[1], n[0], n[2])  # Mostra do maior para o menor
elif n[1] >= n[2] and n[2] >= n[0]:  # Verifica outra ordem começando pelo 2º número
    print(n[1], n[2], n[0])  # Mostra do maior para o menor
elif n[2] >= n[0] and n[0] >= n[1]:  # Verifica outra ordem começando pelo 3º número
    print(n[2], n[0], n[1])  # Mostra do maior para o menor
else:  # Se nenhuma das ordens anteriores aconteceu, resta a última possibilidade
    print((f"Números em ordem decrescente:", n[2], n[1], n[0]))  # Mostra do maior para o menor