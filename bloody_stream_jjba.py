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

tone(3,261,114) #C4(middle)      
delay(114) 
tone(3,311,114) #Eb/D#4 
delay(114) 
tone(3,392,227) #G4 
delay(227)  
tone(3,370,341) #Gb/F#4 
delay(341) 
tone(3,349,227) #F4 
delay(227) 
tone(3,349,227) #F4 
delay(227)   
tone(3,261,114) #C4(middle)      
delay(114) 
tone(3,311,227) #Eb/D#4 
delay(227)  
tone(3,349,114) #F4 
delay(227)   
tone(3,261,114) #C4(middle)      
delay(114) 
tone(3,311,114) #Eb/D#4 
delay(114) 
tone(3,392,227) #G4 
delay(227)  
tone(3,370,341) #Gb/F#4 
delay(341) 
tone(3,349,227) #F4 
delay(227) 
tone(3,349,227) #F4 
delay(227)   
tone(3,261,114) #C4(middle)      
delay(114) 
tone(3,311,227) #Eb/D#4 
delay(227)  
tone(3,349,114) #F4 
delay(227)   
tone(3,261,114) #C4(middle)      
delay(114) 
tone(3,311,114) #Eb/D#4 
delay(114) 
tone(3,392,227) #G4 
delay(227)  
tone(3,370,341) #Gb/F#4 
delay(341) 
tone(3,349,227) #F4 
delay(227) 
tone(3,349,227) #F4 
delay(227)   
tone(3,261,114) #C4(middle)      
delay(114) 
tone(3,311,227) #Eb/D#4 
delay(227)  
tone(3,466,910) #Bb/A#4 
delay(1137) 

#First part first verse

tone(3,392,455) #G4 
delay(455) 
tone(3,392,455) #G4 
delay(455) 
tone(3,370,682) #Gb/F#4 
delay(682)  
tone(3,392,1137) #G4 
delay(2047) 
tone(3,311,455) #Eb/D#4 
delay(455)  
tone(3,349,455) #F4 
delay(455) 
tone(3,370,682) #Gb/F#4 
delay(682)  
tone(3,392,682) #G4 
delay(682) 
tone(3,311,455) #Eb/D#4 
delay(455)  
tone(3,349,1365) #F4 
delay(1592) 
tone(3,523,227) #C5 
delay(227)  
tone(3,392,227) #G4 
delay(227)  
tone(3,349,227) #F4 
delay(227) 
tone(3,311,114) #Eb/D#4 
delay(114)  
tone(3,349,227) #F4 
delay(227) 
tone(3,349,227) #F4 
delay(227) 
tone(3,261,114) #C4(middle)      
delay(114) 
tone(3,311,227) #Eb/D#4 
delay(227) 
tone(3,261,114) #C4(middle)      
delay(114) 
tone(3,311,1231) #Eb/D#4 
delay(1231) 
tone(3,311,227) #Eb/D#4 
delay(227) 
tone(3,349,227) #F4 
delay(227)  
tone(3,311,227) #Eb/D#4 
delay(227) 
tone(3,370,682) #Gb/F#4 
delay(682)  
tone(3,392,1137) #G4 
delay(1137) 
tone(3,622,114) #Eb/D#5 
delay(114) 
tone(3,698,227) #F5 
delay(227)  
tone(3,523,114) #C5 
delay(114) 
tone(3,622,227) #Eb/D#5 
delay(227)  
tone(3,466,114) #Bb/A#4 
delay(114)  
tone(3,523,227) #C5 
delay(227) 
tone(3,392,114) #G4 
delay(114) 
tone(3,261,114) #C4(middle)      
delay(114)  
tone(3,311,114) #Eb/D#4 
delay(114) 
tone(3,466,114) #Bb/A#4 
delay(114)  
tone(3,392,114) #G4 
delay(114)  
tone(3,622,114) #Eb/D#5 
delay(114)  
tone(3,261,114) #C4(middle)      
delay(114)  

#First part second part

