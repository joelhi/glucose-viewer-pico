from driver.display_driver import LCD_1inch8, colour
import math

def get_scaled_pixels(original_pixels, width: int, height: int, scale:int):
    scaled_width:int = width * scale
    scaled_height:int = height * scale
    scaled = [0] * (scaled_height * scaled_width)
    for idx, pixel in enumerate(original_pixels):
        if(pixel == 0):
            continue
        (i, j) = map_index_to_2d(idx, width, 1)
        scaled_pixels = get_scaled_indices(i, j, width, scale)
        for scaled_pixel in scaled_pixels:
            scaled[scaled_pixel] = pixel

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


def draw_circle(lcd : LCD_1inch8, x : float, y : float, r:float, c:int):
    lcd.hline(x-r,y,r*2,c)
    for i in range(1,r):
        a = int(math.sqrt(r*r-i*i))
        lcd.hline(x-a,y+i,a*2,c)
        lcd.hline(x-a,y-i,a*2,c)

def draw_ring(lcd : LCD_1inch8, x:float, y:float, r:float, c:int):
    lcd.pixel(x-r,y,c)
    lcd.pixel(x+r,y,c)
    lcd.pixel(x,y-r,c)
    lcd.pixel(x,y+r,c)
    for i in range(1,r):
        a = int(math.sqrt(r*r-i*i))
        lcd.pixel(x-a,y-i,c)
        lcd.pixel(x+a,y-i,c)
        lcd.pixel(x-a,y+i,c)
        lcd.pixel(x+a,y+i,c)
        lcd.pixel(x-i,y-a,c)
        lcd.pixel(x+i,y-a,c)
        lcd.pixel(x-i,y+a,c)
        lcd.pixel(x+i,y+a,c)

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
