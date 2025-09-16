class Empleado:
    contador_empleado = 0  # Contador de empleados

    def __init__(self, nombre, departamento):
        Empleado.contador_empleado += 1
        self.id = Empleado.contador_empleado  # ID único para cada empleado
        self.nombre = nombre
        self.departamento = departamento

    @classmethod
    def obtener_total_empleador(cls):
        return cls.contador_empleado
