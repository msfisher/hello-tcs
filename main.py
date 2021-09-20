# simple python program to print hello
# this is used for Git / GitHub demonstration
import random

sayings = ["hola", "Bonjour", "Hello", "Zdravstvuyte", "Salve"]

def sayHello(name):
    index = random.randint(0,5)
    print(sayings[index] + " " + name)

firstName = input("Please enter your name: ")
sayHello(firstName)
print(" @ TCS")  # print to the screen

