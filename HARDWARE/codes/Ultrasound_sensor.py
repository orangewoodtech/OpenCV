#import GPIO and time libraries
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#Set GPIOs
TRIG = 23
ECHO = 24

#Setup GPIOs
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
#Short delay
GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

while True:
 #Trigger pulse
 GPIO.output(TRIG, True)
 time.sleep(0.00001)
 GPIO.output(TRIG, False)

 #Wait for pulse to return
 while GPIO.input(ECHO)==0:
  pulse_start = time.time()
 while GPIO.input(ECHO)==1:
  pulse_end = time.time()

 #Calculating time
 pulse_time = pulse_end-pulse_start
 
 #Calculating distance approximating speed of sound to be 34300
 dist = 17150*pulse_time

 print ('Distance:',dist,' cm')
 time.sleep(1) 

GPIO.cleanup()
