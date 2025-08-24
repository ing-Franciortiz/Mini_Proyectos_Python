print("***Calculadora en Python***\n")

num1 = num2 = resultado = 0
salir = False

while not salir:
    print(f"""Operaciones que puede realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division    
    5. Salir""")

    opcion = int(input("Escoje una opcion: "))
    if 1 <= opcion <= 4 :
        num1 = float(input("Dame el valor 1: "))
        num2 = float(input("Dame el valor 2: "))
    if opcion == 1:
        resultado = num1 + num2
        print(f" Resultado de la suma: {resultado:.2f}\n")
    elif opcion == 2:
        resultado = num1 - num2
        print(f" Resultado de la resta: {resultado:.2f}\n")
    elif opcion == 3:
        resultado = num1 * num2
        print(f" Resultado de la multiplicación: {resultado:.2f}\n")
    elif opcion == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f" Resultado de la división: {resultado:.2f}\n")
        else:
            print(" No se puede dividir entre 0.\n")
    elif opcion == 5:
        print("Saliendo de la calculadora. Hasta pronto ")
        salir = True
    else:
        print("Opcion no validad")