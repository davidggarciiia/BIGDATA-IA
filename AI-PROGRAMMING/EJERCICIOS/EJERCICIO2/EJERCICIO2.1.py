def calculadoraBasica():
    print("----Bienvenido a la calculadora----")
    primerNum = float(input("Escribe el primer número: "))
    segundoNum = float(input("Escribe el segundo número: "))

    print("---------------------------------")
    print("SUMA = +")
    print("RESTA = -")
    print("MULTIPLICACIÓN = *")
    print("DIVISIÓN = /")
    print("---------------------------------")

    operador = input("Selecciona el operador: ")

    match operador:
        case '+':
            resultado = primerNum + segundoNum
            print("El resultado es:", resultado)
        case '-':
            resultado = primerNum - segundoNum
            print("El resultado es:", resultado)
        case '*':
            resultado = primerNum * segundoNum
            print("El resultado es:", resultado)
        case '/':
            if segundoNum != 0:
                resultado = primerNum / segundoNum
                print("El resultado es:", resultado)
            else:
                print("Tu divisor no puede ser 0, por favor ingresa un número válido")
        case _:
            print("Por favor, ingresa un operador válido (+, -, *, /)")
