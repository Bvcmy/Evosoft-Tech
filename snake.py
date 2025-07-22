import turtle
import random
import time

delay = 0.1
score = 0 
highestscore = 0  # Corrected spelling from Heightestscore to highestscore
# snakebodies
bodies = []

# getting a screen canvas
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("white")
s.setup(width=600, height=600)

# create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("yellow")
head.fillcolor("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()  
food.speed(0)
food.shape("circle")
food.color("blue")
food.fillcolor("yellow")
food.penup()
food.goto(0, 200)

# score board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, 250)
sb.write(f"Score: {score}, Highest Score: {highestscore}")

# Movement functions
def moveup():
    if head.direction != "down":   
        head.direction = "up"       

def movedown():     
    if head.direction != "up":  
        head.direction = "down"     

def moveleft():
    if head.direction != "right":
        head.direction = "left" 

def moveright():
    if head.direction != "left":
        head.direction = "right"

def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Key Mapping
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")

# Main loop
while True:
 
    s.update() 
    
    # Check collision with border
    if head.xcor() > 540:
     head.setx(-540)  # Wrap around to the left side
    elif head.xcor() < -540:
     head.setx(540)   # Wrap around to the right side
    elif head.ycor() > 540:
     head.sety(-540)  # Wrap around to the bottom
    elif head.ycor() < -540:
     head.sety(540)   # Wrap around to the top

    # Check collision with food
    if head.distance(food) < 20:
        # Move the food to new random place
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the length of the snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)

        # Increase the score
        score += 10
        if score > highestscore:
            highestscore = score

        # Update the scoreboard
        sb.clear()
        sb.write(f"Score: {score}, Highest Score: {highestscore}")

    # Move the snake bodies
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for body in bodies:
                body.ht()
            bodies.clear()
            score = 0
            delay = 0.1
            sb.clear()
            sb.write(f"Score: {score}, Highest Score: {highestscore}")

    time.sleep(delay)

s.mainloop()
