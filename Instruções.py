def calculadora():
    while True:
        print("\nEscolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número da operação: ")

        if opcao == '1':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")

        elif opcao == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")

        elif opcao == '3':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")

        elif opcao == '4':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")

        elif opcao == '0':
            print("Encerrando o programa...")
            break

        else:
            print("Essa opção não existe. Tente novamente.")

calculadora()
