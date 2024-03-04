import pygame

pygame.init()  # Дальше будет происходить разработка игры

# Задаем размер окна
screen = pygame.display.set_mode((600, 300))  # С помощью <flags=pygame.NOFRAME> можно скрыть верхние кнопки

pygame.display.set_caption('Rostya pygame!')  # Название для окна
icon = pygame.image.load('images/icon.png')  # Сохранить иконку
pygame.display.set_icon(icon)  # Указать иконку

square = pygame.Surface((50, 200))  # Поверхность
square.fill('Blue')  # Указать цвет заливки

myfont = pygame.font.Font('fonts/Micro_5/Micro5-Regular.ttf', 40)
text_surface = myfont.render('Rostya', True, 'Red')

player = pygame.image.load('images/icon.png')

running = True
while running:

    pygame.draw.circle(square, 'Red', (35, 185), 15)  # draw - нарисовать
    screen.blit(square, (20, 50))  # В кортеже передаются координаты(x, y)
    screen.blit(text_surface, (300, 100))
    screen.blit(player, (100, 50))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Для возможности закрыть игру
            # После отключения никакие дополнительные действия не должны выполняться
            running = False
            pygame.quit()
