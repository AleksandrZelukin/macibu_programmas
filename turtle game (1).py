import turtle
import random

def PlayerOneWins():
    #turtle.ht()
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto (15, 0)
    turtle.color("blue")
    turtle.write("Player One Wins!", move=False, align="center", font=("Times New Roman", 40, "bold"))

def PlayerTwoWins():
    #turtle.ht()
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto (15, 0)
    turtle.color("red")
    turtle.write("Player One Wins!", move=False, align="center", font=("Times New Roman", 40, "bold"))
    
player_one = turtle.Turtle()
player_one.color("red")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)


player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

die = [1,2,3,4,5,6]

for i in range(20):
    if player_one.pos() >= (300,100):
            PlayerOneWins()
            print("Player One Wins!")
            break
    elif player_two.pos() >= (300,-100):
            PlayerTwoWins()
            print("Player Two Wins!")
            break
    else:
            player_one_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random.choice(die)
            
            player_one.fd(20*die_outcome)
            player_two_turn = input("Press 'Enter' to roll the die ")
            die_outcome = random.choice(die)

           
            player_two.fd(20*die_outcome)
