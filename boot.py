from m5stack import lcd, btnA, btnB, btnC
import socket
from time import ticks_ms, ticks_diff
import json
import gc
from sys import exit
import libraries.hcsr04 as hcsr04
import libraries.imu_utils as imu_utils
import libraries.osc as osc
import configuration.menuOptions as menuOptions

flag = True

lcd.clear()
lcd.font(lcd.FONT_Tooney)
lcd.print('Welcome', lcd.CENTER, 80, lcd.ORANGE)
lcd.font(lcd.FONT_DejaVu18)
lcd.print('Press any button', lcd.CENTER, 120, lcd.YELLOW)