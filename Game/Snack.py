import os
import time
import sys
import random
from pystyle import Colors, Colorate, Center, Box, Write
import playsound

def Snack():

    # En fungerande plånbok.
    class Wallet:
        def __init__(self, balance=130):
            self.balance = balance

    # Funktion för att lägga till pengar till plånboken
        def add_funds(self, amount):
            self.balance += amount

    # Funktion för att ta bort pengar i plånboken
        def make_payment(self, amount):
            if amount > self.balance:
                # Ifall du inte har tillräckligt med pengar kommer detta meddelandet komma up.
                raise ValueError("Du har inte tillräckligt med pengar.")
            self.balance -= amount     

    wallet = Wallet()

    # Mina varaiblar
    usr_answ5 = "ö"
    usr_answ11 = "ö"
    usr_answ12 = "ö"


    # Jag har använt mig av pystyle för att göra många olika varianter av linjer mer kreativa.
    print(Box.Lines("Tjenare och välkommen till 'Hungrig klockan 3!'\n"))
    # time.sleep är hur länge konsollen ska vänta innan den skriver nästa linje.
    time.sleep(.85)

    Write.Print("\nVi kommer att börja med instruktioner för hur du spelar.", Colors.blue_to_green, interval=0.025)
    time.sleep(.85)

    Write.Print("\nFör att gå fram så skriver du 'W' i konsollen, för att gå till höger skriver du 'D' och för att gå till vänster skriver du 'A'\n", Colors.blue_to_green, interval=0.025)
    time.sleep(.85)

    Write.Print("\nNär du väl är inne i ett rum kommer du kunna gå och kolla i rummet för att se om du hittar något intressant.", Colors.blue_to_green, interval=0.025)
    time.sleep(.85)

    Write.Print("\nDu kommer att befinna dig i ditt hus där du vaknar klockan 3 på morgonen och känner dig väldigt hungrig. Du tänker att det bästa alternativet är att gå och handla och det gör du men på vägen märker du att konstiga saker händer.\n", Colors.blue_to_green, interval=0.025)
    time.sleep(.85)

    Write.Print("\nNu är frågan, vill du fortsätta?\n", Colors.blue_to_green, interval=0.025)
    time.sleep(.2)

    usr_answ = int(Write.Input("För att fortsätta kan du skriva 1, om du vill lämna spelet skriver du 2. ", Colors.blue_to_green))
    time.sleep(.6)

    if usr_answ == 1:
        Write.Print("\nBra val.", Colors.blue_to_green, interval=0.025)
    elif usr_answ == 2:
        return "fail"
    else: 
        Write.Print("\nDu har inte angett ett av alternativen.", Colors.blue_to_green, interval=0.025)
    time.sleep(3)

    time.sleep(.95)
    Write.Print("\nDu vaknar en kall och mörkt natt och märker att du är sugen på något.\n", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)
    Write.Print("Du ställer dig upp och sätter på dig dina kläder.\n", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)
    Write.Print("Du tänker för dig själv om du ska gå till köket eller hallen.\n", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)

    while True:
        try:
            usr_answ1 = int(input("\nSkriv in 1 för att gå till köket. Skriv in 2 för att gå till hallen. "))
        except ValueError:
            usr_answ1 = -1
        
        if usr_answ1 == 1:
                time.sleep(.95)
                Write.Print("\nDu går till till köket och öppnar kylen och ser att den är helt tom.", Colors.blue_to_green, interval=0.025)
                break

        elif usr_answ1 == 2:
                time.sleep(.95)
                Write.Print("\nDu går till till hallen för att klä på dig eftersom du kommer ihåg att kylen är helt tom.", Colors.blue_to_green, interval=0.025)
                break

        else:
                time.sleep(.5)
                Write.Print("\nDu har inte angett ett av valen.", Colors.blue_to_green, interval=0.025)
                time.sleep(.5)

        time.sleep(2)
        Write.Print("\nDu tänker att du kan gå till butiken för att köpa något. Du går då till hallen och då hör du ett knack på dörren.", Colors.blue_to_green, interval=0.025)

    while True:
        try:
            usr_answ2 = int(input("\nSkriv in 1 ifall du vill öppna dörren och se om det är någon där. Skriv in 2 om du inte vill öppna dörren. "))
        except ValueError:
            usr_answ2 = -1

            if usr_answ2 == 1:
                time.sleep(.95)
                Write.Print("\nDu går till till köket och öppnar kylen och ser att den är helt tom.", Colors.blue_to_green, interval=0.025)
                time.sleep(.95)
                Write.Print("\nIstället går du mot dörren för att gå till affären.", Colors.blue_to_green, interval=0.025)
                break

            elif usr_answ2 == 2:
                time.sleep(.95)
                Write.Print("\nDu går till till hallen för att klä på dig eftersom du kommer ihåg att kylen är helt tom.", Colors.blue_to_green, interval=0.025)
                time.sleep(.95)
                Write.Print("\nDu går mot dörren och håller på att gå ut.", Colors.blue_to_green, interval=0.025)
                break

            else:
                time.sleep(.5)
                Write.Print("\nDu har inte angett ett av valen.", Colors.blue_to_green, interval=0.025)
                time.sleep(.5)


    time.sleep(.95)
    Write.Print("\nNär du väl gott ut känner du hur någon kollar på dig.", Colors.blue_to_green, interval=0.025)
    time.sleep(.90)
    Write.Print("\nDu kollar runt omkring dig men ser inget.", Colors.blue_to_green, interval=0.025)
    time.sleep(.90)
    Write.Print("\nDu börjar sakta men säkert gå vidare.", Colors.blue_to_green, interval=0.025)
    time.sleep(.90)
    Write.Print("\nEfter att du gått ett tag hör du något prassla i en buske vid dig.", Colors.blue_to_green, interval=0.025)

    while True:
        try:
            usr_answ3 = int(Write.Input("\nSkriv in 1 ifall du vill gå fram till busken. Skriv in 2 om du inte vill gå fram till busken. ", Colors.blue_to_green, interval=0.025))
        except ValueError:
            usr_answ3 = -1

        if usr_answ3 == 1:
            time.sleep(0.95)
            Write.Print("\nDu går fram till busken och en katt hoppar fram.", Colors.blue_to_green, interval=0.025) 
            # Spelar ett katt ljud.
            playsound.playsound("cat.mp3")
            time.sleep(.55)
            Write.Print("\nDu blir rädd och hoppar bak.", Colors.blue_to_green, interval=0.025)
            time.sleep(.95)
            Write.Print("\nKatten springer bort och du fortsätter gå till butiken.", Colors.blue_to_green, interval=0.025)
            time.sleep(3)
            break

        elif usr_answ3 == 2:
            time.sleep(.95)
            Write.Print("\nDu går förbi busken och fortsätter att gå till butiken.", Colors.blue_to_green, interval=0.025)
            time.sleep(3)
            break
        
        else:
            time.sleep(.5)
            Write.Print("\nDu har inte angett ett av valen.", Colors.blue_to_green, interval=0.025)
            time.sleep(.5)

    Write.Print("\nEfter tio minuter av att gå till butiken har du haft oroliga känslor ifall någon kollar på dig.", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)
    Write.Print("\nEfter att du gått ett tag så kommer du fram till butiken", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)
    Write.Print("\nFramför butiken ser du en tiggare.", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)

    while True:
        try:
            usr_answ4 = int(Write.Input("\nSkriv in 1 ifall du vill ge tiggaren en slant. Skriv in 2 om du inte vill gå fram till honom. ", Colors.blue_to_green, interval=0.025))
        except ValueError:
            usr_answ4 = -1
        
        if usr_answ4 == 1:
            wallet.make_payment(10)
            time.sleep(.95)
            Write.Print("\nDu ger tiggaren en slant och han tackar dig glatt.", Colors.blue_to_green, interval=0.025)
            time.sleep(.95)
            break

        elif usr_answ4 == 2:
            time.sleep(.95)
            Write.Print("\nDu går förbi tiggaren och han blir ledsen.", Colors.red, interval=0.025)
            time.sleep(.90)
            break

        else:
            time.sleep(.5)
            Write.Print("\nDu har inte angett ett av valen.", Colors.blue_to_green, interval=0.025)
            time.sleep(.5)

    Write.Print("\nNu är du inne i butiken och kan gå åt 3 olika håll.", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)

    while usr_answ5.lower() not in ["w", "a", "d"]:
        usr_answ5 = str(Write.Input("\nOm du vill gå fram skriv 'W', 'A' för vänster och 'D' för höger. ", Colors.blue_to_green, interval=0.025))
        time.sleep(.95)

        if usr_answ5.lower() == "w":
            time.sleep(.95)
            Write.Print("\nDu har nu gått frammåt och ser ingenting som ser gott ut för dig", Colors.blue_to_green, interval=0.025)
            time.sleep(.95)
            Write.Print("\nVill du fortsätta frammåt?", Colors.blue_to_green, interval=0.025)
            time.sleep(.65)
            
            usr_answ6 = str(Write.Input("\nOm du vill gå fram skriv 'Y' eller 'N' om du inte vill. ", Colors.blue_to_green, interval=0.025))
            if usr_answ6.lower() == "y":
                time.sleep(.95)
                Write.Print("\nDu gick fram lite mer och träffade en tant.", Colors.blue_to_green, interval=0.025)
                time.sleep(.95)
                Write.Print("\n'Hejsan, vad är ditt namn då?'", Colors.purple, interval=0.025)
                time.sleep(.95)
                Write.Print(" Frågar tanten.", Colors.blue_to_green, interval=0.025)
                time.sleep(.95)
                namn = Write.Input("\nAnge ditt namn: ", Colors.blue_to_green, interval=0.025)
                time.sleep(.95)
                Write.Print(f"\n'Vad kul att träffa dig {namn}'", Colors.purple, interval=0.025)
                time.sleep(.45)
                # Namnet fick jag från min polare Isak AKA Zombiemops.
                Write.Print(" 'Mitt namn är Karin'", Colors.purple, interval=0.025)
                time.sleep(.95)
                Write.Input(" 'Vad är du här för då?' ", Colors.purple, interval=0.025)
                time.sleep(.95)
                Write.Print("\n'Jasså, det var kul då.'", Colors.purple, interval=0.025)
                time.sleep(.95)
                Write.Print("\n'Själv försöker jag ta lite kex men kan inte nå dem.'", Colors.purple, interval=0.025)
                time.sleep(.95)
                Write.Print("\n'Skulle du kunna hjälpa mig och ta ner dem?' ", Colors.purple, interval=0.025)
                time.sleep(.95)
                usr_answ9 = str(Write.Input("\nOm du vill hjälpa damen skriv 'Y' eller 'N' om du inte vill. ", Colors.blue_to_green, interval=0.025))
                
                if usr_answ9.lower() == "y":
                    time.sleep(.95)
                    Write.Print("\nDu hjälper henne ta ner dem och hon tackar dig och ger dig 30kr.", Colors.blue_to_green, interval=0.025) 
                    time.sleep(.95)
                    Write.Print(f"\nDu har nu {wallet.balance}kr", Colors.blue_to_green, interval=0.025)
                    time.sleep(.95)
                    wallet.add_funds(30)
                    Write.Print("\nDu tackar henne och sedan börjar du gå.", Colors.blue_to_green, interval=0.025)
                    time.sleep(.95)
                    break
                
                elif usr_answ9 == "n":
                    time.sleep(.95)
                    Write.Print("Tanten blir sur och går iväg")
                    break

                else: 
                    Write.Print("\nDu har inte angett ett av alternativen.", Colors.blue_to_green, interval=0.025)
                    
            elif usr_answ6.lower() == "n":
                time.sleep(.95)
                Write.Print("\nDu gick tillbaka och undrar vart du ska nu.", Colors.blue_to_green, interval=0.025)

            else: 
                Write.Print("\nDu har inte angett ett av alternativen.", Colors.blue_to_green, interval=0.025)
                
        elif usr_answ5.lower() == "a":
            time.sleep(.95)
            Write.Print("\nDu gick till vänster och ser lite munkar.", Colors.blue_to_green, interval=0.025)  
            time.sleep(.95)
            
            usr_answ7 = str(Write.Input("\nOm du vill gå fram skriv 'Y' eller 'N' om du inte vill. ", Colors.blue_to_green, interval=0.025))
            if usr_answ7.lower() == "y":
                time.sleep(.95)
                Write.Print("\nDu gick fram till munkarna och känner dig lite sugen.", Colors.blue_to_green, interval=0.025)
                time.sleep(.95)
                Write.Print(f"\nDu ser på en skyllt att de kostar 20kr för 3 stycken. Du har {wallet.balance}kr", Colors.blue_to_green, interval=0.025)
                
                usr_answ14 = str(Write.Input("\nOm du vill ta några munkar skriv 'Y' eller 'N' om du inte vill. ", Colors.blue_to_green, interval=0.025))
                if usr_answ14 == "y":
                    wallet.make_payment(20)
                    time.sleep(.95)
                    Write.Print(f"\nDu tog några munkar och har nu {wallet.balance}kr", Colors.blue_to_green, interval=0.025)
                    break

                elif usr_answ14 == "n":
                        break

                else: 
                    Write.Print("\nDu har inte angett ett av alternativen.", Colors.blue_to_green, interval=0.025)

            if usr_answ14 == "n":
                break

            else: 
                Write.Print("\nDu har inte angett ett av alternativen.", Colors.blue_to_green, interval=0.025)

        elif usr_answ5.lower() == "d":
            time.sleep(.95)
            Write.Print("\nDu går till höger och ser massa chokladbars, det finns 3 alternativ.", Colors.blue_to_green, interval=0.025)
            time.sleep(.95)
            Write.Print("\nDet finns Mars, Twix och Snickers.", Colors.blue_to_green, interval=0.025)
            time.sleep(.95)
            
            usr_answ16 = Write.Input("\nFör Mars skriv 1, för Twix skriv 2 och för Snickers skriv 3. ", Colors.blue_to_green, interval=0.025)
            if usr_answ16 == "1":
                wallet.make_payment(7)
                time.sleep(.95)
                Write.Print("\nDu valde att ta en Mars och har betalat 7kr för den", Colors.blue_to_green, interval=0.025)
                time.sleep(.75)
                Write.Print(f"\nDu har nu {wallet.balance}kr", Colors.blue_to_green, interval=0.025)
                break

            elif usr_answ16 == "2":
                wallet.make_payment(7)
                time.sleep(.95)
                Write.Print("\nDu valde att ta en Twix och har betalat 7kr för den", Colors.blue_to_green, interval=0.025)
                time.sleep(.75)
                Write.Print(f"\nDu har nu {wallet.balance}kr", Colors.blue_to_green, interval=0.025)
                break

            elif usr_answ16 == "3":
                wallet.make_payment(7)
                time.sleep(.95)
                Write.Print("\nDu valde att ta en Snickers och har betalat 7kr för den", Colors.blue_to_green, interval=0.025)
                time.sleep(.75)
                Write.Print(f"\nDu har nu {wallet.balance}kr", Colors.blue_to_green, interval=0.025)
                break

            else: 
                Write.Print("\nDu har inte angett ett av alternativen.", Colors.blue_to_green, interval=0.025)

    Write.Print("\nDu fortsätter gå vidare in i butiken.", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)

    while usr_answ12.lower() not in ["w", "a", "d"]:
        usr_answ12 = str(Write.Input("\nOm du vill gå fram skriv 'W', 'A' för vänster och 'D' för höger. ", Colors.blue_to_green, interval=0.025))
        time.sleep(.95)
        
        if usr_answ12.lower() == "w":
            time.sleep(.95)
            Write.Print("\nDu gick fram i butiken och ser att det står en stor korg med massa chips.", Colors.blue_to_green, interval=0.025)
            time.sleep(.95)
            Write.Print("\nDu går fram till korgen och tänker för dig själv om du vill ha chips eller inte.", Colors.blue_to_green, interval=0.025)
            time.sleep(.95)
            
            usr_answ13 = str(Write.Input("\nOm du vill ta chips skriv 'Y' eller 'N' om du inte vill. ", Colors.blue_to_green, interval=0.025))
            if usr_answ13.lower() == "y":
                wallet.make_payment(15)
                time.sleep(.95)
                Write.Print(f"\nDu tog en påse chips och har nu {wallet.balance}kr.", Colors.blue_to_green, interval=0.025)
                break

            if usr_answ13.lower() == "n":
                time.sleep(.95)
                Write.Print("Du valde att inte ta något och går vidare.", Colors.blue_to_green, interval=0.025)
                break

            else:
                Write.Print("Du har inte angett ett av valen.", Colors.blue_to_green, interval=0.025)

        if usr_answ11.lower() == "a":
            time.sleep(.95)
            Write.Print("\nDu gick till vänster och ser att det står en hylla med Monster", Colors.blue_to_green, interval=0.025)
            time.sleep(.95)
            Write.Print("\nDu går fram till hyllan och tänker för dig själv om du vill ha en energidryck eller inte.", Colors.blue_to_green, interval=0.025)
            time.sleep(.95)

            usr_answ10 = str(Write.Input("\nOm du vill ta drickan skriv 'Y' eller 'N' om du inte vill. ", Colors.blue_to_green, interval=0.025))
            if usr_answ10.lower() == "y":
                wallet.make_payment(20)
                time.sleep(.95)
                Write.Print(f"\nDu tog drickan och har nu {wallet.balance}kr.", Colors.blue_to_green, interval=0.025)
                break

            if usr_answ13.lower() == "n":
                time.sleep(.95)
                Write.Print("Du valde att inte ta något och går vidare.", Colors.blue_to_green, interval=0.025)
                break

            else:
                Write.Print("Du har inte angett ett av valen.", Colors.blue_to_green, interval=0.025)

        if usr_answ12.lower() == "d":
            time.sleep(.95)
            Write.Print("\nDu gick till vänster och ser att det står en hylla med Atherton eknötter", Colors.blue_to_green, interval=0.025)
            time.sleep(.95)
            Write.Print("\nDu går fram till hyllan och tänker för dig själv om du vill ha nötter eller inte.", Colors.blue_to_green, interval=0.025)
            time.sleep(.95)

            usr_answ13 = str(Write.Input("\nOm du vill ta nötter skriv 'Y' eller 'N' om du inte vill. ", Colors.blue_to_green, interval=0.025))
            if usr_answ13.lower() == "y":
                wallet.make_payment(15)
                time.sleep(.95)
                Write.Print(f"\nDu tog lite nötter och har nu {wallet.balance}kr.", Colors.blue_to_green, interval=0.025)
                break

            if usr_answ13.lower() == "n":
                time.sleep(.95)
                Write.Print("Du valde att inte ta något och går vidare.", Colors.blue_to_green, interval=0.025)
                break

            else:
                Write.Print("Du har inte angett ett av valen.", Colors.blue_to_green, interval=0.025)

    time.sleep(.95)    
    Write.Print("\nDu har nu betalat för allt och har gått ut ur butiken.", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)
    Write.Print("\nDu har glömt vilket håll du ska gå för att komma hem.", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)

    usr_answ17 = str(Write.Input("\nOm du vill gå fram skriv 'W', 'A' för vänster och 'D' för höger. ", Colors.blue_to_green, interval=0.025))
    while usr_answ17.lower() in ("w", "a", "d"):
            
            if usr_answ17.lower() == "w":
                time.sleep(.95)
                Write.Print("\nDu gick fram och ser en fontän, vill du testa din tur med fontänen?", Colors.blue_to_green, interval=0.025)
                time.sleep(.95)

                usr_answ18 = int(Write.Input("\nSkriv in '1' för att slänga in en tia och skriv '2' för att inte. ", Colors.blue_to_green, interval=0.025))
                if usr_answ18 == 1:
                    wallet.make_payment(10)
                    time.sleep(.95)
                    Write.Print("\nDu kastade in myntet och är inte säker på vad du ska önska dig.", Colors.blue_to_green, interval=0.025)
                    time.sleep(.5)
                    Write.Print("\nIfall du vill önska dig ett Fortnite giftcard skriv '1'", Colors.blue_to_green, interval=0.025) 
                    time.sleep(.3)
                    Write.Print("\nIfall du vill önska dig ett nytt pingisrack skriv '2'", Colors.blue_to_green, interval=0.025)
                    time.sleep(.3)
                    Write.Print("\nIfall du vill önskar dig ett Roblox giftcard skriv '3'", Colors.blue_to_green, interval=0.025)
                    time.sleep(.3)
                    usr_answ19 = int(Write.Input("\nOm det är något annat du skulle vilja ha skriv '4' ", Colors.blue_to_green, interval=0.025))

                    if usr_answ19 == 1:
                        time.sleep(.95)
                        Write.Print("\nDu önskade dig ett Fortnite gift card och ser att från himmlen ramlar det ner ett giftcard. \nDu plockar upp det och går vidare.", Colors.blue_to_green, interval=0.025)
                        break

                    elif usr_answ19 == 2:
                        time.sleep(.95)
                        Write.Print("\nDu önskade dig ett pingisrack och ser att från himmlen ramlar det ner ett rack. \nDu plockar upp det och går vidare.", Colors.blue_to_green, interval=0.025)
                        break

                    elif usr_answ19 == 3:
                        time.sleep(.95)
                        Write.Print("\nDu önskade dig ett Roblox giftcard och ser att från himmlen ramlar det ner ett giftcard. \nDu plockar upp det och går vidare.", Colors.blue_to_green, interval=0.025)
                        break

                    # Ditt egna val av gåva. Det kommer bli lite svårt med gramatiken ifall man önskar sig vissa saker men kan tyvärr inte göra så mycket åt det.
                    elif usr_answ19 == 4:
                        time.sleep(.95)
                        usr_gift = Write.Input("\nVad skulle du vilja önska dig? Skriv här -> ", Colors.blue_to_green, interval=0.025)
                        Write.Print(f"\nDu ser att från skyn faller det ner {usr_gift}.", Colors.blue_to_green, interval=0.025)
                        Write.Print(f"\nDu plockar din {usr_gift} och går vidare.", Colors.blue_to_green, interval=0.025)
                        break

                    else:
                        Write.Print("\nDu har inte angett ett av valen, vänligen försök igen.", Colors.blue_to_green, interval=0.025)

                if usr_answ18 == 2:
                    time.sleep(.95)
                    Write.Print("\nDu valde att inte slänga en slant in i fontänen och går vidare", Colors.blue_to_green, interval=0.025)
                    break

                else:
                    Write.Print("\nDu har inte angett ett av valen, vänligen försök igen.", Colors.blue_to_green, interval=0.025)

            elif usr_answ17.lower() == "a":
                time.sleep(.95)
                Write.Print("\nDu gick till vänter och du ser en clown.", Colors.blue_to_green, interval=0.025)
                time.sleep(.95)
                Write.Print("\nDu tänker för dig själv att han ser vänlig ut.", Colors.blue_to_green, interval=0.025)
                time.sleep(.95)
                usr_answ20 = str(Write.Input("\nVill du gå fram till honom? 'Y' För ja och 'N' för nej. ", Colors.blue_to_green, interval=0.025))

                if usr_answ20.lower() == "y":
                    time.sleep(.95)
                    Write.Print("\nDu går fram till honom och han säger.", Colors.blue_to_green, interval=0.025)
                    time.sleep(.4)
                    Write.Print("\n'Hejsan, vad är ditt namn då?'", Colors.purple, interval=0.025)
                    namn = Write.Input(" Ange ditt namn: ", Colors.blue_to_green, interval=0.025)
                    time.sleep(.95)
                    Write.Print(f"\n'Hej {namn}, mitt namn är clownen Bongo.'", Colors.purple, interval=0.025)
                    time.sleep(.95)
                    Write.Print("\n'Vad gör du ute så sent?'", Colors.purple, interval=0.025)
                    str(Write.Input(" Svara här -> ", Colors.blue_to_green, interval=0.025))
                    time.sleep(.95)
                    Write.Print("\n'Jaha, va kul.", Colors.purple_to_red, interval=0.025)
                    time.sleep(.8)
                    Write.Print(".", Colors.purple_to_red, interval=0.025)
                    time.sleep(.8)
                    Write.Print(".", Colors.purple_to_red, interval=0.025)
                    time.sleep(.8)
                    Write.Print("'", Colors.purple_to_red, interval=0.025)
                    time.sleep(.95)
                    Write.Print("\nDu börjar känna dig lite obekväm.", Colors.blue_to_green, interval=0.025)
                    usr_answ21 = str(Write.Input("\nVill du stanna eller gå iväg? 'G' för att gå iväg och 'S' för att stanna. ", Colors.blue_to_green, interval=0.025))

                    if usr_answ21.lower() == "g":
                        time.sleep(.95)
                        Write.Print("\nDu säger ", Colors.blue_to_green, interval=0.025)
                        Write.Print("'Okej, hejdå Bongo' ", Colors.purple, interval=0.025)
                        Write.Print("och går iväg", Colors.blue_to_green, interval=0.025)
                        time.sleep(.95)
                        Write.Print("\nDu kollar bakom dig och ser Bongo när han är arg.", Colors.blue_to_green, interval=0.025)
                        time.sleep(.95)
                        Write.Print("\nDu hör bakom dig ", Colors.blue_to_green, interval=0.025)
                        Write.Print("'Du borde springa'", Colors.red, interval=0.025)
                        playsound.playsound("clown.mp3")
                        time.sleep(.95)
                        Write.Print("\nDu gör som han säger och börjar springa.", Colors.blue_to_green, interval=0.025)
                        time.sleep(.5)
                        Write.Print("\nSlå en tärning för att se vilken hastighet du får. (2.5 - 15", Colors.blue_to_green, interval=0.025)
                        
                        usr_answ22 = Write.Input("Skriv in 'rulla' för att slå tärningarna: ", Colors.blue_to_green, interval=0.025)
                        if usr_answ22.lower() == "rulla":
                            # En del kod för att kasta en tärning som ger dig en hastighet och får du under 7.5 så hinner bongo ikapp dig.
                            dice_roll = random.randint(1,6)
                            speed = dice_roll*2.5
                            time.sleep(.95)
                            Write.Print(f"\nDu fick hastigheten {speed}.", Colors.blue_to_green, interval=0.025)
                            
                            if speed > 7.5:
                                time.sleep(.95)
                                Write.Print("\nDu sprang iväg och är nu utanför din dörr.", Colors.blue_to_green, interval=0.025)                            

                            elif speed < 7.5:
                                time.sleep(.95)
                                Write.Print("\nDu hann inte och bongo han ikapp dig.", Colors.blue_to_green, interval=0.025)
                                time.sleep(.95)
                                Write.Print("\nDu kan be för ditt liv om du vill.", Colors.blue_to_green, interval=0.025)
                                time.sleep(.5)
                                
                                usr_answ23 = Write.Input("Skriv in 'be' för att be för ditt liv: ", Colors.blue_to_green, interval=0.025)

                                if usr_answ23.lower() == "be":
                                    time.sleep(.95)
                                    Write.Print("\nDu bad för ditt liv och Bongo skonade dig denna gången.", Colors.blue_to_green, interval=0.025)
                                    time.sleep(.95)
                                    Write.Print("\nDu började gå samma håll och ser ditt hus och står nu utanför dörren.", Colors.blue_to_green, interval=0.025)

                                else:
                                    time.sleep(.95)
                                    Write.Print("\nDu bad inte för ditt liv och förlorade.", Colors.blue_to_green, interval=0.025)
                                    time.sleep(3)
                                    return "fail"

                        else:
                            Write.Print("\nOgiltligt svar.", Colors.blue_to_green, interval=0.025)

                    else:
                        Write.Print("\nOgiltligt svar.", Colors.blue_to_green, interval=0.025)

                if usr_answ20.lower() == "n":
                    Write.Print("\nDu gick vidare och ser ditt hus och står nu utanför dörren.", Colors.blue_to_green, interval=0.025)
                    break

                else:
                    Write.Print("\nOgiltligt svar.", Colors.blue_to_green, interval=0.025)

            elif usr_answ17.lower() == "d":
                    break    
                                
            else:
                Write.Print("\nDu har inte angett ett av valen, vänligen försök igen.", Colors.blue_to_green, interval=0.025)

    Write.Print("\nDu gick vidare och ser ditt hus och står nu utanför dörren.", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)
    Write.Print("\nDu går in och sätter dig vid datorn med dina godsaker och kopplar av.", Colors.blue_to_green, interval=0.025)
    time.sleep(.95)
    Write.Print("\nDu har överlevt natten.", Colors.blue_to_green, interval=0.025)

    Write.Print("\nTack till alla som hjälpt mig med detta.", Colors.blue_to_green, interval=0.025)

    return "pass"

if __name__ == '__main__':
    Snack()    