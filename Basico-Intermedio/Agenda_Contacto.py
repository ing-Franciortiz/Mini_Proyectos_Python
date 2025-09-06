print("***Agenda de Contactos***")

agenda = {}

while True:
    print("""
Agenda:
1. Agregar contacto
2. Mostrar contacto
3. Mostrar todos los contactos
4. Salir
""")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese su Nombre: ")
        telefono = input("Ingrese su Numero de Telefono: ")
        email = input("Ingrese su Correo: ")
        direccion = input("Ingrese su Direccion: ")

        if not nombre or not telefono or not email or not direccion:
            print("Error: Todos los campos son obligatorios.")
        else:
            agenda[nombre] = {
                "Telefono": telefono,
                "Email": email,
                "Direccion": direccion
            }
            print(f"{nombre} ha sido agregado a la agenda")

    elif opcion == "2":
        contacto = input("Ingrese el Nombre a buscar: ")
        if contacto in agenda:
            detalles = agenda[contacto]
            print(f"\nInformación de {contacto}:")
            print(f"  Telefono: {detalles['Telefono']}")
            print(f"  Email: {detalles['Email']}")
            print(f"  Direccion: {detalles['Direccion']}\n")
        else:
            print("Contacto no encontrado")

    elif opcion == "3":
        if not agenda:
            print("La agenda está vacía.")
        else:
            print("\nContactos en la Agenda:")
            for nombre, detalles in agenda.items():
                print(f"Nombre: {nombre}")
                print(f"  Telefono: {detalles['Telefono']}")
                print(f"  Email: {detalles['Email']}")
                print(f"  Direccion: {detalles['Direccion']}\n")

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida.")
