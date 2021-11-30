from m5stack import btnA, btnB, btnC, lcd
import configuration.networkConnect as networkConnect
import configuration.calibration as calibration
import configuration.webServer as webServer
def rotation():
    lcd.clear()
    menu = True
    section = 0
    while (menu == True):
        if (btnA.wasPressed()):
            print('btnA')
            lcd.clear()
            section-=1
            if (section == -1):
                section = 3
        if (btnC.wasPressed()):
            print('btnC')
            lcd.clear()
            section+=1
            if (section == 4):
                section = 0
        if (section == 0):
            lcd.font(lcd.FONT_DejaVu24)
            lcd.print('Press btnB to:', lcd.CENTER, 80, lcd.GREENYELLOW)
            lcd.print('choose Wifi network', lcd.CENTER, 120, lcd.GREENYELLOW)
            lcd.font(lcd.FONT_DejaVu18)
            lcd.print('Next',235, lcd.BOTTOM, lcd.GREENYELLOW)
            lcd.print('Prev',45, lcd.BOTTOM, lcd.GREENYELLOW)
            
                       
        elif (section == 1):
            lcd.font(lcd.FONT_DejaVu24)
            lcd.print('Press btnB to:', lcd.CENTER, 80, lcd.GREENYELLOW)
            lcd.print('launch web server', lcd.CENTER, 120, lcd.GREENYELLOW)
            lcd.font(lcd.FONT_DejaVu18)
            lcd.print('Next',235, lcd.BOTTOM, lcd.GREENYELLOW)
            lcd.print('Prev',45, lcd.BOTTOM, lcd.GREENYELLOW)
            
            
        elif (section == 2):
            lcd.font(lcd.FONT_DejaVu24)
            lcd.print('Press btnB to:', lcd.CENTER, 80, lcd.GREENYELLOW)
            lcd.print('calibrate MPU6886', lcd.CENTER, 120, lcd.GREENYELLOW)
            lcd.font(lcd.FONT_DejaVu18)
            lcd.print('Next',235, lcd.BOTTOM, lcd.GREENYELLOW)
            lcd.print('Prev',45, lcd.BOTTOM, lcd.GREENYELLOW)
            
            
        elif (section == 3):
            lcd.font(lcd.FONT_DejaVu24)
            lcd.print('Press btnB to:', lcd.CENTER, 80, lcd.GREENYELLOW)
            lcd.print('iniciate proyect', lcd.CENTER, 120, lcd.GREENYELLOW)
            lcd.font(lcd.FONT_DejaVu18)
            lcd.print('Next',235, lcd.BOTTOM, lcd.GREENYELLOW)
            lcd.print('Prev',45, lcd.BOTTOM, lcd.GREENYELLOW)
            
        else:
            print('error')
            
        if(btnB.wasPressed()):
            print('btnB')
            print(section)
            if(section == 0):
                networkConnect.connect()
            elif(section == 1):
                webServer.serv()
            elif(section == 2):
                calibration.calibrate()
            elif(section == 3):
                menu = False

    return
