###
### Author: Kate Martin
### Course: CSc 110
### Description: This program is designed to display a nature scene
###              using graphics.  It utilizes if-statements, while loops,
###              indexing, the random module, parameters and arguments
###              within functions, and incorporates motion parallax on the
###              user's interface.
###

from graphics import graphics
import random

def main(gui):
    # Assign random colors to the mountains in three color strings
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_string_one = gui.get_color_string(red, green, blue)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_string_two = gui.get_color_string(red, green, blue)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_string_three = gui.get_color_string(red, green, blue)
    # Display the scene using a loop
    while True:
        gui.clear()
        sky(gui)
        mountain(gui, color_string_one)
        mountains(gui, color_string_two, color_string_three)
        foreground(gui)
        flowers(gui)
        birds(gui)
        gui.update_frame(30)

def flowers(gui):
    '''
    This function displays a flashing carnival of flowers using a while loop
    '''
    flowers = 0
    while flowers <= 15:
        flower_x = random.randint(0, 500)
        flower_y = random.randint((gui.mouse_y // 4) + 300, 500)
        gui.ellipse(flower_x, flower_y, 10, 10, 'hot pink')
        gui.ellipse(flower_x + 7, flower_y + 5, 10, 10, 'hot pink')
        gui.ellipse(flower_x + 14, flower_y , 10, 10, 'hot pink')
        gui.ellipse(flower_x + 7, flower_y - 5, 10, 10, 'hot pink')
        gui.ellipse(flower_x + 7, flower_y, 5, 5, 'yellow')
        flowers += 1

def sky(gui):
    '''
    This function displays the sky and a yellow sun with a black border
    The sun moves in respect to the mouse of the user.
    '''
    x = (gui.mouse_x // 30)
    y = (gui.mouse_y // 30)
    gui.rectangle(0, 0, 500, 500, 'light sky blue')
    gui.ellipse(x+365, y+65, 76, 76, 'black')
    gui.ellipse(x+365, y+65, 75, 75, 'yellow')

def foreground(gui):
    '''
    This function displays the foreground of the scene, including
    grass and a tree.  The tree uses a while loop to create a carnival
    of leaves of different colors.  The foreground moves in respect
    to the mouse of the user.
    '''
    x = (gui.mouse_x)
    y = (gui.mouse_y // 4)
    gui.rectangle(0, y + 300, 500, 400, 'spring green')
    x_grass = 0
    while x_grass <= 500:
        gui.line(x_grass, y + 300, x_grass, y + 280, 'spring green')
        x_grass += 5

    leaves = 0
    x = (gui.mouse_x // 10)
    while leaves <= 100:
        red = random.randint(0, 50)
        green = random.randint(30, 200)
        blue = random.randint(0, 50)
        color_string = gui.get_color_string(red, green, blue)
        x_leaves = random.randint(405, 480)
        y_leaves = random.randint(315, 380)
        gui.ellipse(x + x_leaves - 50, y + y_leaves - 75, 7, 4, color_string)
        leaves += 1
    gui.rectangle(x+385, y+300, 9, 62, 'brown')

def mountain(gui, color):
    '''
    This function displays the middle mountain in a random color.
    The mountain moves in respect to the mouse of the user.
    '''
    x = (gui.mouse_x // 18)
    y = (gui.mouse_y // 18)
    gui.triangle(x + 250, y + 130, x + 125, y + 400, x + 375, x + 400, color)

def mountains(gui, color_one, color_two):
    '''
    This function displays the middle mountains in random colors.
    The mountains move in respect to the mouse of the user, slightly more
    than the middle mountain does, in order to achieve motion parallax.
    '''
    x = (gui.mouse_x // 15)
    y = (gui.mouse_y // 15)
    gui.triangle(x+100, y+165, x-100, y+400, x+300, y+400, color_one)
    gui.triangle(x+400, y+165, x+200, y+400, x+600, y+400, color_two)

def birds(gui):
    '''
    This function displays 5 birds in the sky traveling downwards.
    Uses a while loop and lines to achieve this.
    '''
    bird = 0
    start_left_x = 30
    start_left_y = 50
    end_left_x = 50
    end_left_y = 60
    while bird < 5:
        gui.line(start_left_x, start_left_y, end_left_x, end_left_y, 'black')
        gui.line(end_left_x, end_left_y, start_left_x + 40, start_left_y, 'black')
        start_left_x += 60
        start_left_y += 15
        end_left_x = start_left_x + 20
        end_left_y = start_left_y + 10
        bird += 1
# call to main - argument passed in is the creation of the canvas for the program
main(gui=graphics(500, 500, 'motion parallax'))
