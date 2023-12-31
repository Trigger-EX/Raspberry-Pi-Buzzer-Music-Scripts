# Original script is credited to Github user "AnonymousAlly"
# https:#github.com/AnonymousAlly/Arduino-Music-Codes/tree/master

import time
import RPi.GPIO as GPIO

#vars
spkrOne=17
spkrTwo=25

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(spkrOne,GPIO.OUT)
GPIO.setup(spkrTwo,GPIO.OUT)

#funcs
def delay(seconds):
    time.sleep(seconds/1750)

def tone(r,hertz,duration):
    pwm = GPIO.PWM(spkrOne,hertz)
    pwm.start(50)
    pwm.ChangeFrequency(hertz)
    delay(duration)
    pwm.stop

#intro
tone(3,196,71) #G3 
delay(71)  
tone(3,220,71) #A3 
delay(71)  
tone(3,261,71) #C4(middle)      
delay(71)  
tone(3,330,71) #E4 
delay(71)  
tone(3,523,572) #C5 
delay(572)  
tone(3,196,40) #G3 
delay(40)   
tone(3,196,246) #G3 
delay(246)  
tone(3,220,286) #A3 
delay(286)  
tone(3,261,572) #C4(middle)      
delay(572)  
tone(3,196,286) #G3 
delay(286)  
tone(3,220,286) #A3 
delay(286)  
tone(3,349,828) #F4 
delay(828)  
tone(3,392,828) #G4 
delay(828)  
tone(3,196,143) #G3 
delay(143)  
tone(3,220,143) #A3 
delay(143)  
tone(3,196,286) #G3 
delay(286) 
tone(3,392,572) #G4 
delay(572)  
tone(3,196,286) #G3 
delay(286) 
tone(3,330,828) #E4 
delay(828)  
tone(3,196,286) #G3 
delay(286)  
tone(3,220,286) #A3 
delay(286)  
tone(3,349,828) #F4 
delay(828)  
tone(3,294,1430) #D4 
delay(1430)  

#First Verse

