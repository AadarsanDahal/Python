import pygame
import time

# Initialize pygame
pygame.init()

# Set up the Xbox controller
pygame.joystick.init()
try:
    controller = pygame.joystick.Joystick(0)
    controller.init()
except pygame.error:
    print("No joystick found.")

def read_controller():
    pygame.event.pump()
    
    # Axis values for left joystick
    left_axis_x = controller.get_axis(0)
    left_axis_y = controller.get_axis(1)

    # Axis values for right joystick
    right_axis_x = controller.get_axis(3)
    right_axis_y = controller.get_axis(4)

    # Buttons
    a_button = controller.get_button(0)
    b_button = controller.get_button(1)
    x_button = controller.get_button(2)
    y_button = controller.get_button(3)

    # Map the axis values and button presses to commands
    if left_axis_y < -0.5:
        print("Forward")
    elif left_axis_y > 0.5:
        print("Backward")
    elif left_axis_x < -0.5:
        print("Left")
    elif left_axis_x > 0.5:
        print("Right")
    elif a_button:
        print("A Button Pressed")
    elif b_button:
        print("B Button Pressed")
    elif x_button:
        print("X Button Pressed")
    elif y_button:
        print("Y Button Pressed")
    else:
        print("Neutral")

try:
    while True:
        read_controller()
        time.sleep(0.1)
except KeyboardInterrupt:
    pygame.joystick.quit()
    pygame.quit()
    print("Controller reading stopped.")
