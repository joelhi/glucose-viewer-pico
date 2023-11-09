import time
from driver.display_driver import LCD_1inch8, setup_lcd, colour
from graphics.number_font import draw_numbers
from graphics.trend_arrows import draw_trend_arrow
from adapters.wifi_adapter import connect
from adapters.libreview_adapter import fetch_glucose_data

SCALE = 8

# Define color constants
COLOR_RED = colour(150, 10, 25)
COLOR_GREEN = colour(20, 150, 80)
COLOR_YELLOW = colour(180, 140, 40)
COLOR_ORANGE = colour(200, 100, 20)
COLOR_BLACK = colour(0, 0, 0)

COLOURS = {
        4: COLOR_RED,
        1: COLOR_GREEN,
        2: COLOR_YELLOW,
        3: COLOR_ORANGE,
    }

def connect_to_wifi(lcd : LCD_1inch8):
    lcd.fill(lcd.BLACK)
    lcd.text("connecting...", 5, 5, lcd.WHITE)
    lcd.show()
    connect()
    lcd.fill(colour(20,180,75))
    lcd.text("connected!", 5, 5, lcd.WHITE)
    lcd.show()
    time.sleep(1)

def render_glucose_value(lcd: LCD_1inch8, value: float):
    integer_part, decimal_part = divmod(value, 1)
    
    integer_digits = str(int(integer_part))
    decimal_digit = str(int(decimal_part * 10))
    
    integer = [integer_digits[0] if len(integer_digits) > 0 else " ",
               integer_digits[1] if len(integer_digits) > 1 else " "]
    
    draw_numbers(lcd, integer, SCALE, 15, 30)
    draw_numbers(lcd, [".", decimal_digit], int(SCALE / 2), int(SCALE + 15 + 2 * 8 * 5), int(30 + (8 * 7 / 2)))


def run_layout():
    lcd = setup_lcd()
    connect_to_wifi(lcd)

    while(True):
        glucose_info = fetch_glucose_data()
        lcd.fill(COLOURS.get(glucose_info[3], COLOR_BLACK))
        render_glucose_value(lcd, glucose_info[0])
        lcd.text("Updated: "+glucose_info[1].split(" ")[1], 5, 5, lcd.WHITE)
        draw_trend_arrow(lcd, 5, 95, 3, glucose_info[2])
        lcd.show()
        time.sleep(30)