tone(3,370,682) #Gb/F#4 
delay(682)  
tone(3,392,1137) #G4 
delay(2047) 
tone(3,311,455) #Eb/D#4 
delay(455)  
tone(3,349,455) #F4 
delay(455) 
tone(3,370,682) #Gb/F#4 
delay(682)  
tone(3,392,682) #G4 
delay(682) 
tone(3,311,455) #Eb/D#4 
delay(455)  
tone(3,349,455) #F4 
delay(455)  
tone(3,415,455) #Ab/G#4 
delay(455)  
tone(3,622,455) #Eb/D#5 
delay(455)  
tone(3,554,455) #Db/C#5 
delay(455) 
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,587,114) #D5 
delay(114)  
tone(3,622,341) #Eb/D#5 
delay(341) 
tone(3,587,227) #D5 
delay(227) 
tone(3,523,227) #C5 
delay(227)  
tone(3,587,114) #D5 
delay(114)  
tone(3,523,910) #C5 
delay(1365)  
tone(3,311,227) #Eb/D#4 
delay(227)  
tone(3,311,227) #Eb/D#4 
delay(227)  
tone(3,311,227) #Eb/D#4 
delay(227)  
tone(3,466,227) #Bb/A#4 
delay(227)  
tone(3,415,114) #Ab/G#4 
delay(114)  
tone(3,392,910) #G4 
delay(1479) 
tone(3,784,114) #G5 
delay(114) 
tone(3,831,114) #Ab/G#5 
delay(114)  
tone(3,932,104) #Bb/A#5 
delay(104)  
tone(3,932,10) #Bb/A#5 
delay(10) 
tone(3,622,104) #Eb/D#5 
delay(104)  
tone(3,622,10) #Eb/D#5 
delay(10)  
tone(3,698,10) #F5 
delay(10) 
tone(3,698,104) #F5 
delay(104) 
tone(3,784,10) #G5 
delay(10) 
tone(3,784,104) #G5 
delay(104) 
tone(3,494,114) #B4 
delay(114) 
tone(3,523,114) #C5 
delay(114)  
tone(3,587,114) #D5 
delay(114) 
tone(3,392,114) #G4 
delay(114) 
tone(3,440,114) #A4 
delay(114) 
tone(3,494,114) #B4 
delay(114) 
tone(3,392,114) #G4 
delay(114) 
tone(3,349,114) #F4 
delay(114) 
tone(3,311,114) #Eb/D#4 
delay(114) 
tone(3,294,114) #D4 
delay(114)  

#Second part

tone(3,523,455) #C5 
delay(455)  
tone(3,523,227) #C5 
delay(227)  
tone(3,466,114) #Bb/A#4 
delay(114)  
tone(3,523,910) #C5 
delay(1934)  
tone(3,523,341) #C5 
delay(341) 
tone(3,587,341) #D5 
delay(341) 
tone(3,622,227) #Eb/D#5 
delay(227) 
tone(3,587,1137) #D5 
delay(1137) 
tone(3,466,227) #Bb/A#4 
delay(227)  
tone(3,466,227) #Bb/A#4 
delay(227)  
tone(3,349,114) #F4 
delay(114) 
tone(3,392,1024) #G4 
delay(1934)  
tone(3,349,455) #F4 
delay(455) 
tone(3,392,227) #G4 
delay(227)  
tone(3,392,682) #G4 
delay(682) 
tone(3,261,227) #C4(middle)      
delay(227)  
tone(3,311,227) #Eb/D#4 
delay(1137)  
tone(3,392,341) #G4 
delay(341)  
tone(3,415,341) #Ab/G#4 
delay(341)  
tone(3,466,227) #Bb/A#4 
delay(227)  
tone(3,392,455) #G4 
delay(455) 
tone(3,247,455) #B3 
delay(455)  
tone(3,261,455) #C4(middle)      
delay(455)  
tone(3,294,455) #D4 
delay(455) 
tone(3,208,114) #Ab/G#3 
delay(114) 
tone(3,233,227) #Bb/A#3 
delay(227)  
tone(3,261,227) #C4(middle)      
delay(227)  
tone(3,294,227) #D4 
delay(227)  
tone(3,311,227) #Eb/D#4 
delay(227) 
tone(3,349,227) #F4 
delay(227)  
tone(3,392,227) #G4 
delay(227)  
tone(3,415,227) #Ab/G#4 
delay(796) 

#Third part first verse

tone(3,392,455) #G4 
delay(455)  
tone(3,494,455) #B4 
delay(455) 
tone(3,587,455) #D5 
delay(455)  
tone(3,622,227) #Eb/D#5 
delay(227)  
tone(3,587,227) #D5 
delay(227)  
tone(3,523,114) #C5 
delay(114)  
tone(3,466,227) #Bb/A#4 
delay(227)  
tone(3,523,114) #C5 
delay(227)  
tone(3,392,227) #G4 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,622,227) #Eb/D#5 
delay(227)  
tone(3,784,227) #G5 
delay(227) 
tone(3,698,227) #F5 
delay(227)  
tone(3,622,114) #Eb/D#5 
delay(114)  
tone(3,698,227) #F5 
delay(227) 
tone(3,622,114) #Eb/D#5 
delay(796) 
tone(3,466,114) #Bb/A#4 
delay(114)  
tone(3,466,114) #Bb/A#4 
delay(114)  
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,523,114) #C5 
delay(114) 
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,523,114) #C5 
delay(114)   
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,494,227) #B4 
delay(227) 
tone(3,494,114) #B4 
delay(114) 
tone(3,523,227) #C5 
delay(227)  
tone(3,587,1024) #D5 
delay(1024)  

