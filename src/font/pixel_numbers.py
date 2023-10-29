from driver.display_driver import LCD_1inch8

_HEIGHT:int = 7
_WIDTH:int = 5
_SPACING = 1

PIXEL_MAP = {
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
        }
    
def draw_numbers(lcd:LCD_1inch8, numbers, scale:int, x:int, y:int):
    
    for index, number in enumerate(numbers):
        x_pos = x + index * scale * (_WIDTH + _SPACING)
        y_pos = y
        scaled = get_scaled_pixels(str(number), scale)
        for i, val in enumerate(scaled):
            (j, i) = map_index_to_2d(i, scale)
            if(val == 1):
                lcd.pixel(x_pos + i, y_pos + j, lcd.WHITE) 
        

def get_scaled_pixels(number:str, scale:int):
    if number not in PIXEL_MAP.keys():
        return PIXEL_MAP[" "]
    
    width:int = _WIDTH * scale
    height:int = _HEIGHT * scale

    original_pixels = PIXEL_MAP[number]

    scaled = [0] * (height * width) # type: ignore
    for idx, pixel in enumerate(original_pixels):
        if(pixel == 0):
            continue
        (i, j) = map_index_to_2d(idx, 1)
        scaled_pixels = get_scaled_indices(i, j, scale)
        for scaled_pixel in scaled_pixels:
            scaled[scaled_pixel] = pixel

    return scaled


def get_scaled_indices(i:int, j:int, scale:int):
    range_i = range(i*scale, i*scale+scale) # type: ignore
    range_j = range(j*scale, j*scale+scale) # type: ignore

    index=[]
    for map_i in range_i:
        for map_j in range_j:
            index.append(map_index_to_linear(map_i, map_j, scale))

    return index

def map_index_to_linear(i:int, j:int, scale:int)->int:
    return _WIDTH * scale * i + j

def map_index_to_2d(i : int, scale : int)->(int, int): # type: ignore
    return (int(i / (_WIDTH * scale)), i % (_WIDTH * scale))

