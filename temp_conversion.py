
def convert_100_to_celsius():
    #Convert a temperature of 100 degrees fahrenheit to celsius
    x = 100
    celsius_100 = (x - 32) * 5/9
    print(celsius_100)
    print('float')
# i know it is a float because it is a decimal. 

     # Save this to a variable called celsius_100, and use print() to print out the value
    #  convert_100_to_celsius = celsius_100
     #first subtract 32, then multiply by 5/9
        #convert_100_to_celsius(100 - 32 * 5/9)
    # Is the resulting temperature you get an integer or float?
    #float
    # Print 'float' if it is a float or 'int' if it is an int
    # How do you know? Write a comment below your code explaining how you know which it is

convert_100_to_celsius()

def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
        y = 0
        celsius_0 = (y - 32) * 5/9
        print(celsius_0)

    # Save this to a variable called celsius_0, and use print() to print out the value

convert_0_to_celsius()

def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
       print((34.2 - 32) * 5/9)

#     # Do this one all in one print statement without saving any variables
    
convert_34_2_to_celsius()


# Now, can you convert back?
# yes 


def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    celsius = (5 * 9/5) + 32
    print(celsius)

convert_5_to_fahrenheit()

def hotter_temp():
#     # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
#     # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively

    #  celsius = (85.1 - 32) * 5/9
    #  fahrenheit = (30.2 - 32) * 5/9
    #  print(celsius)
    # print(fahrenheit)
    #30.2 celsius is hotter than  85.1 degrees fahrenheit because when convert fahrenheit you get 29.5 degrees celsius
     print('30.2 degrees celsius')

hotter_temp()


# Temperature conversions use the following formulas:
# Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32
# Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9