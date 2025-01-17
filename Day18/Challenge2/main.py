import time
import turtle as t

tim = t.Turtle()


for _ in range(15):
    tim.forward(10)
    tim.penup()
    #time.sleep(0.2)  # עיכוב של 0.1 שניות
    tim.forward(10)
    tim.pendown()
    #time.sleep(0.2)  # עיכוב של 0.1 שניות

#t.done()