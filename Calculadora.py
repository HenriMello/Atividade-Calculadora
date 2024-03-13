def soma(x,y):
    return x + y
def subtracao(x,y):
    return x - y
def multiplicacao(x,y):
    return x * y
def divisao(x,y):
    if y == 0:
        raise ValueError("Divisão por zero não permitida")
    else:
        return x/y

o = 1
i = 1
while (i == 1):
    print("Selecione: ")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    op = int(input("Opção: "))

    if op == 1:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print(soma(n1, n2))
        while o == 1:
            print("Deseja continuar calculando? ")
            print("1 - SIM")
            print("2 - NÂO")
            cont_calc = int(input("Opção: "))
            if cont_calc == 1:
                i = 1
                o = 0
            elif cont_calc == 2:
                i = 0
                o = 0 
            else:
                print("Opção Invalida")
                o = 1
    elif op == 2:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print(subtracao(n1, n2))
        while o == 1:
            print("Deseja continuar calculando? ")
            print("1 - SIM")
            print("2 - NÂO")
            cont_calc = int(input("Opção: "))
            if cont_calc == 1:
                i = 1
                o = 0
            elif cont_calc == 2:
                i = 0
                o = 0 
            else:
                print("Opção Invalida")
                o = 1
    elif op == 3:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print(multiplicacao(n1, n2))
        while o == 1:
            print("Deseja continuar calculando? ")
            print("1 - SIM")
            print("2 - NÂO")
            cont_calc = int(input("Opção: "))
            if cont_calc == 1:
                i = 1
                o = 0
            elif cont_calc == 2:
                i = 0
                o = 0 
            else:
                print("Opção Invalida")
                o = 1
    elif op == 4:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print(divisao(n1, n2))
        while o == 1:
            print("Deseja continuar calculando? ")
            print("1 - SIM")
            print("2 - NÂO")
            cont_calc = int(input("Opção: "))
            if cont_calc == 1:
                i = 1
                o = 0
            elif cont_calc == 2:
                i = 0
                o = 0 
            else:
                print("Opção Invalida")
                o = 1
    else:
        print("Opcão Inválida!")
        i = 1
            