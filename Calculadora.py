
from operacoes import Calculadora


#Script para interação com o usuário
def menu():
    calculadora = Calculadora()
    print(r"""
  _____________________
 |  _________________  |
 | | Python Calc   0.| |
 | |_________________| |
 |  ___ ___ ___   ___  |
 | | 7 | 8 | 9 | | + | |
 | |___|___|___| |___| |
 | | 4 | 5 | 6 | | - | |
 | |___|___|___| |___| |
 | | 1 | 2 | 3 | | x | |
 | |___|___|___| |___| |
 | | . | 0 | = | | / | |
 | |___|___|___| |___| |
 |_____________________|
""")

    print("------------ Bem-vindo à Calculadora! ------------")

    while True:
        print("\nEscolha uma das operações:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potenciação")
        print("6. Raiz Quadrada")
        print("7. Logaritmo")
        print("0. Sair da Calculadora")

        escolha = input("Escolha a operação (0-7): ")

        if escolha == '0':
            escolha = input("Deseja sair mesmo ? (s) para Sim ou (n) para Não\n")
            escolha = escolha.upper()
            if escolha == 'S' or escolha == 'SIM':
                print("Saindo...")
                break
            else:
                continue
        elif escolha in ['1', '2', '3', '4', '5']:
            while True:
                try:
                    num1 = int(input("Digite o primeiro número: "))
                    num2 = int(input("Digite o segundo número: "))
                    break
                except ValueError:
                    print("Erro! Por favor, insira um número válido.")
                    continue
            if escolha == '1':
                print("Resultado: ", calculadora.somar(num1, num2))
            elif escolha == '2':
                print("Resultado: ", calculadora.subtrair(num1, num2))
            elif escolha == '3':
                print("Resultado: ", calculadora.multiplicar(num1, num2))
            elif escolha == '4':
                try:
                    print("Resultado: ", calculadora.dividir(num1, num2))
                except ValueError as i:
                    print(i)
            elif escolha == '5':
                print("Resultado: ", calculadora.potencia(num1, num2))
        elif escolha == '7':
            while True:
                try:
                    num1 = int(input("Digite um número para o logaritmo: "))
                    base = int(input("Digite a base do logaritmo (número maior que 1): "))
                    if base <= 1:
                        print("A base deve ser um número maior que 1.")
                        continue
                    elif num1 == False:
                        print("Entrada inválida. Por favor, digite um número.")
                    else:
                        break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
            try:
                print("Resultado: ", calculadora.logaritmo(num1, base))
            except ValueError as i:
                print(i)
        elif escolha == '6':
            while True:
                try:
                    num = int(input("Digite o número para calcular a raiz quadrada: "))
                    break
                except ValueError:
                    print("Entrada inválida! Por favor, insira um número válido.")
            try:
                print("Resultado: ", calculadora.raiz_quadrada(num))
            except ValueError as i:
                print(i)
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
