# Wed Lab2
from pygame.locals import *
import RPi.GPIO as GPIO
import pygame
import os
# Global Flag
CODERUN = True
# Environment Seting
os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1') #
os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
# Init Pygame
pygame.init()
pygame.mouse.set_visible(False)
size = (width, height) = (320, 240)
screen = pygame.display.set_mode(size)
WHITE = 255,255,255
BLACK = 0,0,0
screen.fill(BLACK)
button_font = pygame.font.Font(None, 50)
touch_info_font = pygame.font.Font(None, 30)
# GPIO Setting
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN,pull_up_down = GPIO.PUD_UP)
def GPIO17_callback(channel):
    global CODERUN
    print("Quit by Bail-out button!!!")
    CODERUN = False
GPIO.add_event_detect(17, GPIO.FALLING, callback=GPIO17_callback, bouncetime=300)

pressed_positions_list = []

def check_quit_button_press(position):
    x,y = position
    # Check if the position is in the button area
    if y < 230 and y > 170:
        if x < 280 and x > 200:
            global CODERUN
            print("Quit!!!")
            CODERUN = False

def refresh_touch_info(position):
    pressed_positions_list.append(position)
    x, y = position
    touch_position_info = "touch at " + str(x) + ", " + str(y)
    touch_info = touch_info_font.render(touch_position_info, True, WHITE)
    touch_info_rect = text_surface.get_rect(center=(150,100))
    screen.blit(touch_info, touch_rect)


if __name__ == "__main__":
    text_surface = button_font.render('Quit', True, WHITE)
    # Get Width and Height
    # print(text_surface.get_width())  # 63
    # print(text_surface.get_height()) # 38
    rect = text_surface.get_rect(center=(240, 200))

    screen.blit(text_surface, rect)
    touch_info = touch_info_font.render('Touch at', True, WHITE)
    touch_rect = text_surface.get_rect(center= (150, 100))
    screen.blit(touch_info, touch_rect)
    pygame.display.flip()
    pos_String = "No Touch"

    #while quit button not pressed
    while CODERUN:
        for event in pygame.event.get():
            if(event.type is MOUSEBUTTONDOWN):
                # touch_position = pygame.mouse.get_pos()
                # print(touch_position)
                pass
            #on mouse press
            elif(event.type is MOUSEBUTTONUP):
                touch_position = pygame.mouse.get_pos()
                print(touch_position)
                check_quit_button_press(touch_position)
                screen.fill(BLACK)
                refresh_touch_info(touch_position)
                screen.blit(text_surface, rect)
                pygame.display.flip()

