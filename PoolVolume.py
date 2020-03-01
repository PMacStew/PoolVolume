import math as m


mm_cm = 10
cm_in = 2.54
in_ft = 12
ft_yd = 3
yd_m = 1.09361
m_km = 1000
cm_m = 100
yd_mi = 1760
km_mi = 1.60934
global great_conversion
global less_conversion
global conversion_value
global conversion_type1
global conversion_type2
global conversion_multiplier
global height
global width
global length


# This asks for the dimensions for a 3D shape
def dimension_questions():
    global height
    global length
    global width
    height = float(input("Insert height: "))
    width = float(input("Insert width: "))
    length = float(input("Insert length: "))


def american_conversions():
    global less_conversion
    global great_conversion
    if conversion_type1 == 3:
        great_conversion = in_ft
    elif conversion_type1 == 4:
        less_conversion = in_ft
        great_conversion = ft_yd
    elif conversion_type1 == 5:
        less_conversion = ft_yd
        great_conversion = yd_mi
    elif conversion_type1 == 8:
        less_conversion = yd_mi


# This sets conversion values for metric units
def metric_conversions():
    global great_conversion
    global less_conversion
    if conversion_type1 == 1:
        great_conversion = mm_cm
    elif conversion_type1 == 2:
        less_conversion = mm_cm
        great_conversion = cm_m
    elif conversion_type1 == 6:
        less_conversion = cm_m
        great_conversion = m_km
    elif conversion_type1 == 7:
        less_conversion = m_km


# This converts the value to the right unit
def conversion():
    global conversion_type1
    global conversion_type2
    global conversion_value
    if 1 <= conversion_type1 <= 8 and 1 <= conversion_type2 <= 8:
        if conversion_type1 == conversion_type2:
            print("You already have the right unit!")
        elif (conversion_type1 == 1 or conversion_type1 == 2 or conversion_type1 == 6 or conversion_type1 == 7) and (
                conversion_type2 == 1 or conversion_type2 == 2 or conversion_type2 == 6 or conversion_type2 == 7):
            while conversion_type1 > conversion_type2:
                metric_conversions()
                conversion_value = conversion_value * (less_conversion ** conversion_multiplier)
                conversion_type1 = conversion_type1 - 1
                if conversion_type1 == 5:
                    conversion_type1 = conversion_type1 - 3
            while conversion_type1 < conversion_type2:
                metric_conversions()
                conversion_value = conversion_value / (great_conversion ** conversion_multiplier)
                conversion_type1 = conversion_type1 + 1
                if conversion_type1 == 3:
                    conversion_type1 = conversion_type1 + 3
            if conversion_type1 == conversion_type2:
                print("Your converted value is: " + str(conversion_value))
        elif (conversion_type1 == 3 or conversion_type1 == 4 or conversion_type1 == 5 or conversion_type1 == 8) and (
                conversion_type2 == 3 or conversion_type2 == 4 or conversion_type2 == 5 or conversion_type2 == 8):
            while conversion_type1 > conversion_type2:
                american_conversions()
                conversion_value = conversion_value * (less_conversion ** conversion_multiplier)
                conversion_type1 = conversion_type1 - 1
                if conversion_type1 == 7:
                    conversion_type1 = conversion_type1 - 2
            while conversion_type1 < conversion_type2:
                american_conversions()
                conversion_value = conversion_value / (great_conversion ** conversion_multiplier)
                conversion_type1 = conversion_type1 + 1
                if conversion_type1 == 6:
                    conversion_type1 = conversion_type1 + 2
            if conversion_type1 == conversion_type2:
                print("Your converted value is: " + str(conversion_value))
        else:
            while conversion_type1 > conversion_type2:
                set_conversions()
                conversion_value = conversion_value * (less_conversion ** conversion_multiplier)
                conversion_type1 = conversion_type1 - 1
            while conversion_type1 < conversion_type2:
                set_conversions()
                conversion_value = conversion_value / (great_conversion ** conversion_multiplier)
                conversion_type1 = conversion_type1 + 1
            if conversion_type1 == conversion_type2:
                print("Your converted value is " + str(conversion_value))


# This assigns the conversion variable to the correct value
def set_conversions():
    global great_conversion
    global less_conversion
    if conversion_type1 == 1:
        great_conversion = mm_cm
    elif conversion_type1 == 2:
        less_conversion = mm_cm
        great_conversion = cm_in
    elif conversion_type1 == 3:
        less_conversion = cm_in
        great_conversion = in_ft
    elif conversion_type1 == 4:
        less_conversion = in_ft
        great_conversion = ft_yd
    elif conversion_type1 == 5:
        less_conversion = ft_yd
        great_conversion = yd_m
    elif conversion_type1 == 6:
        less_conversion = yd_m
        great_conversion = m_km
    elif conversion_type1 == 7:
        less_conversion = m_km
        great_conversion = km_mi
    elif conversion_type1 == 8:
        less_conversion = km_mi


