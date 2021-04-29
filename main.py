import pygame 
import os 
import math

pygame.init()

# Display setup 
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('CSC 330 Extra Credit Lab')

# Image loader 
images = []
for i in range(7): 
    images.append(pygame.image.load('images/hangman' + str(i) + '.png'))

# Letter button
# (800 - (gap + r * 2)*13) /2
RADIUS = 20 
GAP = 15
letters = []
start_x = round(WIDTH - (RADIUS * 2 + GAP) * 13) / 2
start_y = 350 
A = 65 # ASCII

for i in range(26): 
    x = start_x + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = start_y + ((i // 13) * (GAP + RADIUS * 2))
    # True meaning still an option to be clicked
    letters.append([x,y, chr(A+i), True])

# Game vars
wrong_guesses = 0 
word = 'DEVELOPER'
guessed = []

# Styles 
WHITE = (255,255,255)
BLACK = (0,0,0)
FONT = pygame.font.SysFont('comicsans', 40)
FONT2 = pygame.font.SysFont('comicsans', 60)
# Game loop 
FPS = 60 
clock = pygame.time.Clock()
run = True 

def draw_buttons(): 
    window.fill(WHITE)
    # Word 
    display_word = ""
    for letter in word: 
        if letter in guessed: 
            display_word += letter + ' '
        else: 
            display_word += "_ "
    text = FONT2.render(display_word, 1, BLACK)
    window.blit(text, (400,200))


    # Buttons
    for letter in letters: 
        x, y, alph, available = letter
        if available: 
            pygame.draw.circle(window, BLACK, (x,y),RADIUS, 3 )
            text = FONT.render(alph, 1, BLACK)
            window.blit(text, (x - text.get_width()/2,y - text.get_height()/2))


    window.blit(images[wrong_guesses], (150,100))
    pygame.display.update()

while run: 
    clock.tick(FPS)

    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for letter in letters: 
                x,y, alph, available = letter 
                if available: 
                    distance = math.sqrt((x-mouse_x)**2 + (y - mouse_y)**2)
                    if distance < RADIUS: 
                        letter[3] = False
                        guessed.append(alph)                        

pygame.quit()
