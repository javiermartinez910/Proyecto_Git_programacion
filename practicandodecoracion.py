print("\u2554" + "\u2550" * 64 + "\u2557")
print("\u2551" + "BIENVENIDO A TU FICHA PERSONAL".center(64) + "\u2551")
print("\u255A" + "\u2550" * 64 + "\u255D" + "\n")
#pedir datos del usuario-son variables
nombre=input("digite su nombre: ")
edad=input("digite su edad: ")
ciudad=input("en que ciudad vive: ")
profesion=input("digite su profesion: ")
#Mostrar ficha personal
print("\u2554" +"\u2550" * 64 + "\u2557")
print("\u2551" + "FICHA PERSONAL" .center(64) + "\u2551")
print("\u2560" + "\u2550" * 64 + "\u2563")
#mostrar cada dato centrado
print("\u2560" + f"nombre: {nombre}".center(64) + "\u2560")
print("\u2560" + f"edad: {edad}".center(64) + "\u2560")
print("\u2560" + f"ciudad: {ciudad}".center(64) + "\u2560")
print("\u2560" + f"profesion: {profesion}".center(64) + "\u2560")
print("\u255A" + "\u2550" * 64 + "\u255D")
#mensaje final
print("\n" + "gracias por usar este programa".center(66))