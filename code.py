import board
import time
import neopixel
import random

pixel_pin=board.GP10
pixels = neopixel.NeoPixel(pixel_pin, 48, auto_write=False)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
DIM_RED = (20, 0, 0)
PINK = (255, 50, 50)
GREEN = (0, 40, 0)
BLUE = (0, 0, 40)
WHITE = (255, 255, 255)
DIM_WHITE = (100, 100, 100)
SOFT_WHITE = (255, 230, 150)

STAR_RED = (45, 0, 0)
STAR_GREEN = (4, 28, 4)
STAR_ORANGE = (22, 12, 2)
STAR_BLUE = (4, 9, 20)

CENTER = 7
INNER = [2, 5, 6, 10, 11]
MIDDLE = [1, 3, 8, 12, 14]
OUTER = [0, 4, 9, 13, 15]

# Test Pattern.
time.sleep(1)
pixels.fill(BLACK)
pixels.show()
time.sleep(1)

pixels.fill(STAR_RED)
pixels.show()
time.sleep(1)

pixels.fill(STAR_GREEN)
pixels.show()
time.sleep(1)

pixels.fill(STAR_BLUE)
pixels.show()
time.sleep(1)

pixels.fill(STAR_ORANGE)
pixels.show()
time.sleep(1)

def star_middle_out(queue_index, pixel_index):
    pixels[CENTER+pixel_index] = color_queue[queue_index+3]

    for each in INNER:
        pixels[each+pixel_index] = color_queue[queue_index+2]

    for each in MIDDLE:
        pixels[each+pixel_index] = color_queue[queue_index+1]
    
    for each in OUTER:
        pixels[each+pixel_index] = color_queue[queue_index+0]


def random_sparkle(pixel_index, pixel_count):
    pixels.fill(BLACK)
    pixels[random.randint(pixel_index, (pixel_index+pixel_count-1))] = DIM_WHITE
    pixels[random.randint(pixel_index, (pixel_index+pixel_count-1))] = DIM_WHITE
    pixels[random.randint(pixel_index, (pixel_index+pixel_count-1))] = DIM_WHITE
    pixels[random.randint(pixel_index, (pixel_index+pixel_count-1))] = DIM_WHITE
    pixels.show()
)

color_queue = [BLACK]
for each in range(0,11):
    color_queue.append(BLACK)
loop_iteration = 0
while (1):
    star_middle_out(4, 0)
    star_middle_out(2, 16)
    star_middle_out(0, 32)
    
    pixels.show()

    color_queue.pop(0)
    
    if (loop_iteration//4 == 0):
        next_color = STAR_RED
    elif (loop_iteration//4 == 1):
        next_color = STAR_BLUE
    elif (loop_iteration//4 == 2):
        next_color = STAR_GREEN
    elif (loop_iteration//4 == 3):
        next_color = STAR_ORANGE

    if (loop_iteration >= 15):
        loop_iteration = 0
    else:
        loop_iteration+=1

    color_queue.append(next_color)
    time.sleep(0.2)

