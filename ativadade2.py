def v():
    print('='*50)
    print(f'PRODUTOS SELECIONADOS: \n{carrinho}')
    tot = sum(total)
    print(f'Total - R${tot:.2f}')

def pag():
    print('='*50)
    formapag = input('Escolha a forma de pagamento: \n0 Pix \n1 Dinheiro \n2 Cartão Débito \n3 Cartão Crédito \n>>>')
    if formapag == '0' or formapag == '1' or formapag == '2' or formapag == '3':
        print('PAGAMENTO CONCLUIDO')

def desp(nome):
    print('='*50)
    return (f'Volte Sempre {nome}')

carrinho = []
total = []
produtos = ['Maracujá','Morango','limão']
valor = [7.99,5.65,2.75]
username = input('Digite seu nome de usuário: ')
password = input('Digite sua senha: ')

def mercado():
    print('Sejá Bem Vindo(a)')
    prod = int(input('''
0 Maracujá - 7.99
1 Morango - 5.65
2 Limão - 2.75    
Digite o numero do produto: '''))
    carrinho.append(produtos[prod])
    total.append(valor[prod])
    escolha = input('Continuar comprando S/N: ')

    while escolha == 's' or escolha == 'S':
        print('='*50)
        prod = int(input('Digite o numero do produto: '))
        carrinho.append(produtos[prod])
        total.append(valor[prod])
        escolha = input('Continuar comprando S/N: ')
        if escolha == 'n' or escolha == 'N':
            print('='*50)
            print('Finalizando compra')
            break
       
    v()
    pag()
    i = desp(username)
    print(i)
    sair = input('Digite ENTER para sair')
