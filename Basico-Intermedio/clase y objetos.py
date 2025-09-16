class Persona :
    contador_personas = 0 


    def __init__(self, nombre, apellido):
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido


    def mostrar_persona(self):
        print(f" Persona: {self.id}, {self.nombre}, {self.apellido}")

if __name__ == "__main__":
    print("*** Ejemplo Contador de Objetos de tipo Persona ***")
    persona1 = Persona("Gerardo", "Perez")
    persona1.mostrar_persona()
    persona2 = Persona("Mia", "Perez")
    persona2.mostrar_persona()


    print(f"Contador Objetos Persona: {Persona.contador_personas}")
    