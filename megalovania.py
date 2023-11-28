# Original script is credited to Github user "AnonymousAlly"
# https://github.com/AnonymousAlly/Arduino-Music-Codes/tree/master

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
    time.sleep(seconds/1000)

def tone(r,hertz,duration):
    pwm = GPIO.PWM(spkrOne,hertz)
    pwm.start(50)
    pwm.ChangeFrequency(hertz)
    delay(duration)
    pwm.stop

tone(3,294,125) #D4
delay(125) 
tone(3,294,125) #D4
delay(125) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,250) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,247,125) #B3
delay(125) 
tone(3,247,125) #B3
delay(125) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,294,125) #D4
delay(125) 
tone(3,294,125) #D4
delay(125) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,247,125) #B3
delay(125) 
tone(3,247,125) #B3
delay(125) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,588,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 

#DOEH DEH DEH AH DAH DOOEH DOO AH (INTENSIFIES)

tone(3,587,125) #D5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,1175,250) #D6
delay(250) 
tone(3,880,250) #A5
delay(325) 
tone(3,831,125) #Ab5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,587,125) #D5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,523,125) #C5
delay(125) 
tone(3,523,125) #C5
delay(125) 
tone(3,1175,250) #D6
delay(250) 
tone(3,880,250) #A5
delay(325) 
tone(3,831,125) #Ab5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,587,125) #D5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,494,125) #B4
delay(125) 
tone(3,494,125) #B4
delay(125) 
tone(3,1175,250) #D6
delay(250) 
tone(3,880,250) #A5
delay(325) 
tone(3,831,125) #Ab5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,587,125) #D5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,466,125) #Bb4
delay(125) 
tone(3,466,125) #Bb4
delay(125) 
tone(3,1175,250) #D6
delay(250) 
tone(3,880,250) #A5
delay(325) 
tone(3,831,125) #Ab5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,587,125) #D5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,1175,250) #D6
delay(250) 
tone(3,880,250) #A5
delay(325) 
tone(3,831,125) #Ab5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,587,125) #D5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,523,125) #C5
delay(125) 
tone(3,523,125) #C5
delay(125) 
tone(3,1175,250) #D6
delay(250) 
tone(3,880,250) #A5
delay(325) 
tone(3,831,125) #Ab5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,587,125) #D5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,494,125) #B4
delay(125) 
tone(3,494,125) #B4
delay(125) 
tone(3,1175,250) #D6
delay(250) 
tone(3,880,250) #A5
delay(325) 
tone(3,831,125) #Ab5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,587,125) #D5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,466,125) #Bb4
delay(125) 
tone(3,466,125) #Bb4
delay(125) 
tone(3,1175,250) #D6
delay(250) 
tone(3,880,250) #A5
delay(325) 
tone(3,831,125) #Ab5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,587,125) #D5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,125) #G5
delay(125) 

#DU DU DUDU DU DU DU

tone(3,698,250) #F5
delay(250) 
tone(3,698,125) #F5
delay(125) 
tone(3,698,125) #F5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,587,250) #D5
delay(250) 
tone(3,587,625) #D5
delay(625) 
tone(3,698,250) #F5
delay(250) 
tone(3,698,125) #F5
delay(125) 
tone(3,698,125) #F5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,831,250) #Ab5
delay(250) 
tone(3,784,42) #G5
delay(42) 
tone(3,831,42) #Ab5
delay(42) 
tone(3,784,42) #G5
delay(42) 
tone(3,698,125) #F5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,125) #G5
delay(375) 
tone(3,698,250) #F5
delay(250) 
tone(3,698,125) #F5
delay(125) 
tone(3,698,125) #F5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,831,125) #Ab5
delay(250) 
tone(3,880,250) #A5
delay(250) 
tone(3,1046,250) #C6
delay(250) 
tone(3,880,375) #A5
delay(375) 
tone(3,1175,250) #D6
delay(250) 
tone(3,1175,250) #D6
delay(250) 
tone(3,1175,125) #D6
delay(125) 
tone(3,880,125) #A5
delay(125) 
tone(3,1175,125) #D6
delay(125) 
tone(3,1046,625) #C6
delay(625) 
tone(3,1568,500) #G6
delay(500) 

