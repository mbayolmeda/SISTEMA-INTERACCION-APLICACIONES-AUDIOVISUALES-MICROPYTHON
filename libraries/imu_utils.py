import math
from lib import mpu6050

imu = mpu6050.MPU6050()
def accel_gyro_offsets(n):
    zero_off = [0.0,0.0,0.0]
    off_acc = [0.0,0.0,0.0]
    off_gyro = [0.0,0.0,0.0]
    for i in range(n):
        a_xyz = accel(zero_off)
        g_xyz = gyro(zero_off)
        for j in range(3):
            off_acc[j] += 1/n*a_xyz[j]
            off_gyro[j] += 1/n*g_xyz[j]
        off_acc[2] -=1.0 #Componente gravedad            
        return off_acc, off_gyro 
         
         
def accel(offset):
    acc = imu.acceleration
    a_xyz = [acc[0]-offset[0], acc[1]-offset[1], acc[2]-offset[2]]
    return a_xyz

def gyro(offset):
    gy = imu.gyro
    g_xyz = [gy[0]-offset[0], gy[1]-offset[1], gy[2]-offset[2]]
    return g_xyz

def smooth(new, prev, alpha):
    sm = [0.0]*len(new)
    for i in range(len(new)):
        sm[i] = new[i]*(1-alpha) + prev[i]*alpha
        prev[i] = sm[i]
    return sm

def ypr_offsets(n):
    zero_off = [0.0,0.0,0.0]
    off_ypr = [0.0,0.0]
    for i in range(n): # perform n readings to estabilice
        ypr = imu.ypr
        for j in range(2):
            off_ypr[j] += 1/n*ypr[j+1]
    off_p = off_ypr[0]
    off_r = off_ypr[1]
    print("Offsets pitch: ", off_p)
    print("Offsets roll: ", off_r)
    return off_p, off_r
    
def pitch_roll(a_xyz):
    #brute-force, mala resolución cuando z se acerca a 0
    tilt_x = math.atan(a_xyz[0]/a_xyz[2])*180/math.pi
    tilt_y = math.atan(a_xyz[1]/a_xyz[2])*180/math.pi
    tilt=[tilt_x,tilt_y]
    #resolución constante
    pitch = math.atan(a_xyz[0]/math.sqrt(a_xyz[1]**2+a_xyz[2]**2))*180/math.pi
    roll = math.atan(a_xyz[1]/math.sqrt(a_xyz[0]**2+a_xyz[2]**2))*180/math.pi
    pr=[pitch, roll]
    return tilt, pr        
        