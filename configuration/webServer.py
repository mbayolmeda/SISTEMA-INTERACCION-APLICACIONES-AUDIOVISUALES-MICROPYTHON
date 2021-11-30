from m5stack import lcd
import socket
import time
import network
import gc
import json
import configuration.webPage as webPage

def serv():
    wlan_sta = network.WLAN(network.STA_IF)
    lcd.clear()

    if (not wlan_sta.isconnected()):
        lcd.print('Conectar a internet primero', lcd.CENTER,lcd.CENTER)
        time.sleep_ms(1000)
        lcd.clear()
        return
    #Socket pagina web
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
    
    lcd.print('Servidor web iniciado',lcd.CENTER,100)    
    ip = wlan_sta.ifconfig()[0]
    lcd.print('%s' % ip, lcd.CENTER, 130)
    
    flag = True
    while (flag == True):
        try:
            if gc.mem_free() < 102000:
                gc.collect()
            conn, addr = s.accept()
            conn.settimeout(3.0)
            lcd.clear()
            lcd.print('Received HTTP GET connection request from %s' % str(addr))
            print('Received HTTP GET connection request from %s' % str(addr))
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            lcd.print('GET Rquest Content = %s' % request)
            print('GET Rquest Content = %s' % request)
            
            alpha_index = request.find('?alpha') + 7
            dist_index = request.find('?dist') + 6
            endVar_index = request.find('?endVar')
            alpha = request[alpha_index:dist_index - 6]
            dist = request[dist_index:endVar_index]
            
            response = webPage.web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
            if((alpha_index != -1) and (dist_index != -1) and (endVar_index != -1)):
                flag = False
        except OSError as e:
            conn.close()
            print('Connection closed')

    s.close()
    var = {}
    var['alpha'] = alpha
    var['dist'] = dist
    var['addr'] = addr
    js_vars = json.dumps(var)
    file = open('files/vars.json', 'w')
    file.write(js_vars)
    file.close()
    lcd.clear()
    lcd.print('Servidor cerrado', lcd.CENTER, lcd.CENTER)
    time.sleep_ms(1500)
    lcd.clear()
    return
