#Alberto Alcaide-Morales
#March 4, 2023

#Problem 1:
print("\n\nProblem 1: ")
import math

def area_of_circle(r):

    area_of_circle = r * r * math.pi
    return area_of_circle

r = int(input("Enter number: "))
result = area_of_circle(r)
print ("The area of the circle is", result)

#Problem 2: 
print("\n\nProblem 2: ")

def t_range(n):
    if n in range(3,9):
        print( n, "is in the range")
    else :
        print("The number is outside the given range.")
t_range(float(input("Enter number: "))) 

#Problem 3:
print("\n\nPorblem 3: ")
def multiply(numbers):  
    total = 1
    for x in numbers:
        total = total * x
    return total  
print(multiply((5, 2, 7, -1)))

#Problem 4:
print("\n\nProblm 4: ")
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1, 3, 3, 3, 6, 2, 3, 5])) 

#Problem 5:
print("\n\nProblem 5: ")

import turtle
#function to draw squar with specified value

        
wn = turtle.Screen()

alex = turtle.Turtle()   
alex.color("blue")

def sqrfunc(size):
    for i in range(4):
        alex.forward(size)
        alex.left(90)
        
    alex.penup()
    alex.goto(1) 
    alex.pendown()




sqrfunc(25)
sqrfunc(50)
sqrfunc(75)
sqrfunc(100)
sqrfunc(125)
sqrfunc(150)
sqrfunc(175)

wn.exitonclick()

#Problem 6:
print("\n\nProblem 6: ")

import turtle
wn = turtle.Screen()

alex = turtle.Turtle()   
alex.color("magenta")

def penta():
    for i in range(10):
        for p in range(8):
            alex.right(45)
            alex.forward(100)
        alex.right(36)

penta()

wn.exitonclick()
   
