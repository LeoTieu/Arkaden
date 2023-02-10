# För att kunna använda sig av pygame biblioteket
import pygame
import random
# För att kunna använda sig av pygame font biblioteket
import pygame.font
import time
import sys

# Initialisera pygame och skapa ett förnster
pygame.display.init()

pygame.font.init()

# Skärm inställningar
window_size = (600, 400)
window = pygame.display.set_mode(window_size)

# Namnet på spelet
pygame.display.set_caption('Snake - By Albin')

bg_color = (0, 0, 0)

font = pygame.font.Font(None, 24)

target_score = 100

game = False

class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body =[[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"

    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == "RIGHT":
            self.position[0] += 10
        elif self.direction == "LEFT":
            self.position[0] -= 10
        elif self.direction == "UP":
            self.position[1] -= 10
        elif self.direction == "DOWN":
            self.position[1] += 10

        self.body.insert(0, list(self.position))
        self.body.pop()

    def grow(self):
        # Lägg till ett block till ormens kropp
        last_block = self.body[-1]
        self.body.append([last_block[0], last_block[1]])

class Food:
    def __init__(self):
        # Genererar en random position för maten
        self.position = [random.randrange(1, (window_size[0]//10)) * 10, random.randrange(1, (window_size[1]//10)) * 10]

    def remove_food(self):
        # Genererar en ny random position för maten
        self.position = [random.randrange(1, (window_size[0]//10)) * 10, random.randrange(1, (window_size[1]//10)) * 10]

class Score:
    def __init__(self):
        self.score = 0

    def update_score(self, new_score):
        self.score = new_score

snake = Snake()

food = Food()

score = Score()

game = False

# Main menu loop
while game == False:
    # Målar upp meny fönstret
    window.fill(bg_color)

    # Rendera "Tryck på mellanslagstangenten" texten som en bild
    text_image = font.render("Tryck på mellanslagstangenten för att starta spelet", True, (255, 255, 255))

    # Får storleken på bilden
    text_rect = text_image.get_rect()

    text_rect.center = (window_size[0] // 2, window_size[1] // 2)

    # Målar upp text bilden på skärmen
    window.blit(text_image, text_rect)

    # Updaterar displayen
    pygame.display.update()

    # Checkar för användar input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Startar spelet
                game = True
                # Main game loop
                while game == True:
                    # Hanterar input och uppdaterar status
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RIGHT:
                                snake.change_direction("RIGHT")
                            elif event.key == pygame.K_LEFT:
                                snake.change_direction("LEFT")
                            elif event.key == pygame.K_UP:
                                snake.change_direction("UP")
                            elif event.key == pygame.K_DOWN:
                                snake.change_direction("DOWN")

                    # Rör ormen och kolla om den har ätit mat
                    snake.move()
                    if snake.position == food.position:
                        snake.grow()
                        food.remove_food()
                        score.update_score(score.score + 10)

                    # Måla upp ormen och maten på skärmen
                    window.fill(bg_color)
                    for pos in snake.body:
                        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(pos[0], pos[1], 10, 10))
        
                    pygame.draw.rect(window, (255, 0, 0), pygame.Rect(food.position[0], food.position[1], 10, 10))

                    score_image = font.render("Score: " + str(score.score), True, (255, 255, 255))

                    # Blit poängen till hörnet längst upp till vänster
                    window.blit(score_image, (0, 0))

                    # Kontrollera kollisioner
                    if snake.position[0] > window_size[0] or snake.position[0] < 0:
                        text_image = font.render("Game over! Poäng: " + str(score.score), True, (255, 255, 255))

                        text_rect = text_image.get_rect()

                        text_rect.center = (window_size[0] // 2, window_size[1] // 2)

                        window.blit(text_image, text_rect)

                        # Updatera displayen och avsluta spelet
                        pygame.display.update()
                        time.sleep(3)
                        score.score = 0
                        game = False

                    if snake.position[1] > window_size[1] or snake.position[1] < 0:

                        text_image = font.render("Game over! Poäng: " + str(score.score), True, (255, 255, 255))

                        text_rect = text_image.get_rect()

                        text_rect.center = (window_size[0] // 2, window_size[1] // 2)

                        window.blit(text_image, text_rect)

                        pygame.display.update()
                        time.sleep(3)
                        score.score = 0
                        game = False

                    for block in snake.body[1:]:
                        if snake.position == block:

                            text_image = font.render("Game over! Poäng: " + str(score.score), True, (255, 255, 255))

                            text_rect = text_image.get_rect()

                            text_rect.center = (window_size[0] // 2, window_size[1] // 2)

                            window.blit(text_image, text_rect)

                            pygame.display.update()
                            time.sleep(3)
                            score.score = 0
                            game = False

                    # Kontrollera om spelaren har nått målpoängen
                    if score.score >= target_score:

                        text_image = font.render("You win! Poäng: " + str(score.score), True, (255, 255, 255))

                        text_rect = text_image.get_rect()

                        text_rect.center = (window_size[0] // 2, window_size[1] // 2)

                        window.blit(text_image, text_rect)

                        pygame.display.update()
                        time.sleep(3)
                        score.score = 0
                        game = False

                    # Updatera displayen och sätt frameraten
                    pygame.display.update()
                    pygame.time.Clock().tick(10)