tone(3,261,572) #C4(middle)      
delay(572)  
tone(3,392,286) #G4 
delay(286)  
tone(3,392,286) #G4 
delay(286)  
tone(3,392,828) #G4 
delay(828)  
tone(3,392,143) #G4 
delay(143)  
tone(3,349,143) #F4 
delay(143) 
tone(3,330,286) #E4 
delay(286)  
tone(3,330,143) #E4 
delay(143)  
tone(3,349,143) #F4 
delay(143) 
tone(3,392,286) #G4 
delay(286)    
tone(3,330,286) #E4 
delay(286)  
tone(3,294,572) #D4 
delay(572)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,294,286) #D4 
delay(286)  
tone(3,330,286) #E4 
delay(286)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,196,286) #G3 
delay(286)  
tone(3,1568,143) #G6 
delay(143) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,1568,143) #G6 
delay(143) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,2093,828) #C7
delay(828) 
tone(3,2093,286) #C7
delay(286) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1975,286) #B6
delay(286) 
tone(3,1568,143) #G6 
delay(143) 
tone(3,1760,286) #A6
delay(286) 
tone(3,1975,286) #B6
delay(286) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,261,572) #C4(middle)      
delay(572)  
tone(3,392,286) #G4 
delay(286)  
tone(3,440,286) #A4 
delay(286)  
tone(3,392,828) #G4 
delay(828)  
tone(3,330,143) #E4 
delay(143)  
tone(3,349,143) #F4 
delay(143)  
tone(3,392,286) #G4 
delay(286)  
tone(3,349,143) #F4 
delay(143)  
tone(3,330,143) #E4 
delay(143) 
tone(3,294,286) #D4 
delay(286)  
tone(3,220,286) #A3 
delay(286)  
tone(3,196,286) #G3 
delay(286)  
tone(3,175,572) #F3 
delay(572)  
tone(3,220,286) #A3 
delay(286)  
tone(3,196,286) #G3 
delay(286)  
tone(3,330,286) #E4 
delay(286)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,1568,143) #G6 
delay(143) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,1568,143) #G6 
delay(143) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,2093,828) #C7
delay(828) 
tone(3,2093,286) #C7
delay(286) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1975,286) #B6
delay(286) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1975,286) #B6
delay(286) 
tone(3,2093,286) #C7
delay(286) 
tone(3,196,71) #G3 
delay(71)  
tone(3,220,71) #A3 
delay(71)  
tone(3,261,71) #C4(middle)      
delay(71)  
tone(3,330,71) #E4 
delay(71)  
tone(3,523,286) #C5 
delay(286)  
tone(3,392,143) #G4 
delay(143) 
tone(3,392,429) #G4 
delay(429) 
tone(3,392,572) #G4 
delay(572) 
tone(3,349,572) #F4 
delay(572)  
tone(3,330,286) #E4 
delay(286)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,277,143) #Db/C#4 
delay(143)  
tone(3,294,429) #D4 
delay(429) 
tone(3,330,572) #E4 
delay(572)  
tone(3,392,828) #G4 
delay(1144)  
tone(3,440,286) #A4 
delay(286)  
tone(3,392,143) #G4 
delay(143)  
tone(3,330,286) #E4 
delay(286)  
tone(3,294,429) #D4 
delay(572)  
tone(3,196,286) #G3 
delay(286)  
tone(3,220,143) #A3 
delay(143) 
tone(3,261,429) #C4(middle)      
delay(429) 
tone(3,220,286) #A3 
delay(286) 
tone(3,261,143) #C4(middle)      
delay(143)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,572) #C4(middle)      
delay(1716)  
tone(3,392,143) #G4 
delay(143) 
tone(3,392,429) #G4 
delay(429) 
tone(3,392,572) #G4 
delay(572) 
tone(3,349,572) #F4 
delay(572)  
tone(3,330,286) #E4 
delay(286)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,277,143) #Db/C#4 
delay(143)  
tone(3,294,429) #D4 
delay(429) 
tone(3,330,572) #E4 
delay(572)  
tone(3,392,828) #G4 
delay(1144)  
tone(3,440,286) #A4 
delay(286)  
tone(3,392,143) #G4 
delay(143)  
tone(3,330,286) #E4 
delay(286)  
tone(3,294,429) #D4 
delay(572)  
tone(3,196,286) #G3 
delay(286)  
tone(3,220,143) #A3 
delay(143) 
tone(3,261,429) #C4(middle)      
delay(429) 
tone(3,220,286) #A3 
delay(286) 
tone(3,261,143) #C4(middle)      
delay(143)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,572) #C4(middle)      
delay(1716)   
tone(3,440,286) #A4 
delay(286)  
tone(3,392,143) #G4 
delay(143)  
tone(3,330,286) #E4 
delay(286)  
tone(3,294,429) #D4 
delay(572)  
tone(3,196,286) #G3 
delay(286)  
tone(3,220,143) #A3 
delay(143) 
tone(3,261,1287) #C4(middle)      
delay(1573) 
tone(3,220,286) #A3 
delay(286) 
tone(3,261,143) #C4(middle)      
delay(143)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,286) #C4(middle)      
delay(286)  

#Interlude One

tone(3,130,286) #C3 
delay(286)  
tone(3,196,143) #G3 
delay(143)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,286) #C4(middle)      
delay(286) 
tone(3,110,286) #A2
delay(286)  
tone(3,220,143) #A3 
delay(143) 
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,286) #C4(middle)      
delay(286) 
tone(3,87,286) #F2
delay(286) 
tone(3,196,143) #G3 
delay(143)  
tone(3,220,286) #A3 
delay(286)  
tone(3,261,143) #C4(middle)      
delay(143) 
tone(3,220,286) #A3 
delay(286)  
tone(3,247,286) #B3 
delay(286)  
tone(3,196,143) #G3 
delay(143)  
tone(3,220,286) #A3 
delay(286) 
tone(3,247,143) #B3 
delay(143)  
tone(3,196,286) #G3 
delay(286)  
tone(3,130,286) #C3 
delay(286)  
tone(3,196,143) #G3 
delay(143)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,286) #C4(middle)      
delay(286) 
tone(3,110,286) #A2
delay(286)  
tone(3,220,143) #A3 
delay(143) 
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,286) #C4(middle)      
delay(286) 
tone(3,87,286) #F2
delay(286) 
tone(3,196,143) #G3 
delay(143)  
tone(3,220,286) #A3 
delay(286)  
tone(3,261,143) #C4(middle)      
delay(143) 
tone(3,220,286) #A3 
delay(286)  
tone(3,247,286) #B3 
delay(286)  
tone(3,196,143) #G3 
delay(143)  
tone(3,220,286) #A3 
delay(286) 
tone(3,247,143) #B3 
delay(143)  
tone(3,196,286) #G3 
delay(286)  

