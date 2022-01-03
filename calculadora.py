print('---------------------')
print('Calculadora em Python')
print('---------------------\n')

def soma(x, y): # Soma
    return x + y

def sub(x, y): # Subtração
    return x - y

def mult(x, y): # Multiplicação
    return x * y

def divisao(x, y): # Divisão
    return x / y



while True:
    try:
        escolha = input('[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n\nSua escolha: ')

        if escolha in ('1', '2', '3', '4'):

            x = float(input('\nInsira um número: '))
            y = float(input('Insira outro número: '))

            print('') # Pulando uma linha
            
            if escolha == '1':
                print(f'{x} + {y} =', soma(x, y))
            
            elif escolha == '2':
                print(f'{x} - {y} =', sub(x, y))

            elif escolha == '3':
                print(f'{x} * {y} =', mult(x, y))

            elif escolha == '4':
                print(f'{x} / {y} =', divisao(x, y))

            print('\n------------------------------------')

            if str(input('\nVocê deseja repetir? (sim/nao): ')).lower() in ['n', 'nao', 'não']:
                print('\nObrigado por usar o programa! :)')
                break
            
            print('') # Pulando uma linha

        else:
            print('\nEscolha inválida!\n')

    except ValueError:
        print("\nErro:", ValueError, "| Utilize apenas números!\n")
