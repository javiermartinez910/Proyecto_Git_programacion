class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.energia = 100

    def alimentar(self):
        if self.energia >= 100:
            print(f" {self.nombre} ya esta lleno, no puede comer mas.")
        else:
            self.energia += 20
            if self.energia > 100:
                self.energia = 100
                print(f" {self.nombre} esta sobrecargado de energia (100).")
            else:
                print(f" Alimentaste a {self.nombre}. Energia actual: {self.energia}")

    def jugar(self):
        if self.energia <= 0:
            print(f" {self.nombre} esta demasiado debil para jugar. ¡Dejalo descansar!")
        elif self.energia < 30:
            print(f" {self.nombre} intenta jugar, pero esta muy cansado. Mejor que descanse.")
        else:
            self.energia -= 30
            print(f" {self.nombre} jugo felizmente. Energia actual: {self.energia}")
            if self.energia <= 0:
                self.energia = 0
                print(f" {self.nombre} se ha debilitado por completo.")

    def descansar(self):
        if self.energia >= 100:
            print(f" {self.nombre} no quiere dormir, ya tiene mucha energia.")
        else:
            self.energia += 10
            if self.energia > 100:
                self.energia = 100
            print(f" {self.nombre} descanso. Energia actual: {self.energia}")

    def mostrar_estado(self):
        if self.energia > 70:
            estado = "feliz y activo "
        elif self.energia > 30:
            estado = "tranquilo "
        elif self.energia > 0:
            estado = "cansado "
        else:
            estado = "debilitado "
        print("\n" + "="*64)
        print(f"{'ESTADO DE ' + self.nombre.upper():^64}")
        print("="*64)
        print(f"Energía actual: {self.energia}")
        print(f"Estado general: {estado}")
        print("="*64 + "\n")

def cuadro(texto):
    print("=" * 64)
    for linea in texto.split("\n"):
        print(f"{linea.center(64)}")
    print("=" * 64)


cuadro(" Bienvenido puedes jugar con el Cocodrilo ")

nombre = input("Por favor, ingresa el nombre de tu cocodrilo: ")
mascota = Mascota(nombre)

while True:
    menu_texto = (
        "1. Alimentar \n"
        "2. Jugar \n"
        "3. Descansar \n"
        "4. Mostrar estado 📊\n"
        "5. Salir 🚪"
    )
    cuadro(menu_texto)
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        mascota.alimentar()
    elif opcion == "2":
        mascota.jugar()
    elif opcion == "3":
        mascota.descansar()
    elif opcion == "4":
        mascota.mostrar_estado()
    elif opcion == "5":
        cuadro(f" ¡Hasta luego! {mascota.nombre} te extranara ")
        break
    else:
        print("⚠️ Opción no valida, intenta nuevamente.")

