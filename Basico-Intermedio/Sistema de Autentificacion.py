print("***Sistema de Autentificaion***")
print()

usuario = "admin"
password = "1234"

usuario_agregado = input("Cual es tu Usuario: ")
password_agregado = input("Cual es tu password: ")


if usuario_agregado == usuario and password_agregado == password :
    print("Bienvenido al Sistema")
elif usuario_agregado == usuario:
    print("Password incorrecto")
elif password_agregado == password:
    print("Usuario incorrecto")
else:
    print("Usuario y password incorrecto")
