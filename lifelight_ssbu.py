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

tone(3,330,310) #E4 
delay(310)  
tone(3,370,310) #Gb/F#4 
delay(310) 
tone(3,392,414) #G4 
delay(414)   
tone(3,330,207) #E4 
delay(207)  
tone(3,392,207) #G4 
delay(207)  
tone(3,587,207) #D5 
delay(207)  
tone(3,554,310) #Db/C#5 
delay(310)  
tone(3,494,310) #B4 
delay(310) 
tone(3,554,207) #Db/C#5 
delay(207)  
tone(3,659,828) #E5 
delay(828) 
tone(3,523,310) #C5 
delay(310) 
tone(3,494,310) #B4 
delay(310) 
tone(3,440,414) #A4 
delay(414)  
tone(3,392,207) #G4 
delay(207)  
tone(3,440,207) #A4 
delay(207)  
tone(3,494,207) #B4 
delay(207) 
tone(3,440,310) #A4 
delay(310)  
tone(3,392,310) #G4 
delay(310)  
tone(3,440,207) #A4 
delay(207)  
tone(3,370,310) #Gb/F#4 
delay(310) 
tone(3,440,310) #A4 
delay(310)  
tone(3,587,207) #D5 
delay(207)  
tone(3,659,3312) #E5 
delay(3312)  

#First Line

tone(3,392,414) #G4 
delay(414)  
tone(3,440,414) #A4 
delay(414)  
tone(3,370,621) #Gb/F#4 
delay(621)  
tone(3,330,103) #E4 
delay(103)  
tone(3,370,103) #Gb/F#4 
delay(103) 
tone(3,392,310) #G4 
delay(310) 
tone(3,440,310) #A4 
delay(310)  
tone(3,494,207) #B4 
delay(207)  
tone(3,440,828) #A4 
delay(828)  
tone(3,392,414) #G4 
delay(414)  
tone(3,440,414) #A4 
delay(414)  
tone(3,370,310) #Gb/F#4 
delay(310) 
tone(3,330,310) #E4 
delay(310)  
tone(3,294,207) #D4 
delay(207)  
tone(3,330,1656) #E4 
delay(1656)  
tone(3,392,414) #G4 
delay(414)  
tone(3,440,414) #A4 
delay(414)  
tone(3,370,621) #Gb/F#4 
delay(621)  
tone(3,330,103) #E4 
delay(103)  
tone(3,370,103) #Gb/F#4 
delay(103) 
tone(3,392,310) #G4 
delay(310) 
tone(3,440,310) #A4 
delay(310)  
tone(3,494,207) #B4 
delay(207)  
tone(3,440,310) #A4 
delay(310)  
tone(3,370,310) #Gb/F#4 
delay(310)  
tone(3,294,207) #D4 
delay(207)  
tone(3,330,828) #E4 
delay(828)  
tone(3,330,310) #E4 
delay(310)  
tone(3,370,310) #Gb/F#4 
delay(310)  
tone(3,392,207) #G4 
delay(207) 
tone(3,440,828) #A4 
delay(828)  
tone(3,494,828) #B4 
delay(828) 

#Second Line

tone(3,784,414) #G5 
delay(414)  
tone(3,880,414) #A5 
delay(414) 
tone(3,740,621) #Gb/F#5 
delay(621)   
tone(3,659,103) #E5 
delay(103)  
tone(3,740,103) #Gb/F#5 
delay(103)   
tone(3,784,310) #G5 
delay(310) 
tone(3,880,310) #A5 
delay(310) 
tone(3,988,207) #B5 
delay(207)  
tone(3,880,777) #A5 
delay(777) 
tone(3,880,51) #A5 
delay(51) 
tone(3,784,414) #G5 
delay(414)  
tone(3,880,414) #A5 
delay(414) 
tone(3,740,310) #Gb/F#5 
delay(310)   
tone(3,659,310) #E5 
delay(310)  
tone(3,587,207) #D5 
delay(207)  
tone(3,659,828) #E5 
delay(828)  
tone(3,554,828) #Db/C#5 
delay(828) 
tone(3,784,414) #G5 
delay(414)  
tone(3,880,414) #A5 
delay(414) 
tone(3,740,621) #Gb/F#5 
delay(621)   
tone(3,659,103) #E5 
delay(103)  
tone(3,740,103) #Gb/F#5 
delay(103)   
tone(3,784,310) #G5 
delay(310) 
tone(3,880,310) #A5 
delay(310) 
tone(3,988,207) #B5 
delay(207)  
tone(3,880,310) #A5 
delay(310) 
tone(3,740,310) #Gb/F#5 
delay(310)  
tone(3,587,207) #D5 
delay(207)  
tone(3,659,828) #E5 
delay(828)  
tone(3,659,310) #E5 
delay(310)  
tone(3,740,310) #Gb/F#5 
delay(310)  
tone(3,784,207) #G5 
delay(207)  
tone(3,880,414) #A5 
delay(414)  
tone(3,1175,414) #D6 
delay(414) 
tone(3,988,828) #B5 
delay(828) 

