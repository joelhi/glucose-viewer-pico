from driver.display_driver import LCD_1inch8, colour

def get_scaled_pixels(original_pixels, width: int, height: int, scale: int):
    scaled_width = width * scale
    scaled_height = height * scale
    scaled = [0] * (scaled_height * scaled_width)
    
    for idx, pixel in enumerate(original_pixels):
        if pixel == 0:
            continue
        
        i, j = map_index_to_2d(idx, width, 1)
        scaled_indices = get_scaled_indices(i, j, width, scale)
        
        for scaled_idx in scaled_indices:
            scaled[scaled_idx] = pixel

    return scaled

def get_scaled_indices(i:int, j:int, width:int, scale:int):
    index=[]
    for map_i in range(i*scale, i*scale+scale):
        for map_j in range(j*scale, j*scale+scale):
            index.append(map_index_to_linear(map_i, map_j, width, scale))

    return index

def map_index_to_linear(i:int, j:int, width:int, scale:int)->int:
    return width * scale * i + j

def map_index_to_2d(i : int, width: int, scale : int)->(int, int):
    return (int(i / (width * scale)), i % (width * scale))

class Colour:
    def __init__(self, r:float, g:float, b:float) -> None:
        self.r = r
        self.b = b
        self.g = g
    
    def interpolate_linear(self, other_colour, parameter:float)->Colour:
        return Colour(
            self.r + parameter * (other_colour.r - self.r),
            self.g + parameter * (other_colour.g - self.g),
            self.b + parameter * (other_colour.b - self.b)
        )
    
    def __repr__(self) -> str:
        return str(self.r) + ", " + str(self.g) + ", " + str(self.b)

def draw_gradient(lcd : LCD_1inch8, base:Colour, x_delta:Colour, y_delta:Colour):
    for w in range(lcd.width):
        f_w = w/lcd.width
        for h in range(lcd.height):
            f_h = h/lcd.height
            lcd.pixel(
                w, 
                h, 
                colour(
                    int(base.r + f_w * x_delta.r + + f_h * y_delta.r),
                    int(base.g + f_w * x_delta.g + + f_h * y_delta.g),
                    int(base.b + f_w * x_delta.b + + f_h * y_delta.b)))
