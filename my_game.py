from tkinter import *
import random

root = Tk()
root.title('Пинг-понг')
c1 = Canvas(root, width=800, heigh=400, cursor='pencil', bg='#D8BFD8')
c1.pack()

def keypress(event):
    if event.keycode == 37:
        c1.move(one, -20, 0)
        if c1.coords(one)[0] < 0:
            c1.move(one, -c1.coords(one)[0], 0)
    if event.keycode == 39:
        c1.move(one, 20, 0)
        if c1.coords(one)[2] > 800:
            c1.move(one, 800 - c1.coords(one)[2], 0)
    if event.keycode == 90:
        c1.move(two, -20, 0)
        if c1.coords(two)[0] < 0:
            c1.move(two, -c1.coords(two)[0], 0)
    if event.keycode == 67:
        c1.move(two, 20, 0)
        if c1.coords(two)[2] > 800:
            c1.move(two, 800 - c1.coords(two)[2], 0)


SPEED_X = 10
SPEED_Y = 5
TOP_DISTANCE = 10


# Возвращает мячик в центр
def new_ball():
    global SPEED_Y
    c1.coords(ball, 370, 180, 410, 220)
    SPEED_Y = - SPEED_Y


# Отскок мяча от ракеток
def bounce(act):
    global SPEED_X, SPEED_Y
    if act == 'strike':
        SPEED_X = random.randrange(-10, 10)
        SPEED_Y = -SPEED_Y
    else:
        SPEED_X = -SPEED_X


def tick():
    ball_left, ball_top, ball_right, ball_bottom = c1.coords(ball)
    ball_center = (ball_top + ball_bottom) / 2
    # Вертикальный отскок
    # Если далеко от горизонтальных границ
    if ball_top + SPEED_Y > TOP_DISTANCE and ball_bottom + SPEED_Y < 390:
        c1.move(ball, SPEED_X, SPEED_Y)
    elif ball_top == TOP_DISTANCE or ball_bottom == 390:
        # Проверяем, верха или низа касаемся
        if ball_top > 200:
            if c1.coords(one)[0] < ball_center < c1.coords(one)[2]:
                bounce('strike')
            else:
                new_ball()
        else:
            if c1.coords(two)[0] < ball_center < c1.coords(two)[2]:
                bounce('strike')
            else:
                new_ball()
    else:
        # Если выше
        if ball_bottom < line_divide:
            c1.move(ball, SPEED_X, 10 + ball_bottom)
        # Если ниже середины
        if ball_bottom > line_divide:
           c1.move(ball, SPEED_X,  390 - ball_bottom)
    # Горизонтальный отскок
    if ball_right + SPEED_X > 800 or ball_left + SPEED_X < 0:
        bounce('ricochet')


# две разделительные линии
line_top = c1.create_line(0, 10, 800, 10, fill='white')
line_bottom = c1.create_line(0, 390, 800, 390, fill='white')

# Создаем линию-разделитель поля
line_divide = c1.create_line(0, 200, 800, 200, fill='white')

# создаем мяч
ball = c1.create_oval(370, 180, 410, 220, fill='yellow')

# создаем платформы
one = c1.create_rectangle(300, 400, 470, 390, fill='#7B68EE', outline='#9932CC')
two = c1.create_rectangle(300, 0, 470, 10, fill='#FF6347', outline='#B22222')
root.bind('<Key>', keypress)





# Запуск мяча
def main():
    tick()
    root.after(30, main)


main()
root.mainloop()