#DU DU DUDU DU DU DUU (INTENSIFIES)

tone(3,880,250) #A5
delay(250) 
tone(3,880,125) #A5
delay(125) 
tone(3,880,125) #A5
delay(250) 
tone(3,880,250) #A5
delay(250) 
tone(3,880,250) #A5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,784,625) #G5
delay(625) 
tone(3,880,250) #A5
delay(250) 
tone(3,880,125) #A5
delay(125) 
tone(3,880,125) #A5
delay(250) 
tone(3,880,250) #A5
delay(250) 
tone(3,784,125) #G5
delay(250) 
tone(3,880,250) #A5
delay(250) 
tone(3,1175,125) #D6
delay(250) 
tone(3,880,125) #A5
delay(125) 
tone(3,784,250) #G5
delay(250) 
tone(3,1175,250) #D6
delay(250) 
tone(3,880,250) #A5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,1046,250) #C6
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,659,250) #E5
delay(250) 
tone(3,466,250) #Bb4
delay(250) 
tone(3,523,125) #C5
delay(125) 
tone(3,587,125) #D5
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,1046,1125) #C6
delay(2125) 

#Epic part

tone(3,698,125) #F5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,831,125) #Ab5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,831,63) #Ab5
delay(63) 
tone(3,784,63) #G5
delay(63) 
tone(3,698,63) #F5
delay(63) 
tone(3,587,63) #D5
delay(63) 
tone(3,698,250) #F5
delay(250) 
tone(3,784,1125) #G5
delay(1125) 
tone(3,831,250) #Ab5
delay(250) 
tone(3,880,125) #A5
delay(125) 
tone(3,1046,250) #C6
delay(250) 
tone(3,880,125) #A5
delay(125) 
tone(3,831,125) #Ab5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,659,125) #E5
delay(125) 
tone(3,698,250) #F5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,880,250) #A5
delay(250) 
tone(3,1046,250) #C6
delay(250) 
tone(3,1109,250) #Db6
delay(250) 
tone(3,831,250) #Ab5
delay(250) 
tone(3,831,125) #Ab5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,1125) #G5
delay(1125) 
tone(3,349,250) #F4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,440,250) #A4
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,659,500) #E5
delay(500) 
tone(3,587,500) #D5
delay(500) 
tone(3,659,500) #E5
delay(500) 
tone(3,698,500) #F5
delay(500) 
tone(3,784,500) #G5
delay(500) 
tone(3,659,500) #E5
delay(500) 
tone(3,880,1000) #A5
delay(1000) 
tone(3,880,125) #A5
delay(125) 
tone(3,831,125) #Ab5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,740,125) #Gb5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,659,125) #E5
delay(125) 
tone(3,622,125) #Eb5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,554,1000) #Db5
delay(1000) 
tone(3,622,1000) #Eb5
delay(2000) 
tone(3,698,125) #F5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,831,125) #Ab5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,831,63) #Ab5
delay(63) 
tone(3,784,63) #G5
delay(63) 
tone(3,698,63) #F5
delay(63) 
tone(3,587,63) #D5
delay(63) 
tone(3,698,250) #F5
delay(250) 
tone(3,784,1125) #G5
delay(1125) 
tone(3,831,250) #Ab5
delay(250) 
tone(3,880,125) #A5
delay(125) 
tone(3,1046,250) #C6
delay(250) 
tone(3,880,125) #A5
delay(125) 
tone(3,831,125) #Ab5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,659,125) #E5
delay(125) 
tone(3,698,250) #F5
delay(250) 
tone(3,784,250) #G5
delay(250) 
tone(3,880,250) #A5
delay(250) 
tone(3,1046,250) #C6
delay(250) 
tone(3,1109,250) #Db6
delay(250) 
tone(3,831,250) #Ab5
delay(250) 
tone(3,831,125) #Ab5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,784,1125) #G5
delay(1125) 
tone(3,349,250) #F4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,440,250) #A4
delay(250) 
tone(3,698,250) #F5
delay(250) 
tone(3,659,500) #E5
delay(500) 
tone(3,587,500) #D5
delay(500) 
tone(3,659,500) #E5
delay(500) 
tone(3,698,500) #F5
delay(500) 
tone(3,784,500) #G5
delay(500) 
tone(3,659,500) #E5
delay(500) 
tone(3,880,1000) #A5
delay(1000) 
tone(3,880,125) #A5
delay(125) 
tone(3,831,125) #Ab5
delay(125) 
tone(3,784,125) #G5
delay(125) 
tone(3,740,125) #Gb5
delay(125) 
tone(3,698,125) #F5
delay(125) 
tone(3,659,125) #E5
delay(125) 
tone(3,622,125) #Eb5
delay(125) 
tone(3,587,125) #D5
delay(125) 
tone(3,554,1000) #Db5
delay(1000) 
tone(3,622,1000) #Eb5
delay(1000) 

