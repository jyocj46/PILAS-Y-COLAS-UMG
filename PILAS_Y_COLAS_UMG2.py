import random
import time
from queue import Queue


   

def colas():
    from queue import Queue
    # Generar números aleatorios y agregarlos a la cola
cola = Queue()
for i in range(1000000):
    numero = random.randint(-10000000, 10000000)
    cola.put(numero)

# Extraer los números de la cola y medir el tiempo
inicio1 = time.time()
while not cola.empty():
    numero = cola.get()
fin1 = time.time()


#------------------Fin Colas---------------------------------------------

 # Definir la clase Pila
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    

    # Generar números aleatorios y agregarlos a la pila
pila = Pila()
for i in range(1000000):
    numeros = random.randint(-10000000, 10000000)
    pila.push(numeros)

# Extraer los números de la pila y medir el tiempo
inicio = time.time()
while not pila.esta_vacia():
    numeros = pila.pop()
fin = time.time()


# -----------------Fin pilas---------------------------------------------------------------

def main():
    while True:
        menu = """
        Opciones
        1. Generar un millon de numeros con pilas.
        2. Generar un millon de numeros con Colas.
        3. Salir
        """
        print(menu)
        op = int(input("Ingrese la opción que desea realizar: "))
        if op == 1:
            numeros = 1000000
            Pila()
            # Imprimir el tiempo transcurrido
            print(f"Se extrajeron 1,000,000 de números aleatorios con Pilas en {fin - inicio} segundos.")
        elif op == 2:
            colas()
            # Imprimir el tiempo transcurrido
            print(f"\n Se extrajeron 1,000,000 de números aleatorios con Colas en {fin1 - inicio1} segundos.")
        elif op == 3:
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
