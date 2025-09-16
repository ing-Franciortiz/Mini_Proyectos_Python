from Class_Empresa import Empresa
from Class_Empleado import Empleado

print("*** Sistema de Empleados ***")

empresa1 = Empresa("Global Mentoring")

empresa1.contratar_empleado("Juan", "Ventas")
empresa1.contratar_empleado("Pedro", "Marketing")
empresa1.contratar_empleado("Maria", "Ventas")
empresa1.contratar_empleado("Ana", "Recursos Humanos")

# Total general de empleados (todas las instancias creadas)
print(f"\nTotal de empleados registrados (contando todas las instancias de Empleado): {Empleado.obtener_total_empleador()}")

# Mostrar los empleados de esta empresa
empresa1.obtener_total_empleados()

# Número de empleados en Ventas
print(f"\nEmpleados en el departamento de Ventas: {empresa1.obtener_numero_empleados_departamento('Ventas')}")
