print("***Sistema del Calificaciones ***")

calificacion = float(input("Proporciona el valor de tu Calificaciones (0-10): "))
resultado = None

if  9 <= calificacion <= 10:
    resultado = "A"
elif 8 <= calificacion < 9:
    resultado = "B"
elif  7 <= calificacion < 8:
    resultado = "C"
elif  6 <= calificacion < 7:
    resultado = "D"
elif  0 <= calificacion < 6:
    resultado = "F"
else:
    resultado = "Valor Desconocido"

print(f"Calificacion {calificacion} es equivalente a {resultado}")