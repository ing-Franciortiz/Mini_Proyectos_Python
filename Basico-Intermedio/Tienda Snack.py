print("--- Tienda de Snacks---")

inventario = [
    {"id": 1, "nombre": "Papa", "precio": 30},
    {"id": 2, "nombre": "Refresco", "precio": 50},
    {"id": 3, "nombre": "Sanwich", "precio": 80},
    {"id": 4, "nombre": "Jugo", "precio": 25},
    {"id": 5, "nombre": "Chocolate", "precio": 70}
]

def mostrar_inventario():
    print("--- Snacks Disponible ---")
    for producto in inventario:
        print(f"id: {producto.get('id')}, -> {producto.get('nombre')},"
              f"$ {producto.get('precio')}")
        
carrito = []
def comprar_snack():
    comprar_id = int(input("Que snack quieres comprar(id): "))
    for producto in inventario:
        if producto.get("id") == comprar_id:
            carrito.append(producto)
            print(f"Snack agregado: id: {producto.get('id')}, Nombre: {producto.get('nombre')}," f"Precio: {producto.get('precio')}") 
            return 
    print("\nProducto NO encontrado")


def mostrar_ticket():
    if not carrito:
        print("\nEl carrito esta vacio")
        return
    print("\n--- Ticket de compra ---")
    total = 0 

    for producto in carrito:
        nombre = producto['nombre']
        precio = producto ['precio']
        print(f"{nombre} - ${precio}")
        total += precio
    print(f"\nTotal a pagar : ${total}")

if __name__ == "__main__":
    while True:
        print(f"""\nMenu:
              1. Mostrar Snacks
              2. Comprar Snack
              3. Mostar ticket
              4. Salir""")
        opcion = int(input("Escoge una opcion: "))
        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print("Gracias por su compra")
            break
        else:
            print("Opcion no valida")