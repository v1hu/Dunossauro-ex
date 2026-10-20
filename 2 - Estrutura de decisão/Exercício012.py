''''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo).
- 3% para o Sindicato
- FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
- O Salário Líquido corresponde ao Salário Bruto menos os descontos. 

O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

- Desconto do IR: 
- Salário Bruto até 900 (inclusive) - isento 
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10% - 
- Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00
(-) INSS (10%)                  : R$  110,00
(-) Sindicato (3%)              : R$   33,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  198,00
Salário Líquido                 : R$  902,00'''


valor = float(input('Qual o valor da hora trabalhada? '))
horas = float(input('Quantida de horas trabalhadas? '))
salariobruto = valor * horas

if valor <= 0 or horas <= 0:
    print('Valor Inválido')

elif salariobruto <= 900:
    
    IR = 0
    INSS = salariobruto * 10 / 100
    SIN = salariobruto * 3 / 100
    FGTS = salariobruto * 11 / 100
    TD = IR + INSS + SIN 
    SL = salariobruto - (TD)
    
    print(f'\033[32mSalário Bruto:\033[m \033[34mR$ {salariobruto:.2f}\033[m')
    print(f'\033[41m(-)IR (0%):\033[m \033[31mR$ {IR:.2f}\033[m')
    print(f'\033[41m(-)INSS (10%):\033[m \033[31mR$ {INSS:.2f}\033[m')
    print(f'\033[41m(-)Sindicato (3%):\033[m \033[31mR$ {SIN:.2f}\033[m')
    print(f'\033[32mFGTS (11%):\033[m \033[34mR$ {FGTS:.2f}\033[m')
    print(f'\033[41mTotal de Descontos:\033[m\033[31m R$ {TD:.2f}\033[m')
    print(f'\033[32mSalário Líquido:\033[m\033[34m R$ {SL:.2f}\033[m')

elif salariobruto > 900 and salariobruto <= 1500:
    
    IR = salariobruto * 5 / 100
    INSS = salariobruto * 10 / 100
    SIN = salariobruto * 3 / 100
    FGTS = salariobruto * 11 / 100
    TD = IR + INSS + SIN
    SL = salariobruto - (TD)
    
    print(f'\033[32mSalário Bruto:\033[m \033[31mR$ {salariobruto:.2f}\033[m')
    print(f'\033[41m(-)IR (5%):\033[m \033[31mR$ {IR:.2f}\033[m')
    print(f'\033[41m(-)INSS (10%):\033[m \033[31mR$ {INSS:.2f}\033[m')
    print(f'\033[41m(-)Sindicato (3%):\033[m \033[31mR$ {SIN:.2f}\033[m')
    print(f'\033[32mFGTS (11%):\033[m \033[31mR$ {FGTS:.2f}\033[m')
    print(f'\033[41mTotal de Descontos:\033[m\033[31m R$ {TD:.2f}\033[m')
    print(f'\033[32mSalário Líquido:\033[m \033[31mR$ {SL:.2f}\033[m')

elif salariobruto > 1500 and salariobruto <= 2500:

    IR = salariobruto * 10 / 100
    INSS = salariobruto * 10 / 100
    SIN = salariobruto * 3 / 100
    FGTS = salariobruto * 11 / 100
    TD = IR + INSS + SIN
    SL = salariobruto - (TD)
    
    print(f'\033[32mSalário Bruto:\033[m \033[31mR$ {salariobruto:.2f}\033[m')
    print(f'\033[41m(-)IR (10%):\033[m \033[31mR$ {IR:.2f}\033[m')
    print(f'\033[41m(-)INSS (10%):\033[m \033[31mR$ {INSS:.2f}\033[m')
    print(f'\033[41m(-)Sindicato (3%):\033[m \033[31mR$ {SIN:.2f}\033[m')
    print(f'\033[32mFGTS (11%):\033[m \033[31mR$ {FGTS:.2f}\033[m')
    print(f'\033[41mTotal de Descontos:\033[m \033[31mR$ {TD:.2f}\033[m')
    print(f'\033[32mSalário Líquido:\033[m \033[31mR$ {SL:.2f}\033[m')

elif salariobruto > 2500:

    IR = salariobruto * 20 / 100
    INSS = salariobruto * 10 / 100
    SIN = salariobruto * 3 / 100
    FGTS = salariobruto * 11 / 100
    TD = IR + INSS + SIN
    SL = salariobruto - (TD)
    
    print(f'\033[32mSalário Bruto:\033[m \033[31mR$ {salariobruto:.2f}\033[m')
    print(f'\033[41m(-)IR (20%):\033[m \033[31mR$ {IR:.2f}\033[m')
    print(f'\033[41m(-)INSS (10%):\033[m \033[31mR$ {INSS:.2f}\033[m')
    print(f'\033[41m(-)Sindicato (3%):\033[m \033[31mR$ {SIN:.2f}\033[m')
    print(f'\033[32mFGTS (11%):\033[m \033[31mR$ {FGTS:.2f}\033[m')
    print(f'\033[41mTotal de Descontos:\033[m \033[31mR$ {TD:.2f}\033[m')
    print(f'\033[32mSalário Líquido:\033[m \033[31mR$ {SL:.2f}\033[m')
