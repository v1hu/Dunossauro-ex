'''Faça um programa que verifique se uma letra digitada é "F" ou "M". 

Conforme a letra escrever:

F - Feminino
M - Masculino
Sexo Inválido.'''


sexo = input("Sexo: [M/F] ").upper()

if sexo == 'M':
       print(f'O sexo é masculino.')
elif sexo == 'F':
        print(f'O sexo é feminino.')
    
else:
       print(f'Sexo invalido')


''' ////////////// MODO 2 ////////////////'''


print("Escolha o sexo:")
print("[ 1 ] - Masculino")
print("[ 2 ] - Feminino")

sexo = int(input("Sexo: [1/2] "))

if sexo == 1:
    print("O sexo é masculino.")
elif sexo == 2:
    print("O sexo é feminino.")
else:
    print("Sexo inválido.")