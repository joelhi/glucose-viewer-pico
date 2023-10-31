import time
from driver.display_driver import LCD_1inch8, setup_lcd, colour
from graphics.number_font import draw_numbers, map_index_to_2d
from graphics.trend_arrows import draw_trend_arrow
from adapters.wifi_adapter import connect
from adapters.libreview_adapter import fetch_glucose_data

SCALE = 8

def connect_to_wifi(lcd : LCD_1inch8):
    lcd.fill(lcd.BLACK)
    lcd.text("connecting...", 5, 5, lcd.WHITE)
    lcd.show()
    connect()
    lcd.fill(colour(20,180,75))
    lcd.text("connected!", 5, 5, lcd.WHITE)
    lcd.show()
    time.sleep(1)

def render_glucose_value(value: float):
    integer = [" ", " "]
    string = str(value)
    split = string.split(".")
    for idx, letter in enumerate(reversed(split[0])):
        integer[len(integer)-1-int(idx)] = str(letter)
    draw_numbers(lcd, integer, SCALE, 15, 30)
    if(len(split)>1):
        decimal = split[1][0]
    else:
        decimal = 0
    draw_numbers(lcd, [".", decimal], int(SCALE/2), int(SCALE + 15 + 2 * 8 * 5), int(30 + (8*7/2)))

def colour_background(value :int):
    if(value==0):
        return(colour(150,10,25))
    elif(value==1):
        return(colour(20,175,100))
    elif(value==2):
        return(colour(180,140,40))
    elif(value==3):
        return(colour(200,100,20))
    else:
        return(colour(0,0,0))

lcd = setup_lcd()

connect_to_wifi(lcd)

while(True):
    glucose_info = fetch_glucose_data()
    lcd.fill(colour_background(glucose_info[3]))
    render_glucose_value(glucose_info[0])
    lcd.text("Updated: "+glucose_info[1].split(" ")[1], 5, 5, lcd.WHITE)
    draw_trend_arrow(lcd, 5, 95, 3, glucose_info[2])
    lcd.show()
    print(glucose_info)
    time.sleep(30)