tone(3,622,227) #Eb/D#5 
delay(227)  
tone(3,587,227) #D5 
delay(227)  
tone(3,523,114) #C5 
delay(114)  
tone(3,466,227) #Bb/A#4 
delay(227)  
tone(3,523,114) #C5 
delay(227)  
tone(3,392,227) #G4 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,622,227) #Eb/D#5 
delay(227)  
tone(3,784,682) #G5 
delay(682) 
tone(3,466,227) #Bb/A#4 
delay(227) 
tone(3,831,227) #Ab/G#5 
delay(227)  
tone(3,784,227) #G5 
delay(227)  
tone(3,698,227) #F5 
delay(227)  
tone(3,784,227) #G5 
delay(227)  
tone(3,698,682) #F5 
delay(682) 
tone(3,622,1137) #Eb/D#5 
delay(1137)  
tone(3,392,114) #G4 
delay(114) 
tone(3,415,114) #Ab/G#4 
delay(114)  
tone(3,466,114) #Bb/A#4 
delay(114)  
tone(3,587,114) #D5 
delay(114)  
tone(3,622,114) #Eb/D#5 
delay(114)  
tone(3,698,114) #F5 
delay(114)  
tone(3,831,114) #Ab/G#5 
delay(114)  
tone(3,932,114) #Bb/A#5 
delay(114)  
tone(3,988,227) #B5 
delay(227)  
tone(3,392,682) #G4 
delay(682)  

#Third part second verse

tone(3,622,227) #Eb/D#5 
delay(227)  
tone(3,587,227) #D5 
delay(227)  
tone(3,523,114) #C5 
delay(114)  
tone(3,466,227) #Bb/A#4 
delay(227)  
tone(3,523,114) #C5 
delay(227)  
tone(3,392,227) #G4 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,622,227) #Eb/D#5 
delay(227)  
tone(3,784,227) #G5 
delay(227) 
tone(3,698,227) #F5 
delay(227)  
tone(3,622,114) #Eb/D#5 
delay(114)  
tone(3,698,227) #F5 
delay(227) 
tone(3,622,114) #Eb/D#5 
delay(796) 
tone(3,466,114) #Bb/A#4 
delay(114)  
tone(3,466,114) #Bb/A#4 
delay(114)  
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,523,114) #C5 
delay(114) 
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,523,114) #C5 
delay(114)   
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,494,227) #B4 
delay(227) 
tone(3,494,114) #B4 
delay(114) 
tone(3,523,227) #C5 
delay(227)  
tone(3,587,1024) #D5 
delay(1024)  
tone(3,622,227) #Eb/D#5 
delay(227)  
tone(3,587,227) #D5 
delay(227)  
tone(3,523,114) #C5 
delay(114)  
tone(3,466,227) #Bb/A#4 
delay(227)  
tone(3,523,114) #C5 
delay(227)  
tone(3,392,227) #G4 
delay(227)  
tone(3,523,227) #C5 
delay(227)  
tone(3,622,227) #Eb/D#5 
delay(227)  
tone(3,784,227) #G5 
delay(227) 
tone(3,698,227) #F5 
delay(227)  
tone(3,622,114) #Eb/D#5 
delay(114)  
tone(3,698,227) #F5 
delay(227) 
tone(3,622,114) #Eb/D#5 
delay(341) 
tone(3,392,227) #G4 
delay(227)  
tone(3,392,227) #G4 
delay(227)  
tone(3,784,1592) #G5 
delay(1820)  

#ending

tone(3,392,910) #G4 
delay(910)  
tone(3,587,455) #D5 
delay(455)  
tone(3,698,227) #F5 
delay(227)  
tone(3,622,144) #Eb/D#5 
delay(144)  
tone(3,587,227) #D5 
delay(227)  
tone(3,523,3526) #C5 
delay(3526)  
tone(3,261,3185) #C4(middle)      
delay(10000)  
