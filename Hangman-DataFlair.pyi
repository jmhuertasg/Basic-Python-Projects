import random
import time

# IPasos iniciales para invitar al juego:
print("\nBienvenido al juego del ahorcado\n")
name=input("Introduzca su nombre: ")
print("Hola "+ name + "! Buena Suerte!")
time.sleep(2)
print("El juego va a comenzar!\n Vamos a jugar al ahorcado!")
time.sleep(3)

# Los parametros requeridos para ejecutar el juego:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["january","border","imaqge",
                      "film","promise","plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends:
def play_loop():
    global play_game
    play_game = input("Quieres jugar otra vez? y = yes, n = no \n")
    while play_game not in ["y","n","Y","N"]:
        play_game = input("Quieres jugar otra vez? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Gracias por jugar! Nosotros esperamos que vuelvas de nuevo!")
        exit()
# Inicializacion de todaslas condiciones requeridas para el juego
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("Esta es la palabra del ahorcado: "+ display + " Introduce tu opcion: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Entrada invalida, pruebe mas tarde\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index+ 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Prueba otra letra.\n")
    else:
        count +=1

        if count == 1:
            time.sleep(1)
            print("  __________\n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__\n")
            print("Mala eleccion.  "+ str(limit - count) + "turnos disponibles\n")
        elif count == 2:
            time.sleep(1)
            print("  __________\n"
                  "  |        |\n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__\n")
            print("Mala eleccion.  "+ str(limit - count) + "turnos disponibles\n")
        elif count == 3:
            time.sleep(1)
            print("  __________\n"
                  "  |        |\n"
                  "  |        |\n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__\n")
            print("Mala eleccion.  "+ str(limit - count) + "turnos disponibles\n")
        elif count == 4:
            time.sleep(1)
            print("  __________\n"
                  "  |        |\n"
                  "  |        |\n"
                  "  |        O\n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__\n")
            print("Mala eleccion.  "+ str(limit - count) + "turnos disponibles\n")
        elif count == 5:
            time.sleep(1)
            print("  __________\n"
                  "  |        |\n"
                  "  |        |\n"
                  "  |        O\n"
                  "  |      / | \ \n"
                  "  |       / \ \n"
                  "  |     \n"
                  "__|__\n")
            print("Mala eleccion.  Estas ahorcado!!!!!!!\n")
            print("La palabra a adivinar era :", already_guessed,word)
            play_loop()

        if word == '_' * length:
            print("Enhorabuena!!!!!Tu has acertado la palabra correcta!!!!!")
            play_loop()
        elif count != limit:
            hangman()

main()

hangman()