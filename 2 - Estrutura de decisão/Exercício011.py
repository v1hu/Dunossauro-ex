"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
lhe contraram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador
e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento."""

S = float(input("Qual o valor do salário ? R$ "))

if S <= 0:
    print("Valor Inválido!!")


elif S <= 280:

    N = S + (S * 20 / 100)
    print(f"\033[32mSalário antes do ajuste:\033[m \033[31m R${S:.2f}\033[m")
    print("\033[32mO percentual aplicado foi de\033[m \033[31m20%\033[m")
    print(f"\033[32mO valor do aumento foi:\033[m \033[31mR${S * 20 / 100:.2f}\033[m")
    print(f"\033[32mO novo salário é:\033[m \033[31mR${N:.2f}\033[m")


elif S > 280 and S <= 700:

    N = S + (S * 15 / 100)
    print(f"\033[32mSalário antes do ajuste:\033[m \033[31mR${S:.2f}\033[m")
    print("\033[32mO percentual aplicado foi de:\033[m \033[31m15%\033[m")
    print(f"\033[32mO valor do aumento foi:\033[m \033[31mR$ {S * 15 / 100:.2f}\033[m")
    print(f"\033[32mO novo salário é:\033[m \033[31mR$ {N:.2f}\033[m")

elif S > 700 and S < 1500:

    N = S + (S * 10 / 100)
    print(f"\033[32mSalário antes do ajuste:\033[m \033[31mR${S:.2f}\033[m")
    print("\033[32mO percentual aplicado foi de\033[m \033[31m10%\033[m")
    print(f"\033[32mO valor do aumento foi:\033[m \033[31mR${S * 10 / 100:.2f}\033[m")
    print(f"\033[32mO novo salário é:\033[m \033[31mR${N:.2f}\033[m")

elif S >= 1500:

    N = S + (S * 5 / 100)
    print(f"\033[32mSalário antes do ajuste:\033[m \033[31mR${S:.2f}\033[m")
    print("\033[32mO percentual aplicado foi de:\033[m \033[31m5%\033[m")
    print(f"\033[32mO valor do aumento foi:\033[m \033[31mR${S * 5 / 100:.2f}\033[m")
    print(f"\033[32mO novo salário é:\033[m \033[31mR${N:.2f}\033[m")
