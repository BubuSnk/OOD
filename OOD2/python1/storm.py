print(" *** Wind classification ***")
st = float(input("Enter wind speed (km/h) : "))

if st > 0 and st < 52:
    print("Wind classification is Breeze.") 
elif st >= 52 and st < 56:
    print("Wind classification is Depression.") 
elif st >= 56 and st < 102:
    print("Wind classification is Tropical Storm.") 
elif st >= 102 and st < 209:
    print("Wind classification is Typhoon.") 
elif st >= 209:
    print("Wind classification is Super Typhoon.") 