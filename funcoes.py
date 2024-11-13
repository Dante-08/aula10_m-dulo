def soma():
    n1 = float(input('>>'))
    n2 = float(input('>>'))
    print(n1 + n2)

def sub():
    n1 = float(input('>>'))
    n2 = float(input('>>'))
    print(n1 - n2)

def div():
    n1 = float(input('>>'))
    n2 = float(input('>>'))
    print(f'{n1 / n2:.2f}')

def mult():
    n1 = float(input('>>'))
    n2 = float(input('>>'))
    print(n1 * n2)

def calc():
    opera = input('DIgite a operação | + | - | * | / |: ')
    if opera == '+':
        soma()
    elif opera == '-':
        sub()
    elif opera == '*':
        mult()
    elif opera == '/':
        div()
    else:
        print('Operação inválida')

