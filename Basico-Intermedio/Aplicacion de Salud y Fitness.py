print("***Aplicacion de Salud y Fitness***")


meta_paso_diarios = 10000
cantidad_por_paso = 0.04

nombre_usuario = input("Cual es tu nombre? ")
pasos_diarios = int(input("Cuantos pasos has caminado hoy?"))

meta_alcanzada = pasos_diarios >= meta_paso_diarios
meta_paso_diarios_txt = "si" if meta_alcanzada else "no"

calorias_quemadas = pasos_diarios * cantidad_por_paso

print(f"\nUsuarios: {nombre_usuario}")
print(f"Paso dados hoy: {pasos_diarios}")
print(f"Calorias quemada: {calorias_quemadas}kcal")
print(f"Meta de pasos diarios alcanzados: {meta_paso_diarios_txt}")
print(f"La meta de pasos diarios es de: {meta_paso_diarios}pasos")
