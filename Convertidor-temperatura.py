print("*** Convertidor de temperatura ***")

print("""\nConvertidor de temperatura
      1. Fahrenheit a Celsius
      2. Celsius a Fahrenheit
      3. Salir""")




def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    while True:
        opcion = int(input("Elija una opcion: "))
        if opcion == 1:
            valor = float(input("Introduce la temperatura en Fahrehheit: "))
            print(f"{valor} °F = {fahrenheit_celsius(valor):.2f}°C")
        elif opcion == 2:
            valor = float(input("Introduce la temperatura en Celsius: "))
            print(f"{valor} °C = {celsius_fahrenheit(valor):.2f}°F")
        elif opcion == 3:
            print("Hasta la proxima ")
            break
        else:
            print("Opcion no valida")