#Bridge 1

tone(3,880,1656) #A5 
delay(1656)  
tone(3,784,310) #G5 
delay(310)  
tone(3,698,310) #F5 
delay(310) 
tone(3,784,207) #G5 
delay(207)  
tone(3,587,828) #D5 
delay(828) 
tone(3,988,828) #B5 
delay(828)   
tone(3,988,310) #B5 
delay(310) 
tone(3,784,310) #G5 
delay(310)  
tone(3,659,207) #E5 
delay(207)  
tone(3,587,414) #D5 
delay(414)  
tone(3,523,621) #C5 
delay(621)  
tone(3,523,207) #C5 
delay(207)  
tone(3,494,207) #B4 
delay(207) 
tone(3,523,207) #C5 
delay(207)  
tone(3,440,621) #A4 
delay(621) 
tone(3,880,621) #A5 
delay(621)  
tone(3,659,207) #E5 
delay(207)   
tone(3,622,1035) #Eb/D#5 
delay(1242)  
tone(3,1046,207) #C6 
delay(207)  
tone(3,988,207) #B5 
delay(207)  
tone(3,880,103) #A5 
delay(207)  
tone(3,880,828) #A5 
delay(1035) 
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,880,207) #A5 
delay(207)  
tone(3,988,1449) #B5 
delay(1863)  

#Third Line

tone(3,196,414) #G3 
delay(414)   
tone(3,220,414) #A3 
delay(414)  
tone(3,185,621) #Gb/F#3 
delay(621)  
tone(3,165,103) #E3 
delay(103)  
tone(3,185,103) #Gb/F#3 
delay(103)  
tone(3,196,310) #G3 
delay(310)   
tone(3,220,310) #A3 
delay(310) 
tone(3,247,207) #B3 
delay(207)   
tone(3,220,828) #A3 
delay(828) 
tone(3,196,414) #G3 
delay(414)   
tone(3,220,414) #A3 
delay(414)  
tone(3,185,310) #Gb/F#3 
delay(310)  
tone(3,165,310) #E3 
delay(310)  
tone(3,147,207) #D3 
delay(207)  
tone(3,165,1656) #E3 
delay(1656)  
tone(3,196,414) #G3 
delay(414)   
tone(3,220,414) #A3 
delay(414)  
tone(3,185,621) #Gb/F#3 
delay(621)  
tone(3,165,103) #E3 
delay(103)  
tone(3,185,103) #Gb/F#3 
delay(103)  
tone(3,196,310) #G3 
delay(310)   
tone(3,220,310) #A3 
delay(310) 
tone(3,247,207) #B3 
delay(207)   
tone(3,220,310) #A3 
delay(310) 
tone(3,185,310) #Gb/F#3 
delay(310)  
tone(3,147,207) #D3 
delay(207)  
tone(3,165,828) #E3 
delay(828)  
tone(3,165,310) #E3 
delay(310)  
tone(3,185,310) #Gb/F#3 
delay(310)  
tone(3,196,207) #G3 
delay(207)  
tone(3,220,414) #A3 
delay(414)  
tone(3,294,414) #D4 
delay(414)  
tone(3,247,828) #B3 
delay(828)  

