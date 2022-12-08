import pygame as pg
import pygame.display

x = 600
y = 400

background_image = pg.transform.scale(pg.image.load("64.jpg"), [x, y])
screen = pg.display.set_mode((x, y))

# Параметры красного шарика
ySpeedOneBalls = 10
xSpeedOneBalls = 10
radiusBall = 30
yOneBalls = 50
xOneBalls = 50
# Параметры зеленого шарики
ySpeedGreenBalls = 10
xSpeedGreenBalls = 10
radiusGreenBall = 30
xGreenBalls = (x/2) - (radiusBall/2)
yGreenBalls = y -radiusGreenBall

tick = pg.time.Clock()
running = True

while running:

    screen.blit(background_image, (0, 0))
    # Отрисовка шаров
    pg.draw.circle(screen, (255, 0, 0), (xOneBalls, yOneBalls), radiusBall)
    pg.draw.circle(screen, (0, 255, 0), (xGreenBalls, yGreenBalls), radiusBall)
    # Передвижение шаров
    xOneBalls += xSpeedOneBalls
    yOneBalls += ySpeedOneBalls

    yGreenBalls += ySpeedGreenBalls

    # Проверка касание стен, отскок
    if (xOneBalls <= 0 + radiusBall) or (xOneBalls > x - radiusBall):
        xSpeedOneBalls = -xSpeedOneBalls
    if (yOneBalls <= 0 + radiusBall) or (yOneBalls > y - radiusBall):
        ySpeedOneBalls = -ySpeedOneBalls

    if (yGreenBalls <= 0 + radiusBall) or (yGreenBalls > y - radiusBall):
        ySpeedGreenBalls = -ySpeedGreenBalls

    pg.display.update()
    tick.tick(15)

'''
Здания: 
1) Исправить ошибки в коде
2) Сменить скорость шариков
3) Изменить кол-во отображаемых кадров
4) Увлечить размер игрового поля (по своему желанию)
5) Добавить свой шарик (движение по своему усмотрению)
'''
