# Litet quiz gjort av: Leo Tieu
# Lånad kod: https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class

import time
import os
import gc
import random

def quiz_game():
    class Question:
        def __init__(self, problem, difficulty, answer):
            self.problem = problem
            self.difficulty = difficulty
            self.answer = answer

    def class_to_list(questions):
        """Sorterar alla frågor i 3 listor. Enkel, medelsvår och svår."""
        list_of_all_questions = []
        list_of_easy_questions = []
        list_of_medium_questions = []
        list_of_hard_questions = []
        # https://stackoverflow.com/questions/328851/printing-all-instances-of-a-class
        for obj in gc.get_objects():
            if isinstance(obj, questions):
                list_of_all_questions.append(obj)
        for question in list_of_all_questions:
            if question.difficulty == "enkel":
                list_of_easy_questions.append(question)
            elif question.difficulty == "medelsvår":
                list_of_medium_questions.append(question)
            elif question.difficulty == "svår":
                list_of_hard_questions.append(question)
        return list_of_easy_questions, list_of_medium_questions, list_of_hard_questions


    # Enkla Frågor
    Question1 = Question("Räkna ut omkretsen på en kvadrat med sidlängden 3 cm.", "enkel", "12")
    Question2 = Question("Hur många cl är det i en normalstor coca-cola burk?", "enkel", "33")
    Question3 = Question("Det finns 5 äpplen på ett bord och du tar 2. Hur många har du?", "enkel", "2")
    Question4 = Question("Vad är det som går och går men aldrig kommer till dörren?", "enkel", "klockan")
    Question5 = Question("Vad heter grisen som är kompis med Nalle Puh?", "enkel", "nasse")
    Question6 = Question("Vad väger mest, fjädrar eller stenar?", "enkel", "stenar")
    Question7 = Question("Är Leo bäst i hela världen?", "enkel", "nej")

    # Medelsvåra frågor
    Question8 = Question("Skriv alfabetet", "medelsvår", "alfabetet")
    Question9 = Question("Hur många sekunder finns det i 1 timma?", "medelsvår", "3600")
    Question10 = Question("3, 5, 9, 17, x. Vad ska stå istället för x?", "medelsvår", "33")
    Question11 = Question("Hur många liter är det i 1 kubik decimeter?", "medelsvår", "1")
    Question12 = Question("Hur många sekunder är 3/4 av en minut?", "medelsvår", "1")
    Question13 = Question("Vad börjar på natten och slutar på dagen?", "medelsvår", "n")
    Question14 = Question("Vad är det som blir större och större ju mer man tar bort?", "medelsvår", "hålet")

    # Svåra frågor
    Question15 = Question("problem", "svår", "5")
    Question15.problem = '''
    En bok och penna kostar totalt 105kr
    Boken kostar 100 kr mer än pennan
    Vad kostar pennan?
    '''

    Question16 = Question("problem", "svår", "2")
    Question16.problem = '''
    Om du tävlar och går om personen som är på andra plats
    Vilken plats hamnar du på då?
    OBS! Svara endast med siffra
    '''

    Question17 = Question("problem", "svår", "kött")
    Question17.problem = '''
    En slaktare är 54 år gammal, 175 cm lång
    Vad väger han?
    '''
    # listor
    EasyQuestions, MediumQuestions, HardQuestions = class_to_list(Question)

    # Startskärm
    os.system('cls')
    cooldown = 1.5
    print("Innan du börjar, låt mig förklara lite regler för dig")
    time.sleep(cooldown)
    print("För att klara spelet så måste du svara på 6 frågor utan ett enda fel!")
    time.sleep(cooldown)
    print("Svara bara med ett ord, en siffra, en bokstav etc. Alltså inga enheter.")
    time.sleep(cooldown)
    print("Svarar du fel så måste du börja om :(")
    time.sleep(cooldown)
    print("Är du redo?")
    UserAnswer = input()
    if UserAnswer == "nej":
        print("Okej, jag bryr mig faktiskt inte så mycket. Du får köra ändå.")
        time.sleep(cooldown)
    os.system('cls')
    time.sleep(cooldown)


    def the_quiz(right_answers_needed, list_of_questions):
        """Ger ett "prov" till användaren. Använder 1 lista med quiz klassen."""
        random.shuffle(list_of_questions)
        right_answers = 0
        for n in range(right_answers_needed):
            os.system('cls')
            question = list_of_questions[n]
            print(f"Svårighetsgrad: {question.difficulty}")
            print("Kom ihåg att svara utan enhet! \n")
            time.sleep(0.5)
            print(f"Fråga nummer {right_answers + 1}")
            print(question.problem)
            user_answer = input(">")
            user_answer = user_answer.lower()
            if user_answer == question.answer:
                right_answers += 1
                print(f"Du har {right_answers_needed-right_answers} frågor kvar tills nästa nivå")
                time.sleep(1)
            else:
                os.system('cls')
                print(f"Du svarade fel, rätt svar var {question.answer}")
                while True:
                    user_answer = input("Börja om - 1 \nGe upp - 2")
                    if user_answer == "1":
                        return "start_over"
                    elif user_answer == "2":
                        return "give_up"
                    else:
                        print("skriv 1 eller 2")
        return "pass"

    UserResult = the_quiz(3, EasyQuestions)
    if UserResult != "pass":
        if UserResult == "start_over":
            return quiz_game()
        return UserResult
    UserResult = the_quiz(2, MediumQuestions)
    if UserResult != "pass":
        if UserResult == "start_over":
            return quiz_game()
        return UserResult
    UserResult = the_quiz(1, HardQuestions)
    if UserResult != "pass":
        if UserResult == "start_over":
            return quiz_game()
        return UserResult
    return UserResult


if __name__ == "__main__":
    quiz_game()
