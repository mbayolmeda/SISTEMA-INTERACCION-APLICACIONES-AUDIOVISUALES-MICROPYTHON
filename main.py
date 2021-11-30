flag = True
while (flag==True):
    if (btnA.wasPressed() or btnB.wasPressed() or btnC.wasPressed()):
        menuOptions.rotation()
        flag = False

pMuestreo = 50 #en ms
t=ticks_ms()
ts=ticks_ms()
acc = [0,0,0]
tune_a = True
sc = False
sel_pr = False
p1 = False
p2 = False
still = True
front = False
back = False
left = False
right = False
vol = 0
port1 = 9000
port2 = 9001
s1=0.1
s2=0.1
s3=0.1
P_S1='/1/fader1'
P_S2='/1/fader2'
P_VOL3='/1/fader3'

file = open('files/offsets.json', 'r')
js_str = json.loads(file.read())
file.close()
acc_offsets = js_str['off_acc']
gyro_offsets = js_str['off_gyro']
pitch_offset = js_str['off_p']
roll_offset = js_str['off_r']

file2 = open('files/vars.json','r')
js_str2 = json.loads(file2.read())
file2.close()
alpha = float(js_str2['alpha'])
dist = int(js_str2['dist'])
srv_addr = js_str2['addr']
sensor = hcsr04.HCSR04(trigger_pin=26 , echo_pin=36, echo_timeout_us=30*2*50)

sc_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sign_gen =(srv_addr[0],9000)
mod = (srv_addr[0],9001)

