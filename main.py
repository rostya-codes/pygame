import pygame

pygame.init()  # Дальше будет происходить разработка игры

# Задаем размер окна
screen = pygame.display.set_mode((600, 300))  # С помощью <flags=pygame.NOFRAME> можно скрыть верхние кнопки

pygame.display.set_caption('Rostya pygame!')  # Название для окна
icon = pygame.image.load('images/icon.png')  # Сохранить иконку
pygame.display.set_icon(icon)  # Указать иконку

running = True
while running:

    #screen.fill((33, 26, 58))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Для возможности закрыть игру
            # После отключения никакие дополнительные действия не должны выполняться
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Проверка на нажатие клавишы
                screen.fill((33, 26, 100))  # Изменение цвета экрана при нажатии на клавишу
