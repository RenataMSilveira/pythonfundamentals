v_hora = float(input("Digite o Valor da hora:"))
h_trabalhadas = float(input("Digite a quantidade de horas Trabalhadas:"))

bruto = v_hora * h_trabalhadas
FGTS = bruto*0.11
SIND = bruto*0.03
IR1 = str('Isento')
IR2 = bruto*0.7
IR3 = bruto*0.15
IR4 = bruto*0.22
IR5 = bruto*0.27


if bruto >= 4601:
    Liquido = bruto-SIND-IR5
    print("Salario Bruto: {}\nValor FGTS:{}\nDesconto Sindicato:{}\nDesconto IR:{}\nSalário Liquido:{}"
    .format(bruto, FGTS, SIND, IR5, Liquido))
elif bruto < 4600 > 3701:
    Liquido = bruto-SIND-IR4
    print("Salario Bruto: {}\nValor FGTS:{}\nDesconto Sindicato:{}\nDesconto IR:{}\nSalário Liquido:{}"
    .format(bruto, FGTS, SIND, IR4, Liquido))
elif bruto < 3700 > 2801:
    Liquido = bruto-SIND-IR3
    print("Salario Bruto:{}\nValor FGTS:{}\nDesconto Sindicato:{}\nDesconto IR:{}\nSalário Liquido:{}"
    .format(bruto, FGTS, SIND, IR3, Liquido))
elif bruto < 2800 > 1901:
    Liquido = bruto-SIND-IR2
    print("Salario Bruto: {}\nValor FGTS:{}\nDesconto Sindicato:{}\nDesconto IR:{}\nSalário Liquido:{}"
    .format(bruto, FGTS, SIND, IR2, Liquido))
elif bruto < 1900:
    Liquido = bruto - SIND - IR1
    print("Salario Bruto: {}\nValor FGTS:{}\nDesconto Sindicato:{}\nDesconto IR:{}\nSalário Liquido:{}"
    .format(bruto, FGTS, SIND, IR1, Liquido))


  #/////////////////////////Correção****************

vlr_hora = float(input('Digite o valor da hora: '))
qtd_hora = float(input('Digite a quantidade de horas trabalhadas: '))

  salario_bruto = (qtd_hora * vlr_hora)

if salario_bruto >= 4600:
    ir = 27
elif salario_bruto > 3700 and salario_bruto < 4600:
    ir = 22
elif salario_bruto > 2800 and salario_bruto <= 3700:
    ir = 15
elif salario_bruto > 1900 and salario_bruto <= 2800:
    ir = 7
else:
    ir = 0

valorIR = salario_bruto * (ir / 100.0)
valor_sindicato = salario_bruto * (3 / 100.0)
valorFGTS = salario_bruto * (11 / 100.0)
total_desconto = valorIR + valor_sindicato

salario_liquido = salario_bruto - total_desconto

print('\nSalario Bruto: ({} * {}): {}'.format(vlr_hora, qtd_hora, salario_bruto))
print('(-) IR ({})%: R${}'.format(ir, valorIR))
print('(-) Sindicato (3%): R${}'.format(valor_sindicato))
print('FGTS (11%): R${}'.format(valorFGTS))
print('Total de Descontos: R${}'.format(total_desconto))
print('Sálario Liquido: R${}'.format(salario_liquido))


