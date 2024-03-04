import pygame

clock = pygame.time.Clock()

pygame.init()  # Дальше будет происходить разработка игры

# Задаем размер окна
screen = pygame.display.set_mode((700, 400))  # С помощью <flags=pygame.NOFRAME> можно скрыть верхние кнопки

pygame.display.set_caption('Rostya pygame!')  # Название для окна
icon = pygame.image.load('images/icon.png')  # Сохранить иконку
pygame.display.set_icon(icon)  # Указать иконку

bg = pygame.image.load('images/bg.jpg')
walk_left = [  # To move to the left side of screen
    pygame.image.load('images/player_left/0.png'),
    pygame.image.load('images/player_left/1.png'),
    pygame.image.load('images/player_left/2.png'),
    pygame.image.load('images/player_left/3.png'),
]

walk_right = [  # To move to the right side of screen
    pygame.image.load('images/player_right/0.png'),
    pygame.image.load('images/player_right/1.png'),
    pygame.image.load('images/player_right/2.png'),
    pygame.image.load('images/player_right/3.png'),
]

player_anim_count = 0
bg_x = 0

bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
# Установка начальной громкости фоновой музыки
bg_sound.set_volume(0.4)  # Начальная громкость 40%
bg_sound.play()

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 700, 0))
    screen.blit(walk_right[player_anim_count], (300, 315))

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 5
    if bg_x == -700:
        bg_x = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Для возможности закрыть игру
            # После отключения никакие дополнительные действия не должны выполняться
            running = False
            pygame.quit()

    clock.tick(15)  # Указываем количество кадров в секунду