#Second Verse

tone(3,261,572) #C4(middle)      
delay(572)  
tone(3,392,286) #G4 
delay(286)  
tone(3,392,286) #G4 
delay(286)  
tone(3,392,828) #G4 
delay(828)  
tone(3,392,143) #G4 
delay(143)  
tone(3,349,143) #F4 
delay(143) 
tone(3,330,286) #E4 
delay(286)  
tone(3,330,143) #E4 
delay(143)  
tone(3,349,143) #F4 
delay(143) 
tone(3,392,286) #G4 
delay(286)    
tone(3,330,286) #E4 
delay(286)  
tone(3,294,572) #D4 
delay(572)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,294,286) #D4 
delay(286)  
tone(3,330,286) #E4 
delay(286)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,196,286) #G3 
delay(286)  
tone(3,1568,143) #G6 
delay(143) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,1568,143) #G6 
delay(143) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,2093,828) #C7
delay(828) 
tone(3,2093,286) #C7
delay(286) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1975,286) #B6
delay(286) 
tone(3,1568,143) #G6 
delay(143) 
tone(3,1760,286) #A6
delay(286) 
tone(3,1975,286) #B6
delay(286) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,261,572) #C4(middle)      
delay(572)  
tone(3,392,286) #G4 
delay(286)  
tone(3,440,286) #A4 
delay(286)  
tone(3,392,828) #G4 
delay(828)  
tone(3,330,143) #E4 
delay(143)  
tone(3,349,143) #F4 
delay(143)  
tone(3,392,286) #G4 
delay(286)  
tone(3,349,143) #F4 
delay(143)  
tone(3,330,143) #E4 
delay(143) 
tone(3,294,286) #D4 
delay(286)  
tone(3,220,286) #A3 
delay(286)  
tone(3,196,286) #G3 
delay(286)  
tone(3,175,572) #F3 
delay(572)  
tone(3,220,286) #A3 
delay(286)  
tone(3,196,286) #G3 
delay(286)  
tone(3,330,286) #E4 
delay(286)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,1568,143) #G6 
delay(143) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,1568,143) #G6 
delay(143) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,2093,828) #C7
delay(828) 
tone(3,2093,286) #C7
delay(286) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1975,286) #B6
delay(286) 
tone(3,1760,143) #A6
delay(143) 
tone(3,1975,286) #B6
delay(286) 
tone(3,2093,286) #C7
delay(286) 
tone(3,196,71) #G3 
delay(71)  
tone(3,220,71) #A3 
delay(71)  
tone(3,261,71) #C4(middle)      
delay(71)  
tone(3,330,71) #E4 
delay(71)  
tone(3,523,286) #C5 
delay(286)  
tone(3,392,143) #G4 
delay(143) 
tone(3,392,429) #G4 
delay(429) 
tone(3,392,572) #G4 
delay(572) 
tone(3,349,572) #F4 
delay(572)  
tone(3,330,286) #E4 
delay(286)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,277,143) #Db/C#4 
delay(143)  
tone(3,294,429) #D4 
delay(429) 
tone(3,330,572) #E4 
delay(572)  
tone(3,392,828) #G4 
delay(1144)  
tone(3,440,286) #A4 
delay(286)  
tone(3,392,143) #G4 
delay(143)  
tone(3,330,286) #E4 
delay(286)  
tone(3,294,429) #D4 
delay(572)  
tone(3,196,286) #G3 
delay(286)  
tone(3,220,143) #A3 
delay(143) 
tone(3,261,429) #C4(middle)      
delay(429) 
tone(3,220,286) #A3 
delay(286) 
tone(3,261,143) #C4(middle)      
delay(143)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,572) #C4(middle)      
delay(1716)  
tone(3,392,143) #G4 
delay(143) 
tone(3,392,429) #G4 
delay(429) 
tone(3,392,572) #G4 
delay(572) 
tone(3,349,572) #F4 
delay(572)  
tone(3,330,286) #E4 
delay(286)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,277,143) #Db/C#4 
delay(143)  
tone(3,294,429) #D4 
delay(429) 
tone(3,330,572) #E4 
delay(572)  
tone(3,392,828) #G4 
delay(1144)  
tone(3,440,286) #A4 
delay(286)  
tone(3,392,143) #G4 
delay(143)  
tone(3,330,286) #E4 
delay(286)  
tone(3,294,429) #D4 
delay(572)  
tone(3,196,286) #G3 
delay(286)  
tone(3,220,143) #A3 
delay(143) 
tone(3,261,429) #C4(middle)      
delay(429) 
tone(3,220,286) #A3 
delay(286) 
tone(3,261,143) #C4(middle)      
delay(143)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,572) #C4(middle)      
delay(2002)   

