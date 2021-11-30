from m5stack import lcd, btnA, btnB, btnC
import time
import json
from lib import mpu6050
import libraries.imu_utils as imu_utils

imu = mpu6050.MPU6050()
def calibrate():
    lcd.clear()
    lcd.font(lcd.FONT_DejaVu18)
    lcd.print('Deja el dispositivo quieto',lcd.CENTER, 80, lcd.ORANGE)
    lcd.print('para empezar la calibracion,',lcd.CENTER, 110, lcd.ORANGE)
    lcd.print('pulsa btnB cuando este listo',lcd.CENTER, 140, lcd.ORANGE)
    
    while (btnB.wasPressed()==False):
        pass

    lcd.clear()
    lcd.print('Pulsa los botones para', lcd.CENTER, 40, lcd.ORANGE)
    lcd.print('elegir un numero de rondas', lcd.CENTER, 70, lcd.ORANGE)
    lcd.print('para la calibracion', lcd.CENTER, 100, lcd.ORANGE)
    lcd.font(lcd.FONT_DejaVu24)
    lcd.print('-', 65, lcd.BOTTOM, lcd.ORANGE)
    lcd.print('+', 245, lcd.BOTTOM, lcd.ORANGE)
    lcd.print('ENTER', 120, lcd.BOTTOM, lcd.ORANGE)        
    enter = False
    count = 1
    lcd.print('\rRondas : %d' %count, lcd.CENTER, 150, lcd.ORANGE)
    while (enter == False):    
        if(btnA.wasPressed()):
            count = count - 1
            lcd.print('\rRondas : %d' %count, lcd.CENTER, 150, lcd.ORANGE)
            if (count<1):
                count = 1
        if(btnC.wasPressed()):
            count = count + 1
            lcd.print('\rRondas : %d' %count, lcd.CENTER, 150, lcd.ORANGE)
        if(btnB.wasPressed()):
            enter = True
    #Guardar valores de offset en json
    time.sleep_ms(500)
    off_acc, off_gyro = imu_utils.accel_gyro_offsets(count)
    off_p, off_r = imu_utils.ypr_offsets(count)
    off = {}
    off['off_acc'] = off_acc
    off['off_gyro'] = off_gyro
    off['off_p'] = off_p
    off['off_r'] = off_r
    js_off = json.dumps(off)
    file = open('offsets.json', 'w')
    file.write(js_off)
    file.close()
    lcd.clear()
    lcd.print('Offsets calculados',lcd.CENTER, 100, lcd.ORANGE) 
    time.sleep_ms(1500)
    lcd.clear()
    return