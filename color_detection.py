import time
import Adafruit_TCS34725
import RPi.GPIO as GPIO
import turtle 
tcs = Adafruit_TCS34725.TCS34725()
tcs.set_interrupt(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
pr = GPIO.PWM(32,50)
pg = GPIO.PWM(36,50)
pb = GPIO.PWM(38,50)
pr.start(20)
pg.start(20)
pb.start(20)
i =0
w=" "
while i <10:
    i =i+1
    r, g, b, c = tcs.get_raw_data()
    if((r > b) and (r >g)):
        if(b <5):
            #red
            pr.ChangeDutyCycle(80)
            pg.ChangeDutyCycle(1)
            pb.ChangeDutyCycle(1)
            time.sleep(5)
            
            
    elif((r < b) and (b >5)):
        #blue
        pr.ChangeDutyCycle(1)
        pg.ChangeDutyCycle(1)
        pb.ChangeDutyCycle(80)
        time.sleep(2)
        
        
    elif((r < g) and (b <g) and (g>20)):
        if (b<10):
            #green 
            pr.ChangeDutyCycle(1)
            pg.ChangeDutyCycle(80)
            pb.ChangeDutyCycle(1)
            time.sleep(5)
    else:
        pr.ChangeDutyCycle(20)
        pg.ChangeDutyCycle(20)
        pb.ChangeDutyCycle(20)


tcs.set_interrupt(True)
tcs.disable()
pr.stop()
pg.stop()
pb.stop()