print("***Sistema Reserva de Hotel***")

habitacion = 150.50
habitacion_mar = 190.50

nombre_cliente = input("Nombre del Cliente: ")
dias_estadia = int(input("Dias de estadia: "))
con_vista = input("Con vista al mar (Si/No)? ").strip().lower()

if con_vista == "si":
    reserva = habitacion_mar * dias_estadia
    reserva_txt = "con vista al mar"
else:
    reserva = habitacion * dias_estadia
    reserva_txt = "sin vista al mar"

print("\n---RESERVA DE HOTEL---")
print(f"Cliente: {nombre_cliente}")
print(f"Días de estadía: {dias_estadia}")
print(f"Tipo de habitación: {reserva_txt}")
print(f"Total a pagar: ${reserva:.2f}")
