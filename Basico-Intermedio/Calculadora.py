print("*** Calculadora ***")

def suma_valores():
    resultado = valor1 + valor2
    print(f"El resultado de la suma es: {resultado}\n")

def resta_valores():
    resultado = valor1 - valor2
    print(f"El resultado de la resta es: {resultado}\n")
def multi_valores():
    resultado = valor1 * valor2
    print(f"El resultado de la Multiplicacion es: {resultado}\n")
def divi_valores():
    resultado = valor1 / valor2
    print(f"El resultado de la Division es: {resultado}\n")

if __name__ == "__main__":

    while True:
        print(f"""\nOperaciones que puedes realizar
            1. Suma
            2. Resta
            3. Multiplicacion
            4. Division
            5. Salir""")

        opcion = int(input("Escoge una opcion: "))

        if opcion == 5:
            print("Saliendo del programa de calculadora. Hasta la proxima")
            break
    
       
        if 1 <= opcion <= 4:
            valor1 = float(input("Dame el Primer valor: "))
            valor2 = float(input("Dame el segundo valor: "))
        if opcion == 1:
           
            suma_valores()
        elif opcion == 2:
            resta_valores()
        elif opcion == 3:
            multi_valores()
        elif opcion == 4:
            divi_valores()
        else:
            print("Opcion no encontrada. Selecione una valida")
