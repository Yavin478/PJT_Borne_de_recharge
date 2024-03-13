##############################################################################################
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                  Tag 166tt, Zt Rezal, KIN 215                              #
#                                                                                            #
#                                                                                            #
#                                                                                            #
#                                                                                            #
##############################################################################################

import lcddriver
from time import *

def initialize_lcd():
	lcd = lcddriver.lcd()
	clear_lcd(lcd)
	return lcd

def clear_lcd(lcd):
	lcd.lcd_clear()
	return True

def empty_line(lcd,line):
	lcd.lcd_display_string(" "*20,line)
	return True

def write_line(lcd,content,line):
	if 1 <= line and line <= 4:
		empty_line(lcd,line)
		if len(content) <= 20:
			lcd.lcd_display_string(content,line)
			return True
		else :
			lcd.lcd_display_string("Error: Line overflow",line)
			return False
	else:
		return False

def write_line_noref(lcd,content,line):
        if 1 <= line and line <= 4:
                if len(content) <= 20:
                        lcd.lcd_display_string(content,line)
                        return True
                else :
                        lcd.lcd_display_string("Error: Line overflow",line)
                        return False
        else:
                return False