#Interlude Two

tone(3,1568,286) #G6 
delay(286) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,110,286) #A2
delay(286)  
tone(3,220,143) #A3 
delay(143) 
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,286) #C4(middle)      
delay(286) 
tone(3,1175,572) #D6 
delay(572) 
tone(3,1318,286) #E6
delay(286) 
tone(3,1397,572) #F6
delay(572) 
tone(3,1568,572) #G6 
delay(572) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,784,286) #G5 
delay(286)  
tone(3,523,286) #C5 
delay(286) 
tone(3,587,286) #D5 
delay(286) 
tone(3,392,143) #G4 
delay(143) 
tone(3,523,286) #C5 
delay(286) 
tone(3,784,286) #G5 
delay(286)  
tone(3,523,143) #C5 
delay(143) 
tone(3,587,572) #D5 
delay(572) 
tone(3,1046,572) #C6 
delay(572)  
tone(3,1175,286) #D6 
delay(286) 
tone(3,1318,572) #E6
delay(572) 
tone(3,1046,572) #C6 
delay(572)  
tone(3,784,286) #G5 
delay(286)  
tone(3,784,286) #G5 
delay(286)  
tone(3,523,286) #C5 
delay(286) 
tone(3,587,286) #D5 
delay(286) 
tone(3,392,143) #G4 
delay(143) 
tone(3,523,286) #C5 
delay(286) 
tone(3,784,286) #G5 
delay(286)  
tone(3,523,143) #C5 
delay(143) 
tone(3,587,572) #D5 
delay(858) 
tone(3,784,143) #G5 
delay(143)  
tone(3,880,143) #A5 
delay(143) 
tone(3,784,143) #G5 
delay(143) 
tone(3,659,286) #E5 
delay(286)  
tone(3,587,286) #D5 
delay(286)  
tone(3,494,143) #B4 
delay(143) 
tone(3,440,143) #A4 
delay(143)  
tone(3,392,286) #G4 
delay(286)  
tone(3,523,143) #C5 
delay(143) 
tone(3,659,286) #E5 
delay(286)  
tone(3,698,429) #F5 
delay(429)  
tone(3,659,429) #E5 
delay(429) 
tone(3,523,429) #C5 
delay(429)   
tone(3,392,429) #G4 
delay(429)  
tone(3,392,143) #G4 
delay(143)  
tone(3,494,143) #B4 
delay(143) 
tone(3,659,286) #E5 
delay(286)  
tone(3,587,286) #D5 
delay(286)  
tone(3,110,143) #A2
delay(143) 
tone(3,147,286) #D3 
delay(286)  
tone(3,175,429) #F3 
delay(429)  
tone(3,98,36) #G2
delay(36)  
tone(3,123,36) #B2 
delay(36)  
tone(3,147,36) #D3 
delay(36)  
tone(3,196,36) #G3 
delay(36)  
tone(3,247,36) #B3 
delay(36) 
tone(3,294,36) #D4 
delay(36) 
tone(3,392,928) #G4 
delay(1500) 

#Bridge

