import turtle

depth = int(input("Введіть глибину рекурсії: "))

screen = turtle.Screen()
t = turtle.Turtle()

def koch_side(n):
    if n==0:
        t.forward(50)
    else:
        for angle in [60, -120, 60, 0]:
            koch_side(n-1)
            t.left(angle)

koch_side(depth)

for _ in range(3):
    t.forward(50)
    t.right(120)

screen.mainloop()
