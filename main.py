import pygame as pg

# Ширина и высота экрана
width = 600 
height = 400

background_image = pg.transform.scale(pg.image.load("background.jpg"), [width, height]) # Фоновая картинка
screen = pg.display.set_mode((width, height))  # Главный экран игры

# Параметры красного шарика
fisrtBallRadius = 30   # Радиус
firstBallX = 50        # Позиция Х
firstBallY = 50        # Позиция У
firstBallSpeedX = 5    # Скорость по Х
firstBallSpeedY = 5    # Скорость по У
# Параметры зеленого шарики
greenBallRadius = 30
greenBallX = (width/2) - (fisrtBallRadius/2)
greenBallY = height -greenBallRadius
greenBallSpeedX = 5
greenBallSpeedY = 5

clock = pg.time.Clock()

while 1:
    for e in pg.event.get(): # Проверяем, решил ли пользователь выйти
        if e.type == pg.QUIT: exit()
        
    # Передвижение шаров
    firstBallX += firstBallSpeedX
    firstBallY += firstBallSpeedY

    greenBallY += greenBallSpeedY

    # Проверка касание стен, отскок
    if (firstBallX <= 0 + fisrtBallRadius) or (firstBallX > height - fisrtBallRadius):
        firstBallSpeedX = -firstBallSpeedX
    if (firstBallY <= 0 + fisrtBallRadius) or (firstBallY > width - fisrtBallRadius):
        firstBallSpeedY = -firstBallSpeedY

    if (greenBallY <= 0 + fisrtBallRadius) or (greenBallY > height - fisrtBallRadius):
        greenBallSpeedY = -greenBallSpeedY

    # Отображаем на экран фон
    screen.blit(background_image, (0, 0))
    # Отрисовка шаров
    pg.draw.circle(screen, 'red', (firstBallY, firstBallX), fisrtBallRadius)
    pg.draw.circle(screen, 'green', (greenBallX, greenBallY), fisrtBallRadius)

    pg.display.update() # Обновляем экран
    clock.tick(30) # Ждем следующего кадра

'''
Здания: 
1) Исправить ошибки в коде
2) Сменить скорость шариков
3) Изменить кол-во отображаемых кадров
4) Увлечить размер игрового поля (по своему желанию)
5) Добавить свой шарик (движение по своему усмотрению)
'''