#Bridge Two

tone(3,220,1656) #A3 
delay(1656) 
tone(3,196,310) #G3 
delay(310)  
tone(3,175,310) #F3 
delay(310)  
tone(3,196,207) #G3 
delay(207)  
tone(3,147,828) #D3 
delay(828)  
tone(3,247,828) #B3 
delay(828)  
tone(3,247,310) #B3 
delay(310)  
tone(3,196,310) #G3 
delay(310)  
tone(3,165,207) #E3 
delay(207) 
tone(3,147,414) #D3 
delay(414) 
tone(3,130,621) #C3 
delay(621)  
tone(3,523,207) #C5 
delay(207)  
tone(3,494,207) #B4 
delay(207) 
tone(3,523,207) #C5 
delay(207)   
tone(3,440,621) #A4 
delay(621) 
tone(3,880,621) #A5 
delay(621)  
tone(3,659,207) #E5 
delay(207) 
tone(3,622,1242) #Eb/D#5 
delay(1242) 
tone(3,1046,207) #C6 
delay(207)  
tone(3,988,207) #B5 
delay(207)  
tone(3,880,207) #A5 
delay(207)  
tone(3,880,1035) #A5 
delay(1035)  
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,880,207) #A5 
delay(207)  
tone(3,988,1449) #B5 
delay(1449)  
tone(3,175,207) #F3 
delay(207)  
tone(3,175,207) #F3 
delay(207)  
tone(3,233,310) #Bb/A#3 
delay(310)  
tone(3,233,310) #Bb/A#3 
delay(310)  
tone(3,208,310) #Ab/G#3 
delay(310) 
tone(3,208,310) #Ab/G#3 
delay(310) 

#Bridge Three

tone(3,261,51) #C4(middle)      
delay(51)  
tone(3,294,51) #D4 
delay(51)  
tone(3,330,51) #E4 
delay(51)  
tone(3,349,51) #F4 
delay(51)  
tone(3,392,51) #G4 
delay(51)  
tone(3,440,51) #A4 
delay(51)  
tone(3,494,51) #B4 
delay(51) 
tone(3,587,51) #D5 
delay(51)  
tone(3,659,1863) #E5 
delay(1863)   
tone(3,294,207) #D4 
delay(207)  
tone(3,220,414) #A3 
delay(414)  
tone(3,196,310) #G3 
delay(310)  
tone(3,185,310) #Gb/F#3 
delay(310)  
tone(3,147,207) #D3 
delay(207)  
tone(3,165,414) #E3 
delay(414)  
tone(3,1318,414) #E6
delay(414) 
tone(3,880,310) #A5 
delay(310)  
tone(3,784,310) #G5 
delay(310) 
tone(3,740,207) #Gb/F#5 
delay(207)  
tone(3,659,1656) #E5 
delay(1656)  
tone(3,349,310) #F4 
delay(310)  
tone(3,392,310) #G4 
delay(310)   
tone(3,415,414) #Ab/G#4 
delay(414)  
tone(3,349,207) #F4 
delay(207)  
tone(3,415,207) #Ab/G#4 
delay(207)  
tone(3,622,207) #Eb/D#5 
delay(207)  
tone(3,587,310) #D5 
delay(310)  
tone(3,523,310) #C5 
delay(310)  
tone(3,587,207) #D5 
delay(207)  
tone(3,466,828) #Bb/A#4 
delay(828)  
tone(3,415,310) #Ab/G#4 
delay(310)  
tone(3,415,310) #Ab/G#4 
delay(310)  
tone(3,466,310) #Bb/A#4 
delay(310)  
tone(3,466,207) #Bb/A#4 
delay(207)  
tone(3,466,103) #Bb/A#4 
delay(103)  
tone(3,466,103) #Bb/A#4 
delay(103)  
tone(3,523,310) #C5 
delay(310)  
tone(3,523,310) #C5 
delay(310)  
tone(3,554,828) #Db/C#5 
delay(1035) 
tone(3,466,414) #Bb/A#4 
delay(414) 
tone(3,523,414) #C5 
delay(414)  
tone(3,440,828) #A4 
delay(828)   
tone(3,466,310) #Bb/A#4 
delay(310) 
tone(3,523,310) #C5 
delay(310) 
tone(3,554,207) #Db/C#5 
delay(207)  
tone(3,523,310) #C5 
delay(310) 
tone(3,622,310) #Eb/D#5 
delay(310)  
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,932,310) #Bb/A#5 
delay(310)  
tone(3,523,310) #C5 
delay(310) 
tone(3,554,207) #Db/C#5 
delay(207)  
tone(3,523,310) #C5 
delay(310) 
tone(3,622,310) #Eb/D#5 
delay(310)  
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,932,1656) #Bb/A#5 
delay(2484) 