# This asks for conversion units
def conversion_questions():
    global conversion_type1
    global conversion_type2
    global conversion_value
    conversion_value = float(input("What value will you be converting: "))
    print("If mm type 1")
    print("If cm type 2")
    print("If in type 3")
    print("If ft type 4")
    print("If yd type 5")
    print("If m type 6")
    print("If km type 7")
    print("If mi type 8")
    conversion_type1 = int(input("What is your starting unit: "))
    if conversion_type1 > 8 or conversion_type1 < 1:
        print("Suit yourself. No fun for you!")
    elif conversion_type1 <= 8 or conversion_type1 >= 1:
        conversion_type2 = int(input("What is your ending unit: "))
        if conversion_type1 > 8 or conversion_type1 < 1:
            print("Suit yourself. No fun for you!")


# This prints the results for 3D shapes
def results():
    print("Your volume is: " + str(volume))
    print("Your surface area is: " + str(surface_area))


# This is the start of the program
first_choice = int(input("If finding measurements press 1. If converting press 2: "))
if first_choice == 1:
    print("Do you want to find the volume and surface area or the area and perimeter of a shape?")
    print("If rectangular prism press 1.")
    print("If right triangular prism press 2.")
    print("If uneven triangular prism press 3.")
    print("If 2D circle press 4.")
    print("If 2D trapezoid press 5.")
    print("If rectangle or square press 6.")
    print("If sphere press 7.")
    print("If isoceles trapezoid press 8.")
    start = int(input("Enter answer here: "))
    # This finds the measurements for a rectangular prism
    if start == 1:
        dimension_questions()
        surface_area = ((height * width) * 2) + ((width * length) * 2) + ((height * length) * 2)
        volume = height * length * width
        results()
    # This finds measurements for a right triangular prism
    elif start == 2:
        dimension_questions()
        volume = (height * length * width) / 2
        hypotenuse = (length ** 2) + (height ** 2)
        hypotenuse_real = m.sqrt(hypotenuse)
        surface_area = (length * width) + (height * width) + (hypotenuse_real * width) + (height * length)
        results()
    # This finds measurements for an uneven triangular prism
    elif start == 3:
        dimension_questions()
        volume = (length * width * height) / 2
        side_length1 = float(input("Enter length of side of triangle: "))
        side_length2 = float(input("Enter other length of side of triangle: "))
        surface_area = (length * width) + (height * width) + (side_length1 * length) + (side_length2 * length)
        results()
    # This finds measurements for a circle
    elif start == 4:
        diameter = float(input("What is your diameter: "))
        surface_area = diameter * m.pi
        volume = ((diameter / 2) ** 2) * m.pi
        print("Your area is: " + str(volume))
        print("Your perimeter is: " + str(surface_area))
    # This finds measurements for a trapezoid
    elif start == 5:
        base1 = float(input("What is the base: "))
        base2 = float(input("What is your other base: "))
        height = float(input("What is your height: "))
        if base1 >= base2:
            base = base2
            base3 = (base1 - base2) / 2
        else:
            base = base1
            base3 = (base2 - base1) / 2
        volume = (base3 + base) * height
        print(str(volume))
    # This finds measurements for a rectangle or square
    elif start == 6:
        height = float(input("What is your length: "))
        length = float(input("What is your height: "))
        volume = height * length
        surface_area = (height + length) * 2
        print("Your area is: " + str(volume))
        print("Your surface area is: " + str(surface_area))
    # This finds the measurements of a sphere
    elif start == 7:
        diameter = float(input("What is your diameter: "))
        volume = (4 / 3) * m.pi * ((diameter / 2) ** 3)
        surface_area = 4 * m.pi * ((diameter / 2) ** 2)
        print("Your volume is: " + str(volume))
        print("Your surface area is: " + str(surface_area))
    elif start == 8:
        base1 = float(input("What is your base: "))
        base2 = float(input("What is your other base: "))
        height = float(input("What is your height: "))
        if base1 >= base2:
            base = base2
            base3 = (base1 - base2) / 2
        else:
            base = base1
            base3 = (base2 - base1) / 2
        volume = (base3 + base) * height
        hypotenuse = (height ** 2) + (base3 ** 2)
        hypotenuse_real = m.sqrt(hypotenuse)
        surface_area = (hypotenuse_real * 2) + (base1 + base2)
        print("Your area is: " + str(volume))
        print("Your perimeter is: " + str(surface_area))

    else:
        print("Suit yourself. No fun for you!")
elif first_choice == 2:
    conversion_scale = int(input("If 1D object press 1. If 2D object press 2. If 3D object press 3: "))
    # This finds the units for a 3D object
    if conversion_scale == 1:
        conversion_questions()
        conversion_multiplier = 1
        conversion()
    # This finds the units for a 2D object
    elif conversion_scale == 2:
        conversion_questions()
        conversion_multiplier = 2
        conversion()
    # This finds the units for a 1D object
    elif conversion_scale == 3:
        conversion_questions()
        conversion_multiplier = 3
        conversion()
    else:
        print("Suit yourself. No fun for you!")
else:
    print("Suit yourself. No fun for you!")
