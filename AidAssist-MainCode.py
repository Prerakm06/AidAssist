import RPi.GPIO as GPIO
import drivers
import time


GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup([26,21],GPIO.IN)
GPIO.setup(4,GPIO.OUT)
display = drivers.Lcd()
display.lcd_clear()

one = 0
two = 0
counter = 0


i = 2

injuries = ["Head Injury", "Cut", "Burn",
            "Eye Injury", "Nosebleed","Fractures", "Splinter"]

instructions = {"Head Injury":["1.Control bleeding: Apply pressure with cloth",
                           "2.Clean wound: Use sterile gauze",
                           "3.Apply sterile dressing to cover",
                           "4.Apply cold compress to reduce swelling",
                           "5.Provide pain relief medication if needed",
                           "6.Monitor vital signs: breathing, pulse, consciousness",
                           "7.Seek medical help for severe symptoms",
                            "Finished"],
                
            "Cut":["1.Clean cut: Use antiseptic wipes to remove debris",
                           "2.Control bleeding: Apply pressure to the wound",
                           "3.Apply topical antibiotics to prevent infection",
                           "4.Apply sterile dressing to protect the wound",
                           "Finished"],
                
            "Burn":["1.Stop burn source,move away",
                           "2.Cool burn with water for 10-15 min",
                           "3.Cover burn with sterile dressing",
                           "4.Provide pain relief medication if needed",
                           "5.Seek medical help for severe burns",
                            "Finished"],
                
            "Eye Injury":["1.If injury affects vision, seek medical attention",
                           "2.If chemical in eye flush with water/ saline solution",
                           "3.Use sterile dressing/cloth to protect eye",
                            "Finished"],
                
            "Nosebleed":["1.Sit & lean fwd to avoid swallowing blood",
                           "2.Pinch nostrils for 10-15 mins",
                           "3.Apply ice to bridge of nose",
                           "4.Repeat pinching if bleeding persists",
                           "5.Seek medical attention for severe bleedings",
                            "Finished"],
                
            "Fractures":["1.Call for help: Dial emergency services immediately",
                           "2.Immobilize: Use splint to prevent further damage",
                           "3.Apply ice: Reduce swelling and pain with ice",
                           "4.Elevate: If possible, raise injured above heart",
                           "Finished"],
                
            "Splinter":["1.Wash affected area",
                           "2.Remove splinter: Use sterilized tweezers or needle",
                           "3.Apply antibiotic ointment",
                           "4.Cover with sterile dressing",
                            "Finished"]}
broke = False
while True:
    display.lcd_display_string("Please Select One:",1)
    display.lcd_display_string(injuries[i-2]+"<-- ", 2)
    display.lcd_display_string(injuries[i-1], 3)
    display.lcd_display_string(injuries[i], 4)

    if GPIO.input(26)==1 :
        display.lcd_clear()
        if i ==6:
            i = 0
        else:
            i = i+1
    if GPIO.input(21) ==1:
        choice = injuries[i-2]
        for q in instructions[choice]:
            line1 = ""
            line2 = ""
            line3 = ""
            display.lcd_clear()
            spaces = []
            counter = 0
            display.lcd_display_string(choice,1)
            string = q+" "
            if len(string)<=21:
                line1= string
                line2 = ""
                line3 = ""
            else:
                for characters in string:
                    if characters == " ":
                        spaces.append(counter)
                    counter = counter+1
                for l in range(0,len(spaces)-1):
                    if spaces[l+1]>20 and spaces[l]<=20:
                        one = spaces[l]+1
                        line1 = (string[0:one])
                        if one+20>=len(string)-1:
                            line2 = (string[one:-1])
                            line3 = ""
                    if spaces[l+1]>=one+20 and spaces[l]<one+20:
                        two = spaces[l]+1
                        line2=(string[one:two])
                        line3=(string[two:-1])

            line1 = line1.strip()
            line2 = line2.strip()
            line3 = line3.strip()
            display.lcd_display_string(line1, 2)
            display.lcd_display_string(line2, 3)
            display.lcd_display_string(line3, 4)
            while GPIO.input(21)==0:
                time.sleep(0.1)
                if GPIO.input(26) == 1:
                    line1 = ""
                    line2 = ""
                    line3 = ""
                    broke = True
                    break
            if broke == True:
                display.lcd_clear()
                broke = False
                break

            display.lcd_clear()

                
            
        
        
        
        
        


