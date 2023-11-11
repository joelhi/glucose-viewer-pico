from driver.display_driver import LCD_1inch8
from graphics.helper import get_scaled_pixels, map_index_to_2d, map_index_to_linear, get_scaled_indices

_HEIGHT:int = 7
_WIDTH:int = 5
_SPACING = 1

NUMBER_BITMAPS = {
        "0" : [0,1,1,1,0,
               1,0,0,0,1,
               1,0,0,1,1,
               1,0,1,0,1,
               1,1,0,0,1,
               1,0,0,0,1,
               0,1,1,1,0],
        "1" : [0,1,1,0,0,
               0,0,1,0,0,
               0,0,1,0,0,
               0,0,1,0,0,
               0,0,1,0,0,
               0,0,1,0,0,
               0,1,1,1,0],
        "2" : [0,1,1,1,0,
               1,0,0,0,1,
               0,0,0,0,1,
               0,0,1,1,0,
               0,1,0,0,0,
               1,0,0,0,0,
               1,1,1,1,1],
        "3" : [0,1,1,1,0,
               1,0,0,0,1,
               0,0,0,0,1,
               0,0,1,1,0,
               0,0,0,0,1,
               1,0,0,0,1,
               0,1,1,1,0],
        "4" : [0,0,0,1,1,
               0,0,1,0,1,
               0,1,0,0,1,
               1,0,0,0,1,
               1,1,1,1,1,
               0,0,0,0,1,
               0,0,0,0,1],
        "5" : [1,1,1,1,1,
               1,0,0,0,0,
               1,1,1,1,0,
               0,0,0,0,1,
               0,0,0,0,1,
               1,0,0,0,1,
               0,1,1,1,0],
        "6" : [0,0,1,1,0,
               0,1,0,0,0,
               1,0,0,0,0,
               1,1,1,1,0,
               1,0,0,0,1,
               1,0,0,0,1,
               0,1,1,1,0],
        "7" : [1,1,1,1,1,
               1,0,0,0,1,
               0,0,0,1,0,
               0,0,1,0,0,
               0,0,1,0,0,
               0,0,1,0,0,
               0,0,1,0,0],
        "8" : [0,1,1,1,0,
               1,0,0,0,1,
               1,0,0,0,1,
               0,1,1,1,0,
               1,0,0,0,1,
               1,0,0,0,1,
               0,1,1,1,0],
        "9" : [0,1,1,1,0,
               1,0,0,0,1,
               1,0,0,0,1,
               0,1,1,1,1,
               0,0,0,0,1,
               0,0,0,1,0,
               0,1,1,0,0],
        " " : [0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0],
        "." : [0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0,
               0,0,0,0,0,
               0,0,1,1,0,
               0,0,1,1,0],
        }
    
def draw_numbers(lcd:LCD_1inch8, numbers, scale:int, x:int, y:int):
    for index, number in enumerate(numbers):
        x_pos = x + index * scale * (_WIDTH + _SPACING)
        y_pos = y
        scaled = get_scaled_pixels(NUMBER_BITMAPS[str(number)], _WIDTH, _HEIGHT, scale)
        for i, val in enumerate(scaled):
            (j, i) = map_index_to_2d(i, _WIDTH, scale)
            if(val == 1):
                lcd.pixel(x_pos + i, y_pos + j, lcd.WHITE) 
        

