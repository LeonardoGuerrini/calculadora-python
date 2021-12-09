import time # Biblioteca time

print('---------------------')
print('Calculadora em Python')
print('---------------------\n')

# Criando as funções de soma, subtração, etc.

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y


while True:
    try:
        escolha = input('''
Selecione:

[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão

Sua escolha: ''')

        if escolha in ('1', '2', '3', '4'):

            x = int(input('Insira um número: '))
            y = int(input('Insira outro número: '))

            print('') # Pulando uma linha
            print('') # Pulando uma linha

            if escolha == '1':
                print(f'{x} + {y} =', soma(x, y))
            
            elif escolha == '2':
                print(f'{x} - {y} =', subtracao(x, y))

            elif escolha == '3':
                print(f'{x} * {y} =', multiplicacao(x, y))
            
            elif escolha == '4':
                print(f'{x} / {y} =', divisao(x, y))
            
            # Repetir

            if str(input('\nVocê deseja repetir? (sim/nao): ')).lower() in ['n', 'nao', 'não']:
                print('\nObrigado por usar o programa :)')
                break
            
        else:
            print('\n-------------------')
            print('Escolha inválida!')
            print('-------------------')
            
            time.sleep(1)

    except:
        print('\nErro!')
