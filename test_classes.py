__author__ = 'Ian'

# import libraries
import webbrowser
import time
import os   # imports filesystem stuff
import turtle



def take_break(minutes, num_breaks):
    # seconds = int(minutes) * 60 # convert minutes to an integer
    break_counter = 0
    print("*************** Started ******************")
    print("******** " + time.ctime() + " ********")
    while break_counter < num_breaks:
        time.sleep(minutes*60) # configured to convert the number of minutes given into seconds
        print("testing!")
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=wm#inbox/14e38528a5dbdd12")
        break_counter += 1
    print("************** Finished **************")

def rename_files():
    # get file names from this folder
    # the r before the path means raw path
    file_list = os.listdir(r"C:\Users\ideans\Documents\Python_Playground\message_pics")
    print file_list
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\ideans\Documents\Python_Playground\message_pics")
    print(saved_path)
    print(os.getcwd())

    for file_name in file_list:
        # remove numbers, convert all letters to lower case and rename file
        os.rename(file_name, file_name.translate(None, "0123456789").lower())
    os.chdir(saved_path)
    print(file_list)

def draw_square(the_turtle):
    counter = 0
    while counter < 4:
        the_turtle.forward(100)
        the_turtle.right(90)
        counter += 1

def draw_triangle(the_turtle):
    the_turtle.forward(70)
    the_turtle.right(135)
    the_turtle.forward(100)
    the_turtle.right(135)
    the_turtle.forward(70)

def loop_triangle(the_turtle):
    for i in range(1, 37):
        draw_triangle(the_turtle)
        the_turtle.right(10)

def loop_square(the_turtle):
    # counter = 0
    for i in range(1, 73):
        the_turtle.right(5)
        draw_square(the_turtle)
        # counter += 1

def start_drawing():
    window = turtle.Screen()
    window.bgcolor("black")
    leo = turtle.Turtle()
    leo.color('blue')
    leo.speed(15)
    loop_triangle(leo)
    # loop_square(leo)
    # draw_circle(window)
    # draw_triangle(window)
    window.exitonclick()

start_drawing()