# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

# try:
#     numero = int(input('>>> '))
# except :
#     print('Isso não é um numero')

# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

try:
    n1 = int(input('>> '))
    n2 = int(input('>> '))
    div = n1 / n2
except ZeroDivisionError:
    print('erro de divisão')
# Exercício 3:
# Crie uma função que aceite uma lista e um índice como entrada e retorne o elemento naquele índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
lista = [1,2,3]

def verifica(lista):
    try:
        n = int(input('>> '))
        i = lista[n]
        print(i)
    except:
        print('Esse indice não existe')
verifica()

# Exercício 4:
# Crie uma função que divida dois números e manipule a exceção caso o divisor seja zero.

def manipule():
    try:
        n1 = int(input('>> '))
        n2 = int(input('>> '))
        div = n1 / n2
    except ZeroDivisionError:
        print('erro de divisão')
manipule()
