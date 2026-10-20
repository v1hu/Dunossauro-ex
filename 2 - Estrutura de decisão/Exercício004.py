'''Faça um programa que verifique se uma letra digitada é vogal ou consoante.'''


V = ['a', 'e', 'i', 'o', 'u']  # cria uma lista com as vogais
F = input('Digite uma letra:').lower()  # pede uma letra ao usuário e transforma em minúscula
if F.isalpha() and len(F) == 1:  # confere se a entrada é letra e se tem só um caractere
    if F in V:  # confere se a letra está na lista de vogais
        print(f'"{F.upper()}" é uma vogal')  # mostra que é vogal
    else:  # se não estiver na lista de vogais
        print(f'"{F.upper}" é consoante')  # mostra que é consoante
else:  # se a entrada não for uma única letra
    print('Digite apenas uma letra')  # mostra a mensagem de erro