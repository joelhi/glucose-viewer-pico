from driver.display_driver import *
from driver.glycose_layout import draw_gradient, Colour

BACKGROUND_COLOUR : int = colour(50,70,50)

PADDING: int = 1

HEADER_HEIGHT: int = 20

FOOTER_HEIGHT: int = 20

"""Interface class to set up and automatically draw the glucose interface"""
class GlycoseDisplay:

    def __init__(self, lcd:LCD_1inch8) -> None:
        self.lcd = lcd


    def render(self):
        draw_gradient(
            self.lcd,
            Colour(50.0,200.0,20.0),
            Colour(50.0,30.0,50.0),
            Colour(-50.0,-150.0,-20.0))

        ## LOGIC HERE ##

        ## HEADER ##
        # self.lcd.fill_rect(
        #     PADDING, 
        #     PADDING, 
        #     self.lcd.width - 2*PADDING, 
        #     HEADER_HEIGHT, 
        #     self.lcd.WHITE)

        self.lcd.text(
            "Joel's glucose",
            5 + PADDING, 
            5 + PADDING, 
            self.lcd.BLACK)

        ## FOOTER ##
        # self.lcd.fill_rect(
        #     PADDING, 
        #     self.lcd.height-PADDING-FOOTER_HEIGHT, 
        #     self.lcd.width - 2*PADDING, 
        #     HEADER_HEIGHT, 
        #     self.lcd.WHITE)

        self.lcd.text(
            "Updated at 22:35",
            5 + PADDING, 
            self.lcd.height - (5 + PADDING + 8), 
            self.lcd.BLACK)

        ## BODY ##

        spacing = 5
        border = 10
        y_level = 32
        dot_size = 5
        large_height = 63
        large_width = 45
        small_height = 35
        small_width = 25
    
        self.lcd.rect(
            border,
            y_level,
            large_width,
            large_height,
            self.lcd.WHITE)
        
        self.lcd.rect(
            border + 1*(large_width + spacing),
            y_level,
            large_width,
            large_height,
            self.lcd.WHITE)
        
        self.lcd.fill_rect(
            border + 2*(large_width + spacing),
            y_level + large_height - dot_size, 
            dot_size, 
            dot_size,
            self.lcd.WHITE)
        
        self.lcd.rect(
            border + 2*(large_width + spacing) + spacing + dot_size,
            y_level + large_height - small_height,
            small_width,
            small_height,
            self.lcd.WHITE)


        self.lcd.show()