import turtle
from turtle import Turtle, Screen
import random

# Initialize the turtle
def initialize_turtle():
    turtle.colormode(255)  # Set color mode to 255
    timmy = Turtle()  # Create a new turtle object
    timmy.pensize(5)  # Set the pen size
    timmy.speed(10)  # Set the drawing speed
    return timmy

# Generate a random color
def random_color():
    r = random.randint(0, 255)  # Generate random red value
    g = random.randint(0, 255)  # Generate random green value
    b = random.randint(0, 255)  # Generate random blue value
    random_color = (r, g, b)  # Create a tuple with the random values
    return random_color

# Draw lines with random colors and directions
def draw_lines(turtle, num_lines):
    for i in range(num_lines):
        turtle.color(random_color())  # Set a random color for the line
        turtle.forward(10)  # Move the turtle forward by 10 units
        # Randomly turn the turtle either right or left
        if random.choice([True, False]):
            turtle.right(90)
        else:
            turtle.left(90)

# Setup the screen to close on click
def setup_screen():
    screen = Screen()  # Create a screen object
    screen.exitonclick()  # Exit the screen on click

# Main function to initialize turtle, draw lines, and setup the screen
def main():
    num_sides = 10000  # Number of sides for the shape
    timmy = initialize_turtle()  # Initialize the turtle
    draw_lines(timmy, num_sides)  # Draw lines with the turtle
    setup_screen()  # Setup the screen

# Call the main function to run the program
main()
