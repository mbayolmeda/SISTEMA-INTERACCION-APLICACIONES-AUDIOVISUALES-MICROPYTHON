import struct
import lib.wifiCfg as wifiCfg
import time
import lib.mpu6050 as mpu6050
import machine

wifiCfg.doConnect('vodafone4468','HTMJNMZHHTMMTK',lcdShow=True)
imu = mpu6050.MPU6050()

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

try:
  import usocket as socket
except:
  import socket

tx_port = 11111

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
s.connect(('192.168.0.17', tx_port)) # para enviar a tx_port



valf = float_to_hex(0.5)
adc = machine.ADC(36)
adc.atten(3)
adc.width(3)

while True:
    acc = imu.acceleration
    print(acc)
    s.sendall(b'/xy1\00\00\00\00,ff\00' + struct.pack('>f',acc[0]) + struct.pack('>f',acc[1]))
    s.sendall(b'/radial2\00\00\00\00,f\00\00' + struct.pack('>f',acc[2]))
    V1 = adc.read()
    print(V1)
    s.sendall(b'/fader9\00,f\00\00' + struct.pack('>f',V1))
    time.sleep_ms(200)
    
    

