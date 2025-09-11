print(f"***Sistema de Inventarios***")

inventario = []

numero_invetario = int(input("Cuantos productos deseas agregar al inventario? "))

for indice in range(numero_invetario):
    print(f"Proporciona los valores del producto {indice + 1}")
    nombre = input(f"Nombre: ")
    cantidad = int(input(f"Cantidad: "))
    precio = float(input(f" Precio : "))

    producto = {"id": indice, "nombre": nombre, "cantidad": cantidad, "precio": precio }

    inventario.append(producto)

print(f"\nInventario inicial: {inventario}")

id_buscado = int(input("Coloca el id:"))

producto_encontrado = None

for producto in inventario:
    if producto.get("id") == id_buscado:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print("Informacion del producto encontrado: ")
    print(f"""Id: {producto_encontrado.get("id")}")
    Nombre:  {producto_encontrado.get("nombre")}"
    Precio:  {producto_encontrado.get("precio")}
    cantidad:  {producto_encontrado.get("cantidad")}""")

else:
    print(f"Producto con id {id_buscado} No encontrado")


print(f"\n--- Inventario Detallado ---")
for producto in inventario:
    print(f"""Id: {producto.get("id")}
    Nombre: {producto.get("nombre")}
    Precio: {producto.get("precio")}
    Cantidad: {producto.get("cantidad")}""")