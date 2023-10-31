from driver.display_driver import LCD_1inch8, colour
from graphics.helper import get_scaled_indices, get_scaled_pixels, map_index_to_linear, map_index_to_2d

_WIDTH = 8
_HEIGHT = 8
_COLOUR = colour(255,255,255)

ARROW_BITMAPS = {
    "1" :  [0,0,0,1,1,0,0,0,
            0,0,0,1,1,0,0,0,
            0,0,0,1,1,0,0,0,
            1,0,0,1,1,0,0,1,
            1,1,0,1,1,0,1,1,
            0,1,1,1,1,1,1,0,
            0,0,1,1,1,1,0,0,
            0,0,0,1,1,0,0,0],

    "2" :  [0,1,0,0,0,0,0,0,
            1,1,1,0,0,0,0,0,
            0,1,1,1,0,0,1,1,
            0,0,1,1,1,0,1,1,
            0,0,0,1,1,1,1,1,
            0,0,0,0,1,1,1,1,
            0,0,1,1,1,1,1,1,
            0,0,1,1,1,1,1,1],

    "3" :  [0,0,0,1,1,0,0,0,
            0,0,0,0,1,1,0,0,
            0,0,0,0,0,1,1,0,
            1,1,1,1,1,1,1,1,
            1,1,1,1,1,1,1,1,
            0,0,0,0,0,1,1,0,
            0,0,0,0,1,1,0,0,
            0,0,0,1,1,0,0,0],

    "4" :  [0,0,1,1,1,1,1,1,
            0,0,1,1,1,1,1,1,
            0,0,0,0,1,1,1,1,
            0,0,0,1,1,1,1,1,
            0,0,1,1,1,0,1,1,
            0,1,1,1,0,0,1,1,
            1,1,1,0,0,0,0,0,
            1,1,0,0,0,0,0,0],

    "5" :  [0,0,0,1,1,0,0,0,
            0,0,1,1,1,1,0,0,
            0,1,1,1,1,1,1,0,
            1,1,0,1,1,0,1,1,
            1,0,0,1,1,0,0,1,
            0,0,0,1,1,0,0,0,
            0,0,0,1,1,0,0,0,
            0,0,0,1,1,0,0,0],
}

def draw_trend_arrow(lcd:LCD_1inch8, x:int, y:int, scale:int, key:int):
    scaled = get_scaled_pixels(ARROW_BITMAPS[str(key)], _WIDTH, _HEIGHT, scale)
    for i, val in enumerate(scaled):
        (j, i) = map_index_to_2d(i, _WIDTH, scale)
        if(val == 1):
            lcd.pixel(x + i, y + j, lcd.WHITE) 
