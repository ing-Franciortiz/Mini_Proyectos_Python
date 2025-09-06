print("***Sistema de Cajero***\n")


saldo = 10000.00
salir = False

while not salir:
    print(f"""Menu:
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir""")

    opcion = int(input("Escoje una opcion: "))

    if opcion == 1:
        print(f"Tu saldo actual es: ${saldo:.2f} ")

    elif opcion == 2:
        monto = float(input("Cual es el monto a retirar: ")) 
        if monto <= saldo:
            saldo -= monto
            print(f"tu retiro fue exitoso monto actual ${saldo:.2f} \n")
        else:
            print(f"Cantida no valida. Saldo actual ${saldo:.2f}")
    elif opcion == 3:
        mas = float(input("Monto a Depositar: "))
        saldo += mas
        print(f"Tu nuevo saldo es: ${saldo:.2f}")
    elif opcion == 4:
        print("Saliendo del cajero. Hasta pronto...\n ")
        salir = True
    else:
        print("Opcion no validad")