lcd.clear()
lcd.print('Ajuste valor de alpha',lcd.CENTER, 60, lcd.ORANGE)
lcd.print('pulse btnB para continuar',lcd.CENTER, 80, lcd.ORANGE)
lcd.font(lcd.FONT_DejaVu24)
lcd.print('-', 60, lcd.BOTTOM, lcd.ORANGE)
lcd.print('+', 250, lcd.BOTTOM, lcd.ORANGE)
lcd.font(lcd.FONT_DejaVu18)
lcd.print('\rAlpha : %.2f' %alpha, lcd.CENTER, 150, lcd.ORANGE)
while True:
    gc.collect()
    #Conexion con servidor para mandar datos
    if tune_a:
        if btnA.wasPressed():
            alpha-=0.05
            lcd.print('\rAlpha : %.2f' %alpha, lcd.CENTER, 150, lcd.ORANGE)
        if btnC.wasPressed():
            alpha+=0.05
            lcd.print('\rAlpha : %.2f' %alpha, lcd.CENTER, 150, lcd.ORANGE)
        if btnB.wasPressed():
            tune_a = False
            sel_pr = True
            lcd.clear()
            lcd.print('Pulsa A para theremin',lcd.CENTER, 60, lcd.ORANGE)
            lcd.print('Pulse C para modulador',lcd.CENTER, 80, lcd.ORANGE)
            lcd.font(lcd.FONT_DejaVu24)
            lcd.print('A', 65, lcd.BOTTOM, lcd.ORANGE)
            lcd.print('C', 245, lcd.BOTTOM, lcd.ORANGE)
    gc.collect()        
    if (ticks_diff(ticks_ms(), t) >= pMuestreo):
        #Obtenemos el valor de HC-SR04
        distance = sensor.distance_cm()
                
        #Obtenemos los valores del acelerometro a partir de nuestra libreria imu_utils
        acc_n = imu_utils.accel(acc_offsets)
        acc = imu_utils.smooth(acc_n, acc, alpha)        
        gyro = imu_utils.gyro(gyro_offsets)
        
        #Guardamos los valores en formato json
        jo = {}
        jo['acc']=acc
        jo['gyro']=gyro
        str_jo = json.dumps(jo)
        msj = bytes(str_jo, 'utf-8')
        t=ticks_ms()
    if (ticks_diff(ticks_ms(), ts) >= 200):
        #Creamos el socket para establecer la comunicacion
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        saddr = socket.getaddrinfo(srv_addr[0],10001)[0][-1]
        s.connect(saddr)
        s.sendall(msj)
        s.close()
        ts=ticks_ms()
    gc.collect()
    if sel_pr:
        lcd.font(lcd.FONT_DejaVu18)
        if btnA.wasPressed():
            p1 = True
            sel_pr = False
            sc = True
            lcd.clear()
            lcd.print('Theremin', lcd.CENTER, 60, lcd.ORANGE)
            lcd.print('signal_generator port 9000', lcd.CENTER, 80, lcd.ORANGE)
        if btnC.wasPressed():
            p2 = True
            sel_pr = False
            sc = True
            lcd.clear()
            lcd.print('Modulador', lcd.CENTER, 60, lcd.ORANGE)
            lcd.print('signal_generator 1 port 9000', lcd.CENTER, 80, lcd.ORANGE)
            lcd.print('signal_generator 2 port 9001', lcd.CENTER, 100, lcd.ORANGE)
    gc.collect()
    if sc:
        lcd.font(lcd.FONT_DejaVu24)
        lcd.print('Exit', 135, lcd.BOTTOM, lcd.ORANGE)
        lcd.print('Back', 40, lcd.BOTTOM, lcd.ORANGE)
        if btnA.wasPressed():
            sc = False
            sel_pr = True
            lcd.clear()
            lcd.print('Pulsa A para theremin',lcd.CENTER, 60, lcd.ORANGE)
            lcd.print('Pulse C para modulador',lcd.CENTER, 80, lcd.ORANGE)
            lcd.font(lcd.FONT_DejaVu24)
            lcd.print('A', 65, lcd.BOTTOM, lcd.ORANGE)
            lcd.print('C', 245, lcd.BOTTOM, lcd.ORANGE)
        if btnB.wasPressed():
            lcd.clear()
            lcd.print('Aplicacion finalizada,', lcd.CENTER, 80, lcd.RED)
            lcd.print('reinicie o apague el', lcd.CENTER, 100, lcd.RED)
            lcd.print('dispositivo', lcd.CENTER, 120, lcd.RED)
            exit()
        us_dist = distance/dist
        
        if (gyro[0]<-20) and (acc[1]<-0.2):
            front = True
            back = False
            still = False
        if (gyro[0]>20) and ((-0.2<acc[1]) and (acc[1]<0.2)):
            front = False
            back = False
            still = True            
        if (gyro[0]<-20) and ((-0.2<acc[1]) and (acc[1]<0.2)):
            front = False
            back = False
            still = True
        if (gyro[0]>20) and (acc[1]>0.2):
            front = False
            back = True
            still = False
            
        if (gyro[1]<-20) and (acc[0]<-0.2):
            right = True
            left = False
            still = False
        if (gyro[1]>20) and ((-0.2<acc[0]) and (acc[0]<0.2)):
            right = False
            left = False
            still = True            
        if (gyro[1]<-20) and ((-0.2<acc[0]) and (acc[0]<0.2)):
            right = False
            left = False
            still = True
        if (gyro[1]>20) and (acc[0]>0.2):
            right = False
            left = True
            still = False
            
        if back:
            if acc[1]>0.1 and acc[1]<0.2:
                s2-=0.005
            if acc[1]>0.2 and acc[1]<0.4:
                s2-=0.01
            if acc[1]>0.4 and acc[1]<0.6:
                s2-=0.015
            if acc[1]>0.6 and acc[1]<0.8:
                s2-=0.02
        if front:
            if acc[1]<-0.1 and acc[1]>-0.2:
                s2+=0.005
            if acc[1]<-0.2 and acc[1]>-0.4:
                s2+=0.01
            if acc[1]<-0.4 and acc[1]>-0.6:
                s2+=0.015
            if acc[1]<-0.6 and acc[1]>-0.8:
                s2+=0.02
                
        if left:
            if acc[0]>0.1 and acc[0]<0.2:
                s1-=0.005
            if acc[0]>0.2 and acc[0]<0.4:
                s1-=0.01
            if acc[0]>0.4 and acc[0]<0.6:
                s1-=0.015
            if acc[0]>0.6 and acc[0]<0.8:
                s1-=0.02
        if right:
            if acc[0]<-0.1 and acc[0]>-0.2:
                s1+=0.005
            if acc[0]<-0.2 and acc[0]>-0.4:
                s1+=0.01
            if acc[0]<-0.4 and acc[0]>-0.6:
                s1+=0.015
            if acc[0]<-0.6 and acc[0]>-0.8:
                s1+=0.02
        if still:
            s1 = s1
            s2 = s2
        
        if p1:
            if us_dist>0:
                sc_socket.sendto(osc.message(P_S1, us_dist),sign_gen)
            sc_socket.sendto(osc.message(P_VOL3, s2),sign_gen)
        if p2:
            us_dist = us_dist*0.1
            sc_socket.sendto(osc.message(P_S1, s1),sign_gen)
            sc_socket.sendto(osc.message(P_S2, us_dist),mod)
            sc_socket.sendto(osc.message(P_S1, s2),mod)
            