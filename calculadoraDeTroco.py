import time


def home():
    print('\n\t-------------------------------(ಠ_ಠ)----------------------------------'
          ' \n\t -------------------- VAMOS FAZER UMAS TROCAS ------------------------'
          '\n\t-----------------------------------------------------------------------')
    opcao = input('''
                    1. CALCULADORA DE TROCO
                    2. EXIT
 
                    ''')

    opcao = opcao.lower()
    if opcao == '1':
        calculadora()
    elif opcao == '2':
        print('\t\t\t\t\t\t(ಠ_ಠ)')
        time.sleep(5)
        exit()
    else:
        print('\t por favor, escolha entre a opcao 1 ou opcao 2')
        home()


def calculadora():
    while True:
        total_da_compra = float(input('total da compra:$ '))
        if total_da_compra == 00:
            home()
        else:
            pass
        valor_pago = float(input('valor recebido:$ '))
        troco = valor_pago - total_da_compra
        if troco == 0:
            print('não há o que retornar')
        elif total_da_compra > valor_pago:
            restante = troco * (-1)
            print(f'ainda resta $ {restante} a ser pago')
        else:
            print(f'$ {troco}')
            print('digite 00 para voltar ao menu')


def exit():
    quit()


home()
