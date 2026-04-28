import pygame  # Импорт библиотеки Pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пример окна Pygame")

# Основной цикл программы
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Закрытие окна
            running = False

    # Заливка фона белым цветом
    screen.fill((255, 255, 255))

    # Обновление экрана
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
