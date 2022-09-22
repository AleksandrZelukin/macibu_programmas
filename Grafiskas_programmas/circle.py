# Python program to demonstrate
# circle drawing


import turtle
	
# Initializing the turtle
t = turtle.Turtle()


r = 50
t.circle(r)

# Python program to demonstrate
# tangent circle drawing


import turtle
	
t = turtle.Turtle()

# radius for smallest circle
r = 10

# number of circles
n = 10

# loop for printing tangent circles
for i in range(1, n + 1, 1):
	t.circle(r * i)


# Python program to demonstrate
# spiral circle drawing


import turtle
	
t = turtle.Turtle()

# taking radius of initial radius
r = 10

# Loop for printing spiral circle
for i in range(100):
	t.circle(r + i, 45)



# Python program to demonstrate
# concentric circle drawing


import turtle
	
	
t = turtle.Turtle()

# radius of the circle
r = 10

# Loop for printing concentric circles
for i in range(50):
	t.circle(r * i)
	t.up()
	t.sety((r * i)*(-1))
	t.down()

