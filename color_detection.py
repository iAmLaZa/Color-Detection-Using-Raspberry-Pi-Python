import time
import Adafruit_TCS34725
import RPi.GPIO as GPIO
tcs = Adafruit_TCS34725.TCS34725()
tcs.set_interrupt(False)

GPIO.setmode(GPIO.BOARD)
RED = 25
GREEN = 24
BLUE = 23
FR=50
SR=11

GPIO.setup(RED,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)

pr = GPIO.PWM(RED,FR)
pg = GPIO.PWM(GREEN,FR)
pb = GPIO.PWM(BLUE,FR)

pr.start(255)
pg.start(255)
pb.start(255)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(SR,GPIO.OUT)
servo = GPIO.PWM(SR,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo.start(0)


try:
    while True:
        r, g, b, c = tcs.get_raw_data()
        if((r > b) and (r >g)):
            if(b <5):
                #red
                #moteur.stop()
                pr.ChangeDutyCycle(80)
                pg.ChangeDutyCycle(1)
                pb.ChangeDutyCycle(1)
                #servo motor italien b degré t3 90 
                servo.ChangeDutyCycle(7)
                time.sleep(5)
                servo.ChangeDutyCycle(2)
                time.sleep(0.5)
                servo.ChangeDutyCycle(0)
                #moteur.start()
                
                
        elif((r < b) and (b >5)):
            #blue
            #moteur.stop()
            pr.ChangeDutyCycle(1)
            pg.ChangeDutyCycle(1)
            pb.ChangeDutyCycle(80)
            time.sleep(2)
            #moteur.start()
            
        elif((r < g) and (b <g) and (g>20)):
            if (b<10):
                #green 
                #moteur.stop()
                pr.ChangeDutyCycle(1)
                pg.ChangeDutyCycle(80)
                pb.ChangeDutyCycle(1)
                time.sleep(5)
                #moteur.start()
        else:
            #default color
            pr.ChangeDutyCycle(255)
            pg.ChangeDutyCycle(255)
            pb.ChangeDutyCycle(255)
except KeyboardInterrupt:
    pass


#Clean things up at the end
servo.stop()
tcs.set_interrupt(True)
tcs.disable()
pr.stop()
pg.stop()
pb.stop()
GPIO.cleanup()



#Clean things up at the end
servo.stop()
GPIO.cleanup()
print ("Goodbye")