# Arkaden
# Gjord av: Albin, Raphael, Kevin och Leo
# Huvudspelet gjort av: Leo

# Alla spel
from MiniQuiz import quiz_game
from Meteorer import meteorer
from Snack import Snack
from reaction import reaction_game
from pong import main_menu

import time
import os


quiz_game()

class Game:
    def __inint__(self, max_points, current_points, price, game, is_locked):
        self.max_points = max_points
        self.current_points = current_points
        self.price = price
        self.game = game
        self.is_locked = is_locked

Meteorer = Game("pass", 100, 0, "free", meteorer(), False)
Quiz = Game("pass", "not passed", 25, quiz_game(), True)
Reaction = Game("pass", "not passed", 25, reaction_game(), True)
GetASnack = Game("pass", "not passed", 50, Snack(), True)
Pong = Game("pass", "not passed", "free", main_menu(), False)


def can_enter_room_2():
    """Kollar om spelaren kan gå in i spel rum 2"""
    if Quiz.current_points == "passed" and Reaction.current_points == "passed":
        return "game_room_2"
    else:
        print(f'''
Du behöver klara:
Quiz och Reaktion för att komma till spel rum 2.

Quiz: {Quiz.current_points} / {Quiz.max_points}
Reaction Game: {Reaction.current_points} / {Reaction.max_points}
''')
    time.sleep(4)
    return "game_room_1"


def buy_game(game):
    """Funktion för att köpa ett spel"""
    global UserPoints
    if game.is_locked == False:
        if UserPoints >= game.price:
            UserPoints -= game.price
            game.is_locked = False


def buy_room():
    """Körs om spelaren är i köp rummet"""
    print('''
Vad vill du göra?
1 - Kolla hur mycket poäng du har fått på olika spel.
2 - Låsa upp nya spel. 

3 - Gå till spelrum nummer 1
    ''')
    user_input = input()

    if user_input == "1":
        print(f'''
Meteorer: {Meteorer.current_points} / {Meteorer.max_points}
Quiz: {Quiz.current_points} / {Quiz.max_points}
Reaction Game: {Reaction.current_points} / {Reaction.max_points}
Snack: {Snack.current_points} / {Snack.max_points}
temporary_game: {TemporaryPointsGame1}/50
Pong: {Pong.current_points} / {Pong.max_points}
Snake: ?

Gå tillbaka - 1
''')
        input()
    elif user_input == "2":
        while True:
            print(f'''

Points: {UserPoints}
Quiz: {Quiz.price} points
Reaction Game: {Reaction.price} points
Snack: {Snack.price} points

Gå tillbaka - 1

Lås upp Quiz - 2
Lås upp Reaction - 3
Lås upp Snack - 4
    ''')
            user_input = input()
            if user_input == "1":
                return "game_room_1"
            elif user_input == "2":
                buy_game(Quiz)
            elif user_input == "3":
                buy_game(Reaction)
            elif user_input == "4":
                buy_game(Snack)
            else:
                print("Var vänlig och skriv en korrekt inmatning")


def game_room_1():
    """Körs om spelaren är i rum 1"""
    while True:
        os.system('cls')
        print('''
Vad vill du göra? (OBS! Svara endast med 1 siffra)
1 - Meteorer
2 - Quiz
3 - Reaktions spel

4 - Gå till Köp rummet
5 - Gå till spelrum nummer 2
        ''')
        user_input = input()
        if user_input == "1":
            UserResult = Meteorer.game
            if UserResult > Meteorer.current_points:
                global UserPoints
                UserPoints = UserResult - Meteorer.current_points
                Meteorer.current_points = UserResult

        if user_input == "2":
            UserResult = Quiz.game
            if UserResult == "pass":
                Quiz.current_points = "pass"        
        if user_input == "3":
            UserResult = Reaction.game
            if UserResult == "pass":
                Reaction.current_points = "pass"        
        if user_input == "4":
            return "buy_room"
        if user_input == "5":
            return can_enter_room_2()
        else:
            print("Var vänlig och skriv en korrekt inmatning")
            time.sleep(cooldown)


def game_room_2():
    """Körs om spelaren är i rum 2"""
    while True:
        os.system('cls')
        print('''
Vad vill du göra? (OBS! Svara endast med 1 siffra)
1 - Get a snack
2 - Pong
3 - Snake

4 - Spelrum nummer 1
        ''')
        user_input = input()
        if user_input == "1":
            UserResult = GetASnack.game
            if UserResult == "pass":
                GetASnack.current_points = "pass"
        if user_input == "2":
            UserResult = GetASnack.game
            if UserResult == "pass":
                GetASnack.current_points = "pass"
        if user_input == "3":
            print("Finns inte just nu")
            time.sleep(cooldown)
        if user_input == "4":
            return "game_room_1"
        else:
            print("Var vänlig och skriv en korrekt inmatning")
            time.sleep(cooldown)
            os.system('cls')


PlayerPosition = "game_room_1"
TemporaryPointsGame1 = 0
TemporaryPriceGame1 = 50

UserPoints = 0
UserPointsGotten = 0

cooldown = 0.2
print("Hej och välkommen till arkaden!")
time.sleep(cooldown)
print("Du har fastnat i denna arkad och måste komma ut!")
time.sleep(cooldown)
print("För att komma ut måste du klara alla mini spel!")
time.sleep(cooldown)
print("Lycka till!")
os.system('cls')
time.sleep(cooldown)

while True:
    if PlayerPosition == "buy_room":
        PlayerPosition = buy_room()
    if PlayerPosition == "game_room_1":
        PlayerPosition = game_room_1()
    if PlayerPosition == "game_room_2":
        PlayerPosition = game_room_2()
