# Juego Ahorcado

# Importa el módulo random para elegir palabras al azar
import random

Palabras = {
    "Animales": ["Perro", "Gato", "Ardilla", "Murcielago", "Cerdo", "Tortuga", "Serpiente", "Vaca", "Toro", "Atun"],
    "Colores": ["Azul", "Rojo", "Verde", "Blanco", "Negro", "Naranja", "Violeta", "Celeste", "Gris"],
    "Paises": ["Chile", "Argentina", "India", "Japon", "Rusia", "España", "Noruega", "Corea", "Colombia", "Uruguay", "Sudafrica", "Marruecos"],
    "Cosas": ["Lluvia", "Sol", "Mesa", "Dados", "Cabeza", "Silla", "Celular", "Lapiz", "Humano", "Planeta", "Universo", "Monitor", "Radio"],
}


#arte del ahorcado

ahorcado = [
    """
      +---+
      |    |
      0    |
     /|\   |
     / \   |
           |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]

# Elige una categoría al azar del diccionario
lista_adivinar = random.choice(list(Palabras.keys()))

# Elige una palabra al azar de la categoría seleccionada
palabra_adivinar = random.choice(Palabras[lista_adivinar]).lower()

# Obtiene el número de letras de la palabra a adivinar
numero_de_guiones = len(palabra_adivinar)

# Crea una cadena de guiones bajos "_" de la misma longitud que la palabra
guion = "_"
adivinar = ""
letras_usadas= []
set_usadas = set(letras_usadas)

for x in range(numero_de_guiones):
    adivinar = adivinar + guion

intentos = 6

while intentos > 0:

    # Imprime el estado inicial del juego
    print("\n")
    print(f"Palabra: {adivinar} ")
    print(f"La categoria es: {lista_adivinar} ")
    if set_usadas:
        print("Letras intentadas: " + str(set_usadas))
    else:
        print("Letras intentadas: Aun no tienes letras")
    print(f"Intentos restantes: {intentos} ")  # Aquí deberías llevar la cuenta de los intentos

    # Pide al jugador que ingrese una letra
    letra_ingresada = input("Ingresa una letra: ").lower() #convierte la letra en minuscula

    #Se agrega una letra a la variable para mostrar luego las letras ya usadas
    set_usadas.add(letra_ingresada)

    # Busca la posición de la letra ingresada en la palabra a adivinar
    posicion = palabra_adivinar.find(letra_ingresada)

    if letra_ingresada in palabra_adivinar:
        posiciones = [i for i, letra in enumerate(palabra_adivinar) if letra == letra_ingresada]
        for posicion in posiciones:
            adivinar = adivinar[:posicion] + letra_ingresada + adivinar[posicion+1:]
            print(f"palabra adivinada: {adivinar}")
                
        if "_" not in adivinar:
            print("\n")
            print("Felicidades has ganado")
            palabra_ganadora = palabra_adivinar.capitalize()
            print(f"La palabra es {palabra_ganadora}")
            break

    else:
        intentos = intentos -1
        print(f"La letra es incorrecta, te quedan {intentos} intentos")
        print(f"{ahorcado[intentos]}")

if intentos == 0:
    print("\n")
    print("PERDISTE")
    print(ahorcado[0])
    palabra_perdedora = palabra_adivinar.capitalize()
    print(f"La palabra es {palabra_perdedora}")

