class Animal :
    def comer(self):
        print("Como muchas veces el dia")


    def dormir(self):
        print("Duermo muchas horas")



class Perro(Animal):

    def hacer_sonido(self):
        print("Puedo ladrar")

    def dormir(self):
        print("Duermo 15 hora  dia")

print("*** Ejemplo de Herencia en Python ***")
print("Clase Padre, Soy un Animal")
animal1 = Animal()
animal1.comer()
animal1.dormir()


print("\nClase Hija, soy un Perro")
perro1 = Perro()
perro1.dormir()
perro1.comer()
perro1.hacer_sonido()