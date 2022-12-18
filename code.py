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


# Center Out
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

#while (1):
#    random_sparkle(0, 16)
#    time.sleep(0.05)

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

'''

pixels.fill(BLACK)
time.sleep(1)

while(1):
    pixels[CENTER] = (random.randint(0, 32), random.randint(0,32), random.randint(0,32))
    time.sleep(0.1)
    #pixels[CENTER] = BLACK

    rand_color = (random.randint(0, 32), random.randint(0,32), random.randint(0,32))
    for each in INNER:
        pixels[each] = rand_color
    time.sleep(0.1)
    #pixels.fill(BLACK)

    rand_color = (random.randint(0, 32), random.randint(0,32), random.randint(0,32))
    for each in MIDDLE:
        pixels[each] = rand_color
    time.sleep(0.1)
    #pixels.fill(BLACK)

    rand_color = (random.randint(0, 32), random.randint(0,32), random.randint(0,32))
    for each in OUTER:
        pixels[each]=rand_color
    time.sleep(0.1)
    #pixels.fill(BLACK)


for each in range(0, 16):
    pixels[each]=DIM_WHITE
    time.sleep(3)



while(1):
    for each in range(0, 16):
        pixel_color = ( random.randint(0, 64), random.randint(0, 64), random.randint(0,64) )
        pixels[each] = pixel_color
    time.sleep(1)


print("Set To GREEN")
pixels.fill(GREEN)
pixels.show()

time.sleep(2)
pixels.fill( (38, 8, 115) )


time.sleep(2)

print("Light Pixels")
pixels.fill(BLACK)
pixels[0]=RED
pixels[1]=GREEN
pixels[2]=BLUE
pixels[3]=WHITE
pixels[4]=DIM_WHITE


time.sleep(2)
pixels.fill(BLACK)
pixels[0]=RED
pixels[1]=DIM_RED
pixels[2]=PINK
pixels[3]=WHITE
pixels[4]=SOFT_WHITE

time.sleep(2)

pixels.fill(BLACK)
for value in range(0, 256):
    pixels.fill( (value, 0, value) )
    time.sleep(0.01)
for value in range(255, -1, -1):
    pixels.fill( (value, 0, value) )
    time.sleep(0.01)


time.sleep(2)
pixels.fill(GREEN)
for each in range(0, 30):
    for value in range(0, 5):
        pixels[value]=RED
        time.sleep(0.1)
        pixels[value]=GREEN


'''


