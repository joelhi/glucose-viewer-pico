from driver.display_driver import LCD_1inch8, setup_lcd, colour
from font.pixel_numbers import draw_numbers, map_index_to_2d

lcd = setup_lcd()

scale = 8
draw_numbers(lcd, [1,2,3], scale, 5, 5)
draw_numbers(lcd, [9," ",5], scale, 5, 5 + scale*(7+1))

lcd.show()
