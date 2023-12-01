import turtle as trtl
import random as rand
import time as time





# -----setup-----
   # Store the file name of your shape


wn = trtl.Screen()
wn.setup(width=650, height=690)  # Make the screen aware of the new file
goodBanana = "BananaTurtle.gif"
badBanana = "RottenBananaTurtle.gif"
wn.bgpic("Backgrond.gif")


wn.addshape(goodBanana)
wn.addshape(badBanana)
wn.addshape("TurtleMonkey.gif")
wn.addshape("HollowedLog.gif")

scoreboard = trtl.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.shape("blank")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.setposition(-250,300)


startmessage = trtl.Turtle()
startmessage.speed(0)
startmessage.color("white")
startmessage.shape("blank")
startmessage.penup()
startmessage.setposition(0,75)
startmessage.pendown()
hardMode = 0
easyMode = 0 
question = str(input("Easy Mode or Hard Mode(E/H):\n")).upper()
if question == "H":
    hardMode = 1
    print("HARD MODE")
elif question == "E":
    easyMode = 1
    print("EASY MODE")
if hardMode == 1:
    wn.update()
    startmessage.write("HARD MODE", align = "center", font = ("Courier", 20, "bold"))
    time.sleep(1)
    startmessage.clear()
if easyMode == 1:
    wn.update()
    startmessage.write("EASY MODE", align = "center", font = ("Courier", 20, "bold"))
    time.sleep(1) 
    startmessage.clear()
startmessage.write("Press SPACE to start", align = "center", font = ("Courier", 20, "bold"))
wn.listen()


monkey = trtl.Turtle()
monkey.penup()
monkey.hideturtle()
monkey.setpos(0,-235)
monkey.shape("TurtleMonkey.gif")
monkey.dy = 1
monkey.dx = 0

Gravity = 1
jumping = False
jumpHeight = 20

log = trtl.Turtle()
log.penup()
log.hideturtle()    
log.setpos(monkey.xcor()-50,monkey.ycor()-165)
log.shape("HollowedLog.gif")

def initalizeScore():
    scoreboard.pendown()
    scoreboard.showturtle()
    scoreboard.write("Score:", align="center", font=("Courier", 20, "bold"))

def beginGame():
   startmessage.clear()
   start = True
   startmessage.write("We've started the game!", align="center", font=("Courier", 20, "bold"))
   time.sleep(1)
   startmessage.clear()
   while start == True:
      addModules()
      wn.onkeypress(moveRight,"Right")
      wn.onkeypress(moveLeft,"Left")
      wn.onkeypress(jump,"Up")
def addModules():
   monkey.showturtle()
   log.showturtle()
   initalizeScore()


def bananaFalling():
    banana = trtl.Turtle()
def moveRight():
    xPos = monkey.xcor()
    xPos = xPos + 15
    if xPos > 300:
        xPos = 300
    monkey.goto(xPos,-235)
def moveLeft():
    xPos = monkey.xcor()
    xPos = xPos - 15
    if xPos < - 300:
        xPos = -300
    monkey.goto(xPos,-235)
def jump():
    global jumping
    if not jumping:
        jumping = True
        initialY = monkey.ycor()

        for i in range(jumpHeight):
            monkey.sety(monkey.ycor() + 4)
            time.sleep(0.01)
            wn.update()

        if(monkey.xcor()<-180):
            monkey.sety(-200)  # Move monkey down to the log position
        else:
            monkey.sety(-210)

        for i in range(jumpHeight):
            monkey.sety(monkey.ycor() - Gravity)
            time.sleep(0.01)
            wn.update()

        jumping = False
        print(monkey.xcor())
wn.onkeypress(beginGame,"space")

trtl.done()