#SNAAAAAAAAAAAAAAAAAAAAAAKE

tone(3,165,828) #E3 
delay(828)  
tone(3,659,414) #E5 
delay(414) 
tone(3,494,51) #B4 
delay(51) 
tone(3,523,51) #C5 
delay(51)  
tone(3,587,51) #D5 
delay(51)  
tone(3,659,51) #E5 
delay(51)  
tone(3,784,414) #G5 
delay(414)  
tone(3,880,51) #A5 
delay(51) 
tone(3,988,51) #B5 
delay(51)   
tone(3,1046,51) #C6 
delay(51) 
tone(3,1175,51) #D6 
delay(51) 
tone(3,1318,414) #E6
delay(414)  

#Fourth Line

tone(3,330,310) #E4 
delay(310)  
tone(3,370,310) #Gb/F#4 
delay(310)  
tone(3,392,414) #G4 
delay(414)  
tone(3,330,207) #E4 
delay(207)  
tone(3,392,207) #G4 
delay(207)  
tone(3,587,207) #D5 
delay(207)  
tone(3,554,310) #Db/C#5 
delay(310)  
tone(3,494,310) #B4 
delay(310) 
tone(3,554,207) #Db/C#5 
delay(207)  
tone(3,440,828) #A4 
delay(828) 
tone(3,523,310) #C5 
delay(310)   
tone(3,494,310) #B4 
delay(310) 
tone(3,440,414) #A4 
delay(414) 
tone(3,392,207) #G4 
delay(207)  
tone(3,440,207) #A4 
delay(207) 
tone(3,494,207) #B4 
delay(207) 
tone(3,440,310) #A4 
delay(310)  
tone(3,392,310) #G4 
delay(310)  
tone(3,440,207) #A4 
delay(207)  
tone(3,370,828) #Gb/F#4 
delay(828)  
tone(3,330,310) #E4 
delay(310)  
tone(3,370,310) #Gb/F#4 
delay(310)  
tone(3,392,414) #G4 
delay(414)  
tone(3,330,207) #E4 
delay(207)  
tone(3,392,207) #G4 
delay(207)  
tone(3,587,207) #D5 
delay(207)  
tone(3,554,310) #Db/C#5 
delay(310)  
tone(3,494,310) #B4 
delay(310) 
tone(3,554,207) #Db/C#5 
delay(207)  
tone(3,659,828) #E5 
delay(828)  
tone(3,523,310) #C5 
delay(310)   
tone(3,494,310) #B4 
delay(310) 
tone(3,440,414) #A4 
delay(414) 
tone(3,392,207) #G4 
delay(207)  
tone(3,440,207) #A4 
delay(207) 
tone(3,494,207) #B4 
delay(207) 
tone(3,440,310) #A4 
delay(310)  
tone(3,392,310) #G4 
delay(310)  
tone(3,440,207) #A4 
delay(207)  
tone(3,370,828) #Gb/F#4 
delay(828)  

#Fifth Line

