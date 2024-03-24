import random  # Importamos el módulo random para generar números aleatorios

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre  # Inicializamos el atributo 'nombre' del gato con el valor proporcionado al crear una instancia de la clase Gato
        self.hambre = 0  # Inicializamos el nivel de hambre del gato en 0 al crear una instancia de la clase Gato

    def alimentar(self, comida):
        # Método para alimentar al gato
        if comida == "pescado":
            self.hambre -= 3  # Reduce el nivel de hambre en 3 si se alimenta con pescado
            print(f"{self.nombre} disfruta el pescado. ¡Está feliz!")
        elif comida == "pollo":
            self.hambre -= 2  # Reduce el nivel de hambre en 2 si se alimenta con pollo
            print(f"{self.nombre} devora el pollo. ¡Está contento!")
        elif comida == "leche":
            self.hambre -= 1  # Reduce el nivel de hambre en 1 si se alimenta con leche
            print(f"{self.nombre} toma la leche. ¡Está satisfecho!")
        else:
            print(f"{self.nombre} no está interesado en {comida}.")  # Si se da una comida desconocida, el gato no está interesado

        if self.hambre < 0:
            self.hambre = 0  # Aseguramos que el nivel de hambre no sea negativo

    def mostrar_estado(self):
        # Método para mostrar el estado actual del gato
        print(f"{self.nombre} tiene nivel de hambre: {self.hambre}")

def main():
    nombre_gato = input("¡Bienvenido al juego de alimentar al gato! ¿Cómo quieres llamar a tu gato? ")
    gato = Gato(nombre_gato)  # Creamos una instancia de la clase Gato con el nombre ingresado por el usuario

    print(f"{gato.nombre} está esperando a ser alimentado.")

    while True:
        gato.mostrar_estado()  # Mostramos el estado actual del gato
        comida = input("¿Qué quieres alimentar al gato? (pescado/pollo/leche/salir) ").lower()  # Solicitamos al usuario que elija una comida y convertimos la entrada a minúsculas

        if comida == "salir":
            print("¡Gracias por jugar!")
            break  # Si el usuario elige salir, terminamos el juego

        if comida in ["pescado", "pollo", "leche"]:
            gato.alimentar(comida)  # Si el usuario elige una comida válida, alimentamos al gato con esa comida
        else:
            print("Por favor, elige una comida válida.")  # Si el usuario elige una comida no válida, mostramos un mensaje de error

        gato.hambre += random.randint(1, 3)  # Incrementamos el nivel de hambre del gato aleatoriamente después de cada comida

if __name__ == "__main__":
    main()  # Llamamos a la función principal si este script es ejecutado directamente
