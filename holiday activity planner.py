# Custom Ride Builder

# File : ride_builder.py

# Lesson: SPCM2L1 — Nested Conditional Statements (Jr)

print("====================================")

print(" Welcome to holiday activity planner! ")

print("====================================")

print()

print("Step 1: Pick your vehicle")

print(" 1 - Mountain")

print(" 2 - Beach")

print(" 3 - country")

print()

choice = int(input("Enter 1 or 2: "))

print()

if choice == 1:
    print("step 2 pick your mountain type")
    print(" 1 - Himalayas")
    print(" 2 - Mount everest")
    print()

    mountain_type = int(input("enter 1 OR 2 :"))
    print()

    if mountain_type == 1:
        print("you picked   :  Himalayas")
        print("height       :  8,849 meter")
        print("best in      :  Climbing")
    else:
        print("you picked   :  Mount everest")
        print("top speed    :  29,032 ft")
        print("best in      :  Climbing")

elif choice == 2:
    print("step 2 pick your beach-type")
    print(" 1 - Butterfly beach")
    print(" 2 - Bondi beach (Sydney)")
    print()

    beach_type = int(input("enter 1 OR 2 :"))
    print()

    if beach_type == 1:
        print("you picked   :  Butterfly beach")
        print("location     :  Goa")    
    else:
        print("you picked   :  Bondi beach")
        print("location     :  sydney")

elif choice == 3:
    print("step 2 pick your country")
    print(" 1 - India")
    print(" 2 - AMERICA")
    print()

    country = int(input("enter 1 OR 2 :"))
    print()

    if country == 1:
        print("you picked        :  India")
        print("capital of country:  delhi")    
    else:
        print("you picked        :  AMERICA")
        print("capital of country:  new yourk")
        
else :
    print("This type is not in a cateogary")
    print("See if there is any writing error")