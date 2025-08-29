print("***Playlist de Canciones***")


cantidad = int(input("Cuantas canciones desea agregar: "))
canciones = []

for i in range (cantidad):
    nombre = input(f"Ingrese el nombre de la cancion {i+1}: ")
    canciones.append(nombre)

print("\n---Tu Playlist---\n")

print(f"tiene un total de {cantidad} canciones.")
for cancion in sorted(canciones, key=str.lower):
    print(cancion)