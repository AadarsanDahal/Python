import pygame
import time

# Initialize pygame
pygame.init()

# Set up the Xbox controller
pygame.joystick.init()
try:
    controller = pygame.joystick.Joystick(0)
    controller.init()
    print(f"Controller initialized: {controller.get_name()}")
except pygame.error:
    print("No joystick found.")
    exit()

def read_controller():
    pygame.event.pump()
    
    # Axis values for left joystick
    left_axis_x = controller.get_axis(0)
    left_axis_y = controller.get_axis(1)

    # Axis values for right joystick
    right_axis_x = controller.get_axis(2)
    right_axis_y = controller.get_axis(3)

    # Print the axis values for debugging
    #print(f"Right Axis X: {right_axis_x}, Right Axis Y: {right_axis_y}")
    
    # Buttons
    a_button = controller.get_button(0)
    b_button = controller.get_button(1)
    x_button = controller.get_button(2)
    y_button = controller.get_button(3)

    # Map the axis values and button presses to commands
    if right_axis_y < -0.5:
        print("Right Forward")
    elif right_axis_y > 0.5:
        print("Right Backward")
    elif right_axis_x < -0.5:
        print("Rjoy Left")
    elif right_axis_x > 0.5:
        print("Rjoy Right")

    if left_axis_y < -0.5:
        print("Ljoy Forward")
    elif left_axis_y > 0.5:
        print("Ljoy  Backward")
    elif left_axis_x < -0.5:
        print("Ljoy Left")
    elif left_axis_x > 0.5:
        print("Ljoy Right")
#now button pressed code 
    if a_button:
        print("A Button Pressed")
    elif b_button:
        print("B Button Pressed")
    elif x_button:
        print("X Button Pressed")
    elif y_button:
        print("Y Button Pressed")
    #else:
        #print("Neutral")

try:
    while True:
        read_controller()
        time.sleep(0.1)
except KeyboardInterrupt:
    pygame.joystick.quit()
    pygame.quit()
    print("Controller reading stopped.")
