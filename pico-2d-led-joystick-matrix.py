from machine import Pin
import time
# pins
pin1=Pin(5,Pin.OUT)
pin2=Pin(21,Pin.OUT)
pin3=Pin(26,Pin.OUT)
pin4=Pin(18,Pin.OUT)
pin5=Pin(19,Pin.OUT)
pin6=Pin(15,Pin.OUT)
pin7=Pin(4,Pin.OUT)
pin8=Pin(20,Pin.OUT)
pin9=Pin(16,Pin.OUT)
leds=[
    [pin1,pin2,pin3],
    [pin4,pin5,pin6],
    [pin7,pin8,pin9]
]

#voltage bits windows 
low=20000
high=43650

#axis pins
x=machine.ADC(28)
y=machine.ADC(27)

i=0
j=0

while True:
    #voltage bit declaration 
    x_axis=x.read_u16()
    y_axis=y.read_u16()
    
    #led 0 command 
    for row in leds:
        for pin in row:
            pin.value(0)
   
    #Left-Right movement command
    if x_axis>high:
        i+=1
        if i>2:  
            i=0      
    elif x_axis<low:
        i-=1
        if i<0:
            i=2       

    #up down movement command
    if y_axis>high:
        j+=1
        if j>2:
            j=0
    elif y_axis<low:
        j-=1
        if j<0:
            j=2
            
    leds[j][i].value(1) # led on accroding to the array
    
    print("x-axis value:", x_axis)
    print("y-axis value:", y_axis)
    time.sleep(.2)