#Opera

tone(3,233,1500) #Bb3
delay(1500) 
tone(3,349,500) #F4
delay(500) 
tone(3,330,1000) #E4
delay(1000) 
tone(3,294,1000) #D4
delay(1000) 
tone(3,349,4000) #F4
delay(4000) 
tone(3,233,1500) #Bb3
delay(1500) 
tone(3,349,500) #F4
delay(500) 
tone(3,330,1000) #E4
delay(1000) 
tone(3,294,1000) #D4
delay(1000) 
tone(3,294,1000) #D4
delay(1000) 
tone(3,294,83) #D4
delay(83) 
tone(3,277,83) #Db4
delay(83) 
tone(3,261,83) #C4(middle)     
delay(83) 
tone(3,247,83) #B3
delay(83) 
tone(3,233,83) #Bb3
delay(83) 
tone(3,220,83) #A3
delay(83) 
tone(3,208,83) #Ab3
delay(83) 
tone(3,196,83) #G3
delay(83) 
tone(3,185,83) #Gb3
delay(83) 
tone(3,175,83) #F3
delay(83) 
tone(3,165,83) #E3
delay(83) 
tone(3,156,83) #Eb3
delay(83) 
tone(3,147,2000) #D3
delay(2000) 
tone(3,233,1500) #Bb3
delay(1500) 
tone(3,349,500) #F4
delay(500) 
tone(3,330,1000) #E4
delay(1000) 
tone(3,294,1000) #D4
delay(1000) 
tone(3,349,2000) #F4
delay(2000) 
tone(3,123,125) #B2
delay(125) 
tone(3,196,125) #G3
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,294,125) #D4
delay(125) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,125) #F4
delay(125) 
tone(3,261,125) #C4(middle)     
delay(125) 
tone(3,294,125) #D4
delay(125) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,220,250) #A3
delay(250) 
tone(3,196,125) #G3
delay(125) 
tone(3,261,125) #C4(middle)     
delay(125) 
tone(3,233,1500) #Bb3
delay(1500) 
tone(3,349,500) #F4
delay(500) 
tone(3,330,1000) #E4
delay(1000) 
tone(3,294,1000) #D4
delay(1000) 
tone(3,147,125) #D3
delay(125) 
tone(3,147,125) #D3
delay(125) 
tone(3,349,250) #F4
delay(250) 
tone(3,330,250) #E4
delay(250) 
tone(3,261,125) #C4(middle)     
delay(250) 
tone(3,330,250) #E4
delay(250) 
tone(3,247,250) #B3
delay(250) 
tone(3,196,125) #G3
delay(125) 
tone(3,220,125) #A3
delay(125) 
tone(3,261,125) #C4(middle)     
delay(125) 
tone(3,147,125) #D3
delay(125) 
tone(3,147,125) #D3
delay(125) 
tone(3,349,250) #F4
delay(250) 
tone(3,330,250) #E4
delay(250) 
tone(3,261,125) #C4(middle)     
delay(250) 
tone(3,330,250) #E4
delay(250) 
tone(3,247,250) #B3
delay(250) 
tone(3,196,125) #G3
delay(125) 
tone(3,220,125) #A3
delay(125) 
tone(3,261,125) #C4(middle)     
delay(125) 

#rock part

tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,130,125) #C3
delay(125) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,130,125) #C3
delay(125) 
tone(3,130,125) #C3
delay(125) 
tone(3,130,125) #C3
delay(125) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,147,125) #D3
delay(125) 
tone(3,294,250) #D4
delay(250) 
tone(3,277,250) #Db4
delay(250) 
tone(3,277,250) #Db4
delay(250) 
tone(3,139,125) #Db3
delay(125) 
tone(3,139,125) #Db3
delay(125) 
tone(3,139,125) #Db3
delay(125) 
tone(3,277,250) #Db4
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,130,125) #C3
delay(125) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,247,250) #B3
delay(250) 
tone(3,247,250) #B3
delay(250) 
tone(3,123,125) #B2
delay(125) 
tone(3,123,125) #B2
delay(125) 
tone(3,123,125) #B2
delay(125) 
tone(3,247,250) #B3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,130,125) #C3
delay(125) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,130,125) #C3
delay(125) 
tone(3,130,125) #C3
delay(125) 
tone(3,130,125) #C3
delay(125) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,147,125) #D3
delay(125) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,147,125) #D3
delay(125) 
tone(3,147,125) #D3
delay(125) 
tone(3,147,125) #D3
delay(125) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,147,125) #D3
delay(125) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,147,125) #D3
delay(125) 
tone(3,147,125) #D3
delay(125) 
tone(3,147,125) #D3
delay(125) 
tone(3,294,250) #D4
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,130,125) #C3
delay(125) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,130,125) #C3
delay(125) 
tone(3,130,125) #C3
delay(125) 
tone(3,130,125) #C3
delay(125) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,147,125) #D3
delay(125) 
tone(3,294,250) #D4
delay(250) 
tone(3,277,250) #Db4
delay(250) 
tone(3,277,250) #Db4
delay(250) 
tone(3,139,125) #Db3
delay(125) 
tone(3,139,125) #Db3
delay(125) 
tone(3,139,125) #Db3
delay(125) 
tone(3,277,250) #Db4
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,130,125) #C3
delay(125) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,247,250) #B3
delay(250) 
tone(3,247,250) #B3
delay(250) 
tone(3,123,125) #B2
delay(125) 
tone(3,123,125) #B2
delay(125) 
tone(3,123,125) #B2
delay(125) 
tone(3,247,250) #B3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,116,125) #Bb2
delay(125) 
tone(3,233,250) #Bb3
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,130,125) #C3
delay(125) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,261,250) #C4(middle)     
delay(250) 
tone(3,130,125) #C3
delay(125) 
tone(3,130,125) #C3
delay(125) 
tone(3,130,125) #C3
delay(125) 
tone(3,261,250) #C4(middle)
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,147,125) #D3
delay(125) 
tone(3,294,250) #D4
delay(250) 
tone(3,220,125) #A3
delay(125) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,175,250) #F3
delay(250) 
tone(3,147,125) #D3
delay(125) 
tone(3,294,125) #D4
delay(125) 
tone(3,196,125) #G3
delay(125) 
tone(3,294,125) #D4
delay(125) 
tone(3,147,125) #D3
delay(125) 
tone(3,294,250) #D4
delay(250) 
tone(3,220,125) #A3
delay(125) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,294,250) #D4
delay(250) 
tone(3,175,250) #F3
delay(250) 
tone(3,147,125) #D3
delay(125) 
tone(3,294,125) #D4
delay(125) 
tone(3,196,125) #G3
delay(125) 

#99999999999999999999999999999999999999999999999999999999999999

tone(3,294,125) #D4
delay(125) 
tone(3,294,125) #D4
delay(125) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,250) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,247,125) #B3
delay(125) 
tone(3,247,125) #B3
delay(125) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,233,62) #Bb3
delay(62) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,294,125) #D4
delay(125) 
tone(3,294,125) #D4
delay(125) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(125) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,261,125) #C4(middle)     
delay(62) 
tone(3,587,250) #D5
delay(250) 
tone(3,440,375) #A4
delay(375) 
tone(3,415,125) #Ab4
delay(250) 
tone(3,392,250) #G4
delay(250) 
tone(3,349,250) #F4
delay(250) 
tone(3,294,125) #D4
delay(125) 
tone(3,349,125) #F4
delay(125) 
tone(3,392,125) #G4
delay(4125)