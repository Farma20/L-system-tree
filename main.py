import turtle
from random import randint

#прячем черепаху и процесс рисования
turtle.hideturtle()
turtle.tracer(0)
#поднимаем черепаху
turtle.penup()
#переносим черепаху
turtle.setposition(0, -300)
turtle.left(90)
#опускаем черепаху
turtle.pendown()
#толщина линии в пикселях
thick = 16
turtle.pensize(thick)
#цвет
turtle.pencolor('#000000')


Axiom = '0'
tempAx = ''
itr = 13
#Угол, длина сегмента и стек
angl = 16
dl = 10
stc = []

#словарь
translate = {'0': '1[-20]+20',
             '1': '21'}

for j in range(itr):
  for ch in Axiom:
    if ch in translate:
      tempAx += translate[ch]
    else:
      tempAx += ch

  Axiom = tempAx
  tempAx = ''
print(Axiom)

for ch in Axiom:
  #если сивол равен числу, то мы двиигаем черепаху вперед на dl
  if ch == '0':
    stc.append(turtle.pensize())
    turtle.pensize(4)

    r = randint(0, 10)

    if r < 3:
      turtle.pencolor('#009900')
    elif r > 6:
      turtle.pencolor('#667900')
    else:
      turtle.pencolor('#20BB00')

    turtle.forward(dl - 2)
    turtle.pensize(stc.pop())
    turtle.pencolor('#000000')


  if ch == '1':
    if randint(0, 10) > 4:
      turtle.forward(dl)


  if ch == '2':
    if randint(0, 10) > 4:
      turtle.forward(dl)

  if ch == '+':
    turtle.right(angl - randint(-13, 13))

  if ch == '-':
    turtle.left(angl - randint(-13, 13))

  #Если попалась открыв. скобка, то записываем в стек положение и угол попорота
  if ch == '[':
    thick *= 0.75
    turtle.pensize(thick)
    stc.append(thick)
    stc.append(turtle.xcor())
    stc.append(turtle.ycor())
    stc.append(turtle.heading())

  #Если встретилась закрю скобка, то мы перемещаем черепаху на записанные в стеке последнии данные и удаляем их
  if ch == ']':
    turtle.penup()
    turtle.setheading(stc.pop())
    turtle.sety(stc.pop())
    turtle.setx(stc.pop())
    thick = stc.pop()
    turtle.pensize(thick)
    turtle.pendown()

#обновление экрана
turtle.update()
turtle.done()