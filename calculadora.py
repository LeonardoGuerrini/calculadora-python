print("---------------------")
print("Calculadora em Python")
print("---------------------")


def soma(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y


while True:
    print('''
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão
    ''')

    escolha = input("Sua escolha (1/2/3/4): ")

    print("")

    if escolha in ("1", "2", "3", "4"):
        x = float(input("Primeiro número: "))
        y = float(input("Segundo número: "))

        print("")

        if escolha == "1":
            print(x, "+", y, "=", soma(x, y))
        elif escolha == "2":
            print(x, "-", y, "=", subtracao(x, y))
        elif escolha == "3":
            print(x, "*", y, "=", multiplicacao(x, y))
        elif escolha == "4":
            print(x, "/", y, "=", divisao(x, y))

        proxima_operacao = input("\nDeseja fazer outra operação? (sim/nao): ")
        if proxima_operacao.lower() == "nao":
            print("Obrigado por usar a calculadora! :)")
            break

    else:
        print("Escolha inválida.")
