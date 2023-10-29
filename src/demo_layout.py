import time
from driver.display_driver import LCD_1inch8, setup_lcd, colour
from driver.graphic_utils import Colour, draw_gradient
from font.pixel_numbers import draw_numbers, map_index_to_2d

lcd = setup_lcd()

scale = 8
count = 0
while(True):
    g = int(count*256/1000)
    lcd.fill(colour(50,g,750))
    string  = str(count)
    numbers = [" ", " ", " "]
    for idx, letter in enumerate(reversed(string)):
        numbers[len(numbers)-1-int(idx)] = str(letter) # type: ignore
    draw_numbers(lcd, numbers, scale, 15, 30)
    lcd.show()
    count+=1
    if count > 1000:
        count = 0

    time.sleep(1)
