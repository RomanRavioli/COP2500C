# Roman Manuel
# Problem 6 - Layout
# COP 2500C Section 5
# 10/16/2023

import turtle

def draw_trampoline(x, y, size):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.circle(size)

def draw_weight_machine(x, y, length, width):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(width)
  turtle.right(90)
  turtle.forward(length)
  turtle.right(90)
  turtle.forward(width)
  turtle.right(90)

def draw_pull_up_rack(x, y, length):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  for i in range(5):
    turtle.forward(length)
    turtle.right(72)

def main():
  draw_trampoline(-100, -100, 50)
  draw_weight_machine(-100, -100, 50, 50)
  draw_pull_up_rack(-100, -100, 50)

main()