tone(3,659,310) #E5 
delay(310)  
tone(3,740,310) #Gb/F#5 
delay(310)  
tone(3,784,414) #G5 
delay(414)  
tone(3,659,207) #E5 
delay(207)  
tone(3,784,207) #G5 
delay(207)  
tone(3,1175,207) #D6 
delay(207) 
tone(3,1109,310) #Db/C#6 
delay(310)  
tone(3,988,310) #B5 
delay(310)  
tone(3,1109,207) #Db/C#6 
delay(207)  
tone(3,880,828) #A5 
delay(828) 
tone(3,1046,310) #C6 
delay(310)  
tone(3,988,310) #B5 
delay(310)  
tone(3,880,414) #A5 
delay(414)  
tone(3,784,207) #G5 
delay(207) 
tone(3,880,207) #A5 
delay(207)  
tone(3,988,207) #B5 
delay(207)  
tone(3,880,310) #A5 
delay(310) 
tone(3,784,310) #G5 
delay(310) 
tone(3,880,207) #A5 
delay(207)  
tone(3,740,828) #Gb/F#5 
delay(828)   
tone(3,659,310) #E5 
delay(310)  
tone(3,740,310) #Gb/F#5 
delay(310)  
tone(3,784,414) #G5 
delay(414)  
tone(3,659,207) #E5 
delay(207)  
tone(3,784,207) #G5 
delay(207)  
tone(3,1175,207) #D6 
delay(207) 
tone(3,1109,310) #Db/C#6 
delay(310)  
tone(3,988,310) #B5 
delay(310)  
tone(3,1109,207) #Db/C#6 
delay(207)  
tone(3,1318,828) #E6
delay(828) 
tone(3,1046,310) #C6 
delay(310)  
tone(3,988,310) #B5 
delay(310)  
tone(3,880,414) #A5 
delay(414)  
tone(3,784,207) #G5 
delay(207) 
tone(3,880,207) #A5 
delay(207)  
tone(3,988,207) #B5 
delay(207)  
tone(3,880,310) #A5 
delay(310) 
tone(3,784,310) #G5 
delay(310) 
tone(3,880,207) #A5 
delay(207)  
tone(3,740,310) #Gb/F#5 
delay(310)  
tone(3,880,310) #A5 
delay(310) 
tone(3,1175,207) #D6 
delay(207) 

#Bridge Four

tone(3,1568,621) #G6 
delay(621) 
tone(3,1480,828) #Gb/F#6
delay(1035) 
tone(3,1318,621) #E6
delay(621) 
tone(3,1175,828) #D6 
delay(621) 
tone(3,1760,207) #A6
delay(207) 
tone(3,1760,207) #A6
delay(207) 
tone(3,1568,621) #G6 
delay(621) 
tone(3,1480,621) #Gb/F#6
delay(621) 
tone(3,1175,414) #D6 
delay(414) 
tone(3,1397,414) #F6
delay(414) 
tone(3,1318,414) #E6
delay(414) 
tone(3,1865,414) #Bb/A#6
delay(414) 
tone(3,1568,414) #G6 
delay(414) 

#Sixth Line

tone(3,698,310) #F5 
delay(310)  
tone(3,784,310) #G5 
delay(310)  
tone(3,831,414) #Ab/G#5 
delay(414)  
tone(3,698,207) #F5 
delay(207)  
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,1244,207) #Eb/D#6
delay(207) 
tone(3,1175,310) #D6 
delay(310) 
tone(3,1046,310) #C6 
delay(310)  
tone(3,1175,207) #D6 
delay(207) 
tone(3,932,828) #Bb/A#5 
delay(828)  
tone(3,1109,310) #Db/C#6 
delay(310)  
tone(3,1046,310) #C6 
delay(310)  
tone(3,932,414) #Bb/A#5 
delay(414) 
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,932,207) #Bb/A#5 
delay(207)  
tone(3,1046,207) #C6 
delay(207)  
tone(3,932,310) #Bb/A#5 
delay(310)  
tone(3,831,310) #Ab/G#5 
delay(310) 
tone(3,932,207) #Bb/A#5 
delay(207) 
tone(3,784,828) #G5 
delay(828)   
tone(3,698,310) #F5 
delay(310)  
tone(3,784,310) #G5 
delay(310)  
tone(3,831,414) #Ab/G#5 
delay(414)  
tone(3,698,207) #F5 
delay(207)  
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,1244,207) #Eb/D#6
delay(207) 
tone(3,1175,310) #D6 
delay(310) 
tone(3,1046,310) #C6 
delay(310)  
tone(3,1175,207) #D6 
delay(207) 
tone(3,1397,828) #F6
delay(828) 
tone(3,1109,310) #Db/C#6 
delay(310)  
tone(3,1046,310) #C6 
delay(310)  
tone(3,932,414) #Bb/A#5 
delay(414) 
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,932,207) #Bb/A#5 
delay(207)  
tone(3,1046,207) #C6 
delay(207)  
tone(3,932,310) #Bb/A#5 
delay(310)  
tone(3,831,310) #Ab/G#5 
delay(310) 
tone(3,932,207) #Bb/A#5 
delay(207) 
tone(3,784,828) #G5 
delay(828)   

