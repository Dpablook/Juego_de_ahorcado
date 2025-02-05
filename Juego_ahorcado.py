# Juego Ahorcado

# Importa el módulo random para elegir palabras al azar
import random

# Diccionario con categorías de palabras y sus respectivas listas
Palabras = {
    "Animales": ["perro", "gato", "ardilla", "murcielago", "cerdo"],
    "Colores": ["azul", "rojo", "verde", "blanco", "negro"],
    "Paises": ["chile", "argentina", "india", "japon", "rusia", "españa", "noruega"],
    "Cosas": ["lluvia", "sol", "mesa", "dados", "cabeza"],
}

# Elige una categoría al azar del diccionario
lista_adivinar = random.choice(list(Palabras.keys()))

# Elige una palabra al azar de la categoría seleccionada
palabra_adivinar = random.choice(Palabras[lista_adivinar])

# Obtiene el número de letras de la palabra a adivinar
numero_de_guiones = len(palabra_adivinar)

# Crea una cadena de guiones bajos "_" de la misma longitud que la palabra
guion = "_"
adivinar = ""

for x in range(numero_de_guiones):
    adivinar = adivinar + guion

# Imprime la palabra a adivinar (esto es solo para pruebas, ¡no debería mostrarse al jugador!)
print(palabra_adivinar)

intentos = 10

while intentos > 0:

    # Imprime el estado inicial del juego
    print("\n")
    print(f"Palabra: {adivinar} ")
    print("Letras intentadas: []")  # Aún no se ha intentado ninguna letra
    print(f"Intentos restantes: {intentos} ")  # Aquí deberías llevar la cuenta de los intentos

    # Pide al jugador que ingrese una letra
    letra = input("Ingresa una letra: ").lower() #convierte la letra en minuscula

    # Busca la posición de la letra ingresada en la palabra a adivinar
    posicion = palabra_adivinar.find(letra)


    #Me perdi, hay que rehacerlo
