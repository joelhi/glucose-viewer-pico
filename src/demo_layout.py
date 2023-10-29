import time
from driver.display_driver import LCD_1inch8, setup_lcd, colour
from driver.graphic_utils import Colour, draw_gradient
from font.pixel_numbers import draw_numbers, map_index_to_2d
from web_adapter.wifi_connection import connect
from web_adapter.fetch_glucose import fetch_glucose

lcd = setup_lcd()

lcd.fill(lcd.BLACK)
lcd.text("connecting...", 5, 5, lcd.WHITE)
lcd.show()
connect()
lcd.fill(colour(20,180,75))
lcd.text("connected!", 5, 5, lcd.WHITE)
lcd.show()
time.sleep(1)

scale = 8
while(True):
    lcd.fill(colour(20,150,75))
    first = [" ", " "]
    resp = fetch_glucose()
    string = str(resp[0])
    split = string.split(".")
    for idx, letter in enumerate(reversed(split[0])):
        first[len(first)-1-int(idx)] = str(letter) # type: ignore
    draw_numbers(lcd, first, scale, 15, 30)
    if(len(split)>1):
        decimal = split[1][0]
    else:
        decimal = 0
    draw_numbers(lcd, [".", decimal], int(scale/2), int(scale + 15 + 2 * 8 * 5), int(30 + (8*7/2)))
    lcd.text(resp[1].split(" ")[1], 5, 5, lcd.WHITE)
    lcd.show()

    time.sleep(30)
