# Enkelt spel gjort: Leo Tieu
# Lånad kod - ingen

def meteorer():
    # Moduler
    from msvcrt import getch
    import os
    import random
    import time


    # Funktioner
    def ship_mover(ship_column):
        """Ändrar skeppets position"""
        ship_top_row = ["   "] * 9
        ship_bottom_row = ["   "] * 9

        ship_top_row[ship_column] = " X "
        ship_bottom_row[ship_column] = "XXX"
        return (ship_top_row, ship_bottom_row)


    def animation(points, ship_top_row, ship_bottom_row, list_of_rows, bullets):
        """Printar ut allt, den ger alltså ut bilden"""
        print(f"points: {points}           bullets: {bullets}")

        for row in list_of_rows:
            for i in row:
                print(i, end="")
            print("")
        for i in ship_top_row:
            print (i, end="")
        print("")

        for i in ship_bottom_row:
            print (i, end="")
        print("")


    def meteor_updator(frame_counter):
        '''Uppdaterar alla meteor rader.'''
        if frame_counter == 1:
            meteor_updator_extra()
            new_meteor_coordinate = random.randint(0,8)
            row_1[new_meteor_coordinate] = " o "
        else:
            meteor_updator_extra()

        if frame_counter == 3:
            frame_counter = 1
        else:
            frame_counter = frame_counter + 1
        return (frame_counter)


    def meteor_updator_extra():
        '''uppdaterar meteorerna så att de är på deras rätta ställe'''
        for row in list_of_rows:
            new_meteor_coordinates = 10
            try:
                #Om det finns en meteor blir "new_meteor_coordinates" en y koordinat. 
                new_meteor_coordinates = row.index(" o ")
                row[new_meteor_coordinates] = "   "
            except:
                None
            try: 
                #Om det inte finns en meteor kommer new_meteor_coordinates vara 10 vilket innebär att ingenting kommer hända
                row[old_meteor_coordinates] = " o "
            except: 
                None
            old_meteor_coordinates = new_meteor_coordinates


    def laser(ship_column):
        '''Skjuter en laser och returnerar poängen som man fick'''
        hits = 0
        for row in list_of_rows:
            try:
                #Kollar hur många meteorer som finns i raden man skjöt på
                meteor_coordinates = row.index(" o ")
                if ship_column == meteor_coordinates:
                    hits += 1
            except:
                None
            row[ship_column] = " | "
        animation(points, ship_top_row, ship_bottom_row, list_of_rows, bullets)
        time.sleep(0.05)
        os.system('cls')
        for row in list_of_rows:
            row[ship_column] = "   "
        return hits
            

    #Start skärm
    os.system('cls')
    print('''
    -----------------------------------------------
    |                 Meteorer                    |
    |                                             |
    |                                             |
    |           För regler, tryck på A            |
    |  Annan valfri knapp för att starta spelet   |
    |                                             |
    |                                             |
    | (1) credit                                  |
    -----------------------------------------------
    ''')

    keyboard_input = (ord(getch()))
    print(keyboard_input)
    #97 == a
    if keyboard_input == 97:
        os.system('cls')
        print('''
    -----------------------------------------------                   
    |   Du börjar med 18 skott. För varje meteor  |
    | du träffar så får du 5 poäng. Max 100 poäng |
    |                                             |
    |             gå till vänster - A             |
    |             gå till höger - D               |
    |                Skjuta - L                   |
    |                                             |
    |   Tryck på valfri knapp för att fortsätta   |
    -----------------------------------------------
        ''')
        keyboard_input = (ord(getch()))
    os.system('cls')


    #Deklaration av variabler och listor för framtida användning
    frame_counter = 1
    ship_column = 4
    points = 0
    bullets = 18
    three_digits = 100
    two_digits = 10
    screen_fixer = "NotAssigned"

    # Keyboard inputs from Getch
    A = 97
    B = 98
    D = 100
    L = 108

    row_1 = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    row_2 = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    row_3 = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    row_4 = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    row_5 = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    row_6 = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    row_7 = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    row_8 = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    row_9 = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    ship_top_row = ["   ", "   ", "   ", "   ", " X ", "   ", "   ", "   ", "   "]
    ship_bottom_row = ["   ", "   ", "   ", "   ", "XXX", "   ", "   ", "   ", "   "]

    list_of_rows = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9]
    

    animation(points, ship_top_row, ship_bottom_row, list_of_rows, bullets)

    while not((bullets <= 0) or (points == 100)):
        keyboard_input = (ord(getch()))
        if keyboard_input == A:
            if ship_column > 0:
                os.system('cls')
                ship_column = ship_column - 1
                frame_counter = meteor_updator(frame_counter)
                ship_top_row, ship_bottom_row = ship_mover(ship_column)
                animation(points, ship_top_row, ship_bottom_row, list_of_rows, bullets)
        elif keyboard_input == D:
            if ship_column < 8:
                os.system('cls')
                ship_column = ship_column + 1
                frame_counter = meteor_updator(frame_counter)
                ship_top_row, ship_bottom_row = ship_mover(ship_column)
                animation(points, ship_top_row, ship_bottom_row, list_of_rows, bullets)
        elif keyboard_input == 108:
            os.system('cls')
            points = points + (laser(ship_column)*5)
            if points > 100:
                points = 100
            bullets += -1
            animation(points, ship_top_row, ship_bottom_row, list_of_rows, bullets)

    #Slut skärm
    os.system('cls')
    for _ in range(4):
        animation(points, ship_top_row, ship_bottom_row, list_of_rows, bullets)
        time.sleep(0.3)
        os.system('cls')
        time.sleep(0.3)
    time.sleep(0.5)


    if points < two_digits:
        screen_fixer = "                "
    elif points < three_digits:
        screen_fixer = "               "
    elif points == three_digits:
        screen_fixer = "              "

    print(f'''
        -----------------------------------------------                   
        |                                             |
        |         {points} poäng / 100 poäng {screen_fixer}|
        |                                             |
        |                                             |
        |         För att sluta spela, tryck a        |
        |         För att köra igen, tryck b          |
        |                                             |
        |                                             |
        -----------------------------------------------
    ''')
    time.sleep(0.2)

    while True:
        keyboard_input = (ord(getch()))
        if keyboard_input == A:
            return points
        elif keyboard_input == B:
            return meteorer()


if __name__ == '__main__':
    meteorer()
