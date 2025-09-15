print(f"Sistema de Inventario con (Funciones)")

Inventario = [
    {"id": 1, "nombre": "Camiza", "precio": 25.99, "cantidad": 50},
    {"id": 2, "nombre": "Pantalones", "precio": 39.99, "cantidad": 30},
    {"id": 3, "nombre": "Zapatos", "precio": 49.99, "cantidad": 20}
]

def mostrar_inventario():
    print("--- Inventario del Almacen ---")
    for producto in Inventario:
        print(f"id: {producto.get("id")}, nombre: {producto.get("nombre")},",
            f"Precio: {producto.get("precio")}, Cantidad: {producto.get("cantidad")}")


def agregar_producto():
    print("--- Agrega Nuevo Producto ---")
    id = input("id: ")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = input("Cantidad: ")
    producto = {
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    Inventario.append(producto)
    print("Producto agregado al inventario")

def buscar_producto_por_id():
    print("--- Buscar Producto por Id ---")
    id_buscar = int(input("Agrega el id: "))
    for producto in Inventario:
        if producto.get("id") == id_buscar:
            print("\nInformacion del producto encontrado: ")
            print(f"id: {producto.get("id")}, Nombre: {producto.get("nombre")},"
                  f"Precio: {producto.get("precio")},"
                  f"Cantidad: {producto.get("cantidad")}")
            return 
    print("\nProducto NO encontrado")

if __name__ == "__main__":
    while True:
        print(f"""\n--- Menu ---
        1. Mostrar inventario
        2. Agregar nuevo producto
        3. Buscar prodecto por id
        4.salir""")
        opcion = int(input("Proporciona una opcion (1-4): "))
        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
             buscar_producto_por_id()
        elif opcion == 4:
            print("Hasta luego")
            break
        else:
            print("Opcion no validad agrega una opcion validad")