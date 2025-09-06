print("***Calculadora de promedio***")

cantidad = int(input("Proporciona el no. de calificaciones a evaluar: "))
calificaciones = []

for i in range (cantidad):
    valor = int(input(f"Calificaion [{i+1}]:"))
    calificaciones.append(valor)
    promedio = sum(calificaciones) / cantidad
print(f"\nLas calificaciones proporcionadas son:", calificaciones)
print(f"\nPromedio de las Calificaciones: {promedio}")