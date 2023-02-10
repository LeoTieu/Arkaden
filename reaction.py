
# importerar nödvändiga moduler
import random
import time
import msvcrt
import os
import sys

# definierar spelet
def reaction_game():
    print("Välkommen till Reaktionsspelet!")
    print("När bokstaven visas på skärmen trycker du på motsvarande tangent på tangentbordet så snabbt du kan.")
    print("Du kommer att få mindre poäng ju längre tiden går, så se till att vara snabb!")
    print("Du får 10 sekunder att få 300 poäng sammanlagt.")
    print("Är du redo att börja? Tryck på 'y' för att starta.")

    # om spelaren inte trycker på "y" så stängs spelet av
    start = input().lower()
    if start != 'y':
        print("Hejdå!")
        time.sleep(5)
        return "not passed"
    # variabler
    points = 0
    start_time = time.time()
    end_time = start_time + 10
    letters = ['a', 's', 'd', 'f', 'j', 'k', 'l', 'u']
    
    while True:
        # skriver "game over" om tiden tar slut
        if time.time() > end_time:
            print(f"Game over! Totala poäng: {points}")
            time.sleep(5)
            return "not passed"
        letter = random.choice(letters)
        print(letter)
        # gör så att spelaren inte behöver trycka på enter efter varje tangent är tryckt
        user_input = msvcrt.getch().decode().lower()
        # ger och visar spelaren poängen om rätt bokstav är skriven beroende på hur snabb spelaren var
        if user_input == letter:
            reaction_time = time.time() - start_time
            points += int(1 / reaction_time * 100)
            print(f"{int(1 / reaction_time * 100)} poäng. Totala poäng: {points}")
        # skriver vinst om spelaren få över 300 innan tiden tar slut
        if points >= 300:
            print(f"Du vann! Du fick {points} sammanlagt")
            time.sleep(5)
            return "pass"

# kallar på funktionerna
if __name__ == '__main__':
    reaction_game()
    