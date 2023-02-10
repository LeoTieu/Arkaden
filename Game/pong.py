import pygame
import sys


# variabler
WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 7

SCORE_FONT = pygame.font.SysFont("comicsans", 50)

score = 0


class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL



class Ball:
    MAX_VEL = 6
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel *= -1
        self.x_vel *= -1



def draw(win, paddles, ball, score):
    win.fill(BLACK)

    score_text = SCORE_FONT.render(f"{score}", 1, WHITE)
    win.blit(score_text, (WIDTH * (2/4) - score_text.get_width()//2, 20))

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue

    ball.draw(win)
    pygame.display.update()

# hanterar kollisionen på bollen och paddeln
def handle_collision(ball, paddle):

    # bollen studsar på väggar
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1
    elif ball.x - ball.radius >=700:
        ball.x_vel *= -1
        
    # bollen åker åt ett annat håll beroende på vart den landar på paddeln.
    if ball.x_vel < 0:
        if ball.y >= paddle.y and ball.y <= paddle.y + paddle.height:
            if ball.x - ball.radius <= paddle.x + paddle.width:
                ball.x_vel *= -1

                middle_y = paddle.y + paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = -1 * y_vel
                

# låter spelaren styra paddeln
def handle_paddle_movement(keys, paddle):
    if keys[pygame.K_w] and paddle.y - paddle.VEL >= 0:
        paddle.move(up=True)
    if keys[pygame.K_s] and paddle.y + paddle.VEL + paddle.height <= HEIGHT:
        paddle.move(up=False)


def win_menu(score):
    run = True
    score = 20
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return "passed"
                

        WIN.fill(BLACK)

        # skriver text
        win_font = pygame.font.SysFont("comicsans", 70)
        win_text = win_font.render("You Win!", 1, WHITE)
        WIN.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, 100))

        final_score_font = pygame.font.SysFont("comicsans", 40)
        final_score_text = final_score_font.render(f"Final Score: {score}", 1, WHITE)
        WIN.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, 200))

        button_font = pygame.font.SysFont("comicsans", 40)
        restart_button = button_font.render("Restart", 1, WHITE)
        WIN.blit(restart_button, (WIDTH // 2 - restart_button.get_width() // 2, 300))
        exit_button = button_font.render("Exit", 1, WHITE)
        WIN.blit(exit_button, (WIDTH // 2 - exit_button.get_width() // 2, 400))

        # gör musen användbar
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]

        # om musen trycker på restart börjar spelet om
        if 300 <= mouse_y <= 350:
            if WIDTH // 2 - restart_button.get_width() // 2 <= mouse_x <= WIDTH // 2 + restart_button.get_width() // 2:
                if pygame.mouse.get_pressed()[0]:
                    main()

        # om musen trycker på exit så returnas passed
        if 400 <= mouse_y <= 450:
            if WIDTH // 2 - exit_button.get_width() // 2 <= mouse_x <= WIDTH // 2 + exit_button.get_width() // 2:
                if pygame.mouse.get_pressed()[0]:
                    run = False
                    return "passed"

        pygame.display.update()

def game_over_menu(score):
    if score < 0:
        score = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return "not passed"

        WIN.fill(BLACK)

        # skriver text
        game_over_font = pygame.font.SysFont("comicsans", 70)
        game_over_text = game_over_font.render("Game Over", 1, WHITE)
        WIN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 100))

        final_score_font = pygame.font.SysFont("comicsans", 40)
        final_score_text = final_score_font.render(f"Final Score: {score}", 1, WHITE)
        WIN.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, 200))

        button_font = pygame.font.SysFont("comicsans", 40)
        restart_button = button_font.render("Restart", 1, WHITE)
        WIN.blit(restart_button, (WIDTH // 2 - restart_button.get_width() // 2, 300))
        exit_button = button_font.render("Exit", 1, WHITE)
        WIN.blit(exit_button, (WIDTH // 2 - exit_button.get_width() // 2, 400))

        # gör musen användbar
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]

        # om musen trycker på restart startas spelet om
        if 300 <= mouse_y <= 350:
            if WIDTH // 2 - restart_button.get_width() // 2 <= mouse_x <= WIDTH // 2 + restart_button.get_width() // 2:
                if pygame.mouse.get_pressed()[0]:
                    main()

        # om musen trycker på exit returnas not passed
        if 400 <= mouse_y <= 450:
            if WIDTH // 2 - exit_button.get_width() // 2 <= mouse_x <= WIDTH // 2 + exit_button.get_width() // 2:
                if pygame.mouse.get_pressed()[0]:
                    run = False
                    pygame.quit()
                    return "not passed"

        pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    score = 0

    # allting som får spelet att fungera
    while run:
        clock.tick(FPS)
        draw(WIN, [paddle], ball, score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return "not passed"

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, paddle)

        ball.move()
        handle_collision(ball, paddle)

        # om poängen går under 0 poäng så startas game over menyn
        if ball.x < 0:
            game_over_menu(score)
            run = False
            return "not passed"
            
        # varje gång bollen studsar på högra väggen får spelaren ett poäng och bollens hastighet ökar med 0.2
        elif ball.x > WIDTH:
            score += 1
            ball.x_vel += 0.2
            ball.x_vel = -ball.x_vel

        # om spelaren får 20 poäng eller över så startas vinst menyn.
        if score >= 20:
            win_menu(score)
            run = False
            return "passed"
            

    pygame.quit()
    
# start menyn
def main_menu():
    pygame.init()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return "not passed"

        WIN.fill(BLACK)
        
        # skriver instruktioner
        title_font = pygame.font.SysFont("comicsans", 70)
        title_text = title_font.render("Pong", 1, WHITE)
        WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 75))

        instructions_font = pygame.font.SysFont("comicsans", 30)
        instructions_text = instructions_font.render("Få 20 poäng för att vinna!", 1, WHITE)
        WIN.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, 175))

        instructions_text = instructions_font.render("Använd 'W' och 'S' för att styra paddeln", 1, WHITE)
        WIN.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, 230))

        instructions_text = instructions_font.render("Tryck på 'SPACE' för att starta", 1, WHITE)
        WIN.blit(instructions_text, (WIDTH // 2 - instructions_text.get_width() // 2, 350))

        # när spelaren trycker på mellanslag så startas main
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            main()
    
        pygame.display.update()


if __name__ == '__main__':
    main_menu()