#Seventh Line

tone(3,698,310) #F5 
delay(310)  
tone(3,784,310) #G5 
delay(310)  
tone(3,831,414) #Ab/G#5 
delay(414)  
tone(3,698,207) #F5 
delay(207)  
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,1244,207) #Eb/D#6
delay(207) 
tone(3,1175,310) #D6 
delay(310) 
tone(3,1046,310) #C6 
delay(310)  
tone(3,1175,207) #D6 
delay(207) 
tone(3,932,828) #Bb/A#5 
delay(828)  
tone(3,1109,310) #Db/C#6 
delay(310)  
tone(3,1046,310) #C6 
delay(310)  
tone(3,932,414) #Bb/A#5 
delay(414) 
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,932,207) #Bb/A#5 
delay(207)  
tone(3,1046,207) #C6 
delay(207)  
tone(3,932,310) #Bb/A#5 
delay(310)  
tone(3,831,310) #Ab/G#5 
delay(310) 
tone(3,932,207) #Bb/A#5 
delay(207) 
tone(3,784,828) #G5 
delay(828)   
tone(3,698,310) #F5 
delay(310)  
tone(3,784,310) #G5 
delay(310)  
tone(3,831,414) #Ab/G#5 
delay(414)  
tone(3,698,207) #F5 
delay(207)  
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,1244,207) #Eb/D#6
delay(207) 
tone(3,1175,310) #D6 
delay(310) 
tone(3,1046,310) #C6 
delay(310)  
tone(3,1175,207) #D6 
delay(207) 
tone(3,1397,828) #F6
delay(828) 

#Finale

tone(3,1109,310) #Db/C#6 
delay(310)  
tone(3,1046,310) #C6 
delay(310)  
tone(3,932,414) #Bb/A#5 
delay(414) 
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,932,207) #Bb/A#5 
delay(207)  
tone(3,1046,207) #C6 
delay(207)  
tone(3,932,310) #Bb/A#5 
delay(310)  
tone(3,831,310) #Ab/G#5 
delay(310) 
tone(3,932,207) #Bb/A#5 
delay(207)  
tone(3,784,310) #G5 
delay(310)  
tone(3,932,310) #Bb/A#5 
delay(310)  
tone(3,1244,207) #Eb/D#6
delay(207) 
tone(3,1397,1656) #F6
delay(1656) 
tone(3,466,310) #Bb/A#4 
delay(310)  
tone(3,415,310) #Ab/G#4 
delay(310)  
tone(3,466,207) #Bb/A#4 
delay(207)  
tone(3,392,310) #G4 
delay(310) 
tone(3,466,310) #Bb/A#4 
delay(310)  
tone(3,622,207) #Eb/D#5 
delay(207)  
tone(3,1109,310) #Db/C#6 
delay(310)  
tone(3,1046,310) #C6 
delay(310)  
tone(3,932,414) #Bb/A#5 
delay(414) 
tone(3,831,207) #Ab/G#5 
delay(207)  
tone(3,932,207) #Bb/A#5 
delay(207)  
tone(3,1046,207) #C6 
delay(207)  
tone(3,932,310) #Bb/A#5 
delay(310)  
tone(3,831,310) #Ab/G#5 
delay(310) 
tone(3,932,207) #Bb/A#5 
delay(207)  
tone(3,784,310) #G5 
delay(310)  
tone(3,932,360) #Bb/A#5 
delay(360)  
tone(3,1244,307) #Eb/D#6
delay(307) 
tone(3,1397,3312) #F6
delay(7500) 