tone(3,392,286) #G4 
delay(286)  
tone(3,392,286) #G4 
delay(286)  
tone(3,392,828) #G4 
delay(828)  
tone(3,392,143) #G4 
delay(143)  
tone(3,349,143) #F4 
delay(143) 
tone(3,330,286) #E4 
delay(286)  
tone(3,330,143) #E4 
delay(143)  
tone(3,349,143) #F4 
delay(143) 
tone(3,392,286) #G4 
delay(286)    
tone(3,330,286) #E4 
delay(286)  
tone(3,294,572) #D4 
delay(572)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,294,286) #D4 
delay(286)  
tone(3,1568,286) #G6 
delay(286) 
tone(3,1318,286) #E6
delay(286) 
tone(3,1397,286) #F6
delay(286) 
tone(3,1175,286) #D6 
delay(286) 
tone(3,1318,286) #E6
delay(286) 
tone(3,1046,286) #C6 
delay(286)  
tone(3,1175,286) #D6 
delay(286) 
tone(3,880,190) #A5 
delay(190) 
tone(3,698,95) #F5 
delay(95) 
tone(3,784,286) #G5 
delay(286) 
tone(3,659,190) #E5 
delay(190) 
tone(3,698,95) #F5 
delay(95) 
tone(3,784,190) #G5 
delay(190) 
tone(3,1760,381) #A6
delay(381)  
tone(3,1568,572) #G6 
delay(1716) 
tone(3,392,286) #G4 
delay(286)  
tone(3,440,286) #A4 
delay(286)  
tone(3,392,828) #G4 
delay(828)  
tone(3,330,143) #E4 
delay(143)  
tone(3,349,143) #F4 
delay(143)  
tone(3,392,286) #G4 
delay(286)  
tone(3,349,143) #F4 
delay(143)  
tone(3,330,143) #E4 
delay(143) 
tone(3,294,286) #D4 
delay(286)  
tone(3,220,286) #A3 
delay(286)  
tone(3,196,286) #G3 
delay(286)  
tone(3,175,572) #F3 
delay(572)  
tone(3,220,286) #A3 
delay(286)  
tone(3,1568,286) #G6 
delay(286) 
tone(3,1318,286) #E6
delay(286) 
tone(3,1397,286) #F6
delay(286) 
tone(3,1175,286) #D6 
delay(286) 
tone(3,1318,286) #E6
delay(286) 
tone(3,1046,286) #C6 
delay(286)  
tone(3,1175,286) #D6 
delay(286) 
tone(3,880,286) #A5 
delay(286) 
tone(3,1760,286) #A6
delay(286) 
tone(3,1397,286) #F6
delay(286) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,1318,286) #E6
delay(286) 
tone(3,1397,286) #F6
delay(286) 
tone(3,1175,286) #D6 
delay(286) 
tone(3,1318,286) #E6
delay(286) 
tone(3,1046,286) #C6 
delay(286) 
tone(3,698,286) #F5 
delay(286)  
tone(3,880,572) #A5 
delay(572)  
tone(3,1046,286) #C6 
delay(286) 
tone(3,784,286) #G5 
delay(286) 
tone(3,988,572) #B5 
delay(572) 
tone(3,1175,286) #D6 
delay(286) 
tone(3,698,143) #F5 
delay(143)  
tone(3,784,143) #G5 
delay(143)  
tone(3,880,286) #A5 
delay(286) 
tone(3,880,143) #A5 
delay(143)  
tone(3,784,143) #G5 
delay(143) 
tone(3,880,286) #A5 
delay(286) 
tone(3,988,143) #B5 
delay(143) 
tone(3,784,143) #G5 
delay(143) 
tone(3,880,143) #A5 
delay(143) 
tone(3,988,143) #B5 
delay(143) 
tone(3,1175,143) #D6 
delay(143) 
tone(3,1480,143) #Gb/F#6
delay(143) 
tone(3,1568,286) #G6 
delay(286) 

#Bridge to end

