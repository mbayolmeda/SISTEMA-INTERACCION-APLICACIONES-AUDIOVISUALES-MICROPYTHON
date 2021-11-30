from lib import wifiCfg
from m5stack import btnA, btnB, btnC, lcd
import time
import network
wlan_sta = network.WLAN(network.STA_IF)

def connect():
    lcd.clear()
    menu = True
    section = 0
    while (menu == True):
        if (btnA.wasPressed()):
            print('btnA')
            lcd.clear()
            section-=1
            if (section == -1):
                section = 2
        if (btnC.wasPressed()):
            print('btnC')
            lcd.clear()
            section+=1
            if (section == 3):
                section = 0
        if (section == 0):
            lcd.font(lcd.FONT_DejaVu24)
            lcd.print('Press btnB to:', lcd.CENTER, 80, lcd.GREENYELLOW)
            lcd.print("choose juan's network", lcd.CENTER, 120, lcd.GREENYELLOW)
            lcd.font(lcd.FONT_DejaVu18)
            lcd.print('Next',235, lcd.BOTTOM, lcd.GREENYELLOW)
            lcd.print('Prev',45, lcd.BOTTOM, lcd.GREENYELLOW)
        
        if (section == 1):
            lcd.font(lcd.FONT_DejaVu24)
            lcd.print('Press btnB to:', lcd.CENTER, 80, lcd.GREENYELLOW)
            lcd.print("choose home's network", lcd.CENTER, 120, lcd.GREENYELLOW)
            lcd.font(lcd.FONT_DejaVu18)
            lcd.print('Next',235, lcd.BOTTOM, lcd.GREENYELLOW)
            lcd.print('Prev',45, lcd.BOTTOM, lcd.GREENYELLOW)
        
        if (section == 2):
            lcd.font(lcd.FONT_DejaVu24)
            lcd.print('Press btnB to:', lcd.CENTER, 80, lcd.GREENYELLOW)
            lcd.print("choose phone's network", lcd.CENTER, 120, lcd.GREENYELLOW)
            lcd.font(lcd.FONT_DejaVu18)
            lcd.print('Next',235, lcd.BOTTOM, lcd.GREENYELLOW)
            lcd.print('Prev',45, lcd.BOTTOM, lcd.GREENYELLOW)
            
        if(btnB.wasPressed()):
            menu = False

    if(section == 0):
        ssid = 'ZAFIRO_TELECOM_UN9E_2.4Ghz'
        pswd = 'hzbcKaZK'
        
    elif(section == 1):
        ssid = 'vodafone4468'
        pswd = 'HTMJNMZHHTMMTK'
            
    elif(section == 2):
        ssid = 'OnePlus Nord 2'
        pswd = 'mariamola'
    wlan_sta.disconnect()    
    wifiCfg.doConnect(ssid, pswd, lcdShow=True)
    if(wifiCfg.isconnected()==False):
        lcd.print('wifi not connected, try again', lcd.CENTER,lcd.CENTER, lcd.RED)
    time.sleep_ms(1500)
    lcd.clear()
    return
