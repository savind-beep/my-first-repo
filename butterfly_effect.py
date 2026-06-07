HUM=int(input("Enter the humidity: "))
TEMP=int(input("Enter the temperature: "))
WSP=int(input("Enter the wind speed: "))
if HUM>80:
    if TEMP>30:
        if WSP>40:
            print("Severe storm warning .")
        else:
            print("heavy rain expected.")
    else:
        print("cloudy weather .")
else:
    if TEMP>35: 
        print("heat wave alert.") 
    else:   
         print("Normal weather expected.")      