tone(3,523,286) #C5 
delay(286)  
tone(3,392,143) #G4 
delay(143) 
tone(3,392,429) #G4 
delay(429) 
tone(3,392,572) #G4 
delay(572) 
tone(3,349,572) #F4 
delay(572)  
tone(3,330,286) #E4 
delay(286)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,277,143) #Db/C#4 
delay(143)  
tone(3,294,429) #D4 
delay(429) 
tone(3,330,572) #E4 
delay(572)  
tone(3,392,828) #G4 
delay(1144)  
tone(3,440,286) #A4 
delay(286)  
tone(3,392,143) #G4 
delay(143)  
tone(3,330,286) #E4 
delay(286)  
tone(3,294,429) #D4 
delay(572)  
tone(3,196,286) #G3 
delay(286)  
tone(3,220,143) #A3 
delay(143) 
tone(3,261,429) #C4(middle)      
delay(429) 
tone(3,220,286) #A3 
delay(286) 
tone(3,261,143) #C4(middle)      
delay(143)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,572) #C4(middle)      
delay(1430)  
tone(3,196,71) #G3 
delay(71)  
tone(3,220,71) #A3 
delay(71)  
tone(3,261,71) #C4(middle)      
delay(71)  
tone(3,330,71) #E4 
delay(71)  
tone(3,523,286) #C5 
delay(286)  
tone(3,392,143) #G4 
delay(143) 
tone(3,392,429) #G4 
delay(429) 
tone(3,392,572) #G4 
delay(572) 
tone(3,349,572) #F4 
delay(572)  
tone(3,330,286) #E4 
delay(286)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,277,143) #Db/C#4 
delay(143)  
tone(3,294,429) #D4 
delay(429) 
tone(3,330,572) #E4 
delay(572)  
tone(3,392,828) #G4 
delay(1144)  
tone(3,440,286) #A4 
delay(286)  
tone(3,392,143) #G4 
delay(143)  
tone(3,330,286) #E4 
delay(286)  
tone(3,294,429) #D4 
delay(572)  
tone(3,196,286) #G3 
delay(286)  
tone(3,220,143) #A3 
delay(143) 
tone(3,261,429) #C4(middle)      
delay(429) 
tone(3,220,286) #A3 
delay(286) 
tone(3,261,143) #C4(middle)      
delay(143)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,572) #C4(middle)      
delay(858)  
tone(3,196,286) #G3 
delay(286) 
tone(3,220,143) #A3 
delay(143) 
tone(3,261,429) #C4(middle)      
delay(429) 
tone(3,220,286) #A3 
delay(286)  
tone(3,261,143) #C4(middle)      
delay(143)  
tone(3,294,143) #D4 
delay(143) 
tone(3,261,572) #C4(middle)      
delay(572)  
tone(3,330,572) #E4 
delay(572)  
tone(3,349,286) #F4 
delay(286) 
tone(3,349,286) #F4 
delay(286) 
tone(3,330,143) #E4 
delay(143) 
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,220,143) #A3 
delay(143)  
tone(3,261,572) #C4(middle)      
delay(572)  
tone(3,392,828) #G4 
delay(828)  
tone(3,1568,286) #G6 
delay(286) 
tone(3,1318,286) #E6
delay(286) 
tone(3,1397,286) #F6
delay(286) 
tone(3,1046,572) #C6 
delay(572) 
tone(3,1760,572) #A6
delay(572) 
tone(3,1568,1430) #G6 
delay(1716) 
tone(3,196,286) #G3 
delay(286) 
tone(3,220,286) #A3 
delay(286)  
tone(3,261,143) #C4(middle)      
delay(143)  
tone(3,261,143) #C4(middle)      
delay(143) 

#End

tone(3,130,286) #C3 
delay(286)  
tone(3,196,143) #G3 
delay(143)  
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,286) #C4(middle)      
delay(286) 
tone(3,110,286) #A2
delay(286)  
tone(3,220,143) #A3 
delay(143) 
tone(3,261,286) #C4(middle)      
delay(286)  
tone(3,294,143) #D4 
delay(143)  
tone(3,261,286) #C4(middle)      
delay(286) 
tone(3,87,286) #F2
delay(286) 
tone(3,196,143) #G3 
delay(143)  
tone(3,220,286) #A3 
delay(286)  
tone(3,261,143) #C4(middle)      
delay(143) 
tone(3,220,286) #A3 
delay(286)  
tone(3,98,286) #G2
delay(286) 
tone(3,196,143) #G3 
delay(143)  
tone(3,220,286) #A3 
delay(286) 
tone(3,247,143) #B3 
delay(143)  
tone(3,196,286) #G3 
delay(286)  
tone(3,130,429) #C3 
delay(429)  
tone(3,1318,71) #E6
delay(71) 
tone(3,1397,71) #F6
delay(71) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,1568,286) #G6 
delay(286) 
tone(3,1568,828) #G6 
delay(828) 
tone(3,1568,143) #G6 
delay(143) 
tone(3,1397,143) #F6
delay(143) 
tone(3,1318,286) #E6
delay(286) 
tone(3,1397,143) #F6
delay(143) 
tone(3,1568,143) #G6 
delay(143) 
tone(3,1760,286) #A6
delay(286) 
tone(3,1975,286) #B6
delay(286) 
tone(3,1568,828) #G6 
delay(828) 
tone(3,1975,828) #B6
delay(828) 
tone(3,1568,572) #G6 
delay(572) 
tone(3,130,71) #C3 
delay(71) 
tone(3,165,71) #E3 
delay(71)  
tone(3,196,71) #G3 
delay(71)  
tone(3,261,71) #C4(middle)      
delay(71)  
tone(3,330,71) #E4 
delay(71)  
tone(3,392,1933) #G4 
delay(10000) 
