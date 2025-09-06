print("***Sistema de tienenda***")
print()

#Precios de los produtos 
precio_leche = float(input("Precio leche: "))
precio_pan= float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platano = float(input("Precio platano: "))
precio_papa = float(input("Precio papa: "))
precio_aguacate = float(input("Precio aguacate: "))
precio_azucar = float(input("Precio azucar: "))
subtotal = precio_leche + precio_pan + precio_lechuga +precio_platano +precio_papa + precio_aguacate + precio_azucar

precio_descuento = 400
membresia = input("Tiene la membresia de la tienda (Si/No)?").strip().lower()

porcentaje_descuento = 0.20 if subtotal >= precio_descuento and membresia == "si" else 0.10 if subtotal >= precio_descuento and membresia !=  "si" else 0

monto_descuento = subtotal * porcentaje_descuento
impuesto = (subtotal - monto_descuento) * 0.16
costo_total_compra = subtotal - monto_descuento + impuesto

print(f"""
subtotal: ${subtotal:.2f}
descuento: ${monto_descuento:.2f}
impuesto(16%): ${impuesto:.2f}
monto total de compra: ${costo_total_compra:.2f}
""")
