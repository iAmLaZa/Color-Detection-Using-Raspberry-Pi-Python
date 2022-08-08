import time
import Adafruit_TCS34725
import RPi.GPIO as GPIO
tcs = Adafruit_TCS34725.TCS34725()
tcs.set_interrupt(False)

GPIO.setmode(GPIO.BCM)
RED = 25
GREEN = 24
BLUE = 23

GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)

GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)

GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)



while True:
    try :
        r, g, b, c = tcs.get_raw_data()
        if((r > b) and (r >g)):
            if(b <5):
                #red
                #moteur.stop()
                time.sleep(5)
                #servo motor italien b degré t3 90 
                #moteur.start()
                
                
        elif((r < b) and (b >5)):
            #blue
            #moteur.stop()
            time.sleep(2)
            #moteur.start()
            
        elif((r < g) and (b <g) and (g>20)):
            if (b<10):
                #green 
                #moteur.stop()
                time.sleep(5)
                #moteur.start()
            
        GPIO.output(RED,r)
        GPIO.output(GREEN,g)
        GPIO.output(BLUE,b)
    except KeyboardInterrupt:
        GPIO.cleanup()


tcs.set_interrupt(True)
tcs.disable()