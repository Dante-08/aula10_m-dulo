from funcoes import calc

calc()
while True:
    resp = input('Continuar calculando S/N: ')
    if resp == 'n' or resp == 'N':
        print('Fechando calculadora')
        break
    elif resp == 's' or 'S':
        calc()