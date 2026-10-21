from machine import Pin
import time
# give the pico some time to boot up
time.sleep(0.1)


# creating a dictionary to hold the buttons and the respective led + the state
#button as the dict keys
#value is a dict containing the leds + button state (True or False) for pressed or not

buttons_data = {Pin(10, Pin.IN, Pin.PULL_DOWN) : {"Led": Pin("LED", Pin.OUT) , "Pressed": False},
                  Pin(11, Pin.IN, Pin.PULL_DOWN) : {"Led": Pin(16, Pin.OUT) , "Pressed": False},
                  Pin(12, Pin.IN, Pin.PULL_DOWN) : {"Led": Pin(17, Pin.OUT) , "Pressed": False},
                  Pin(13, Pin.IN, Pin.PULL_DOWN) : {"Led": Pin(20, Pin.OUT) , "Pressed": False},
                  Pin(22, Pin.IN, Pin.PULL_DOWN) : {"Led": Pin(18, Pin.OUT) , "Pressed": False}}

#making sure to start with the leds off
for data in buttons_data.values():
    data["Led"].value(0)

while True :

    #looping through the buttons:
    for button, data in buttons_data.items():


        if button.value() == 1 and not data["Pressed"]:  #the button is pressed 
            time.sleep_ms(50) # wait some time to avoid the rebond 

            if button.value() == 1:#checking if the button still pressed after 50 milliseconds 
                data["Pressed"] = True # save the current state of the button as pressed 

        elif button.value() == 0 and data["Pressed"]: #if the state of the button is True which means the button was or is pressed  
            time.sleep_ms(50) #wait for the user to release the button

            if button.value() == 0: # checking if the button was released 
                data["Led"].toggle() # change the led to on if it s off and off if it's on 
                data["Pressed"] = False #reset the state of the button








    


    """# checking which button is pressed and turning the led associated to it 
        for  button, light in buttons_lights.items():
            #check if the button is pressed then it changes it state to true 
            if button.value() == 1:
                light[1] = True
            #if the button is still pressed wait for 50 millisecond and then check
            elif light[1] == True:
                time.sleep_ms(50)
                if button.value() == 0:
                    light[0].toggle()
                    light[1]= False
        time.sleep_ms(10)"""
    


            
        
    
        
                   
    
    
   
  
        
        
                

                

"""if sw1.value() == 1:
          led.on()
      else:
          led.off()
  
  
      if sw2.value() == 1:
          led1.on()
      else:
          led1.off()
  
      if sw3.value() == 1:
          led2.on()
      else:
          led2.off()
  
      if sw4.value() == 1:
          led3.on()
      else:
          led3.off()
  
      if sw5.value() == 1:
          led4.on()
      else:
          led4.off()"""      
    