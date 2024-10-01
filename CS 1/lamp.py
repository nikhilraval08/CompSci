print ("Lamp doesn't work.")
lampplug = input ("Lamp plugged in?")
if lampplug == ("no"):
    print("Plug in lamp")

elif lampplug == ("yes"):
    bulbout = input ("Bulb is burned out?")
    if bulbout == ("yes"):
        print("Replace bulb")
    elif bulbout == ("no"):
        print("Repair lamp")
        
