'''
2. If-Else with Multiple Conditions
Write a program to check if a given temperature is:
Cold if below 15°C
Warm if between 15°C and 25°C
Hot if above 25°C
'''

def checkTemperature(temp):
    if temp < 15:
        print("Cold")
    elif 15 <= temp <= 25:
        print("Warm")
    else:
        print("Hot")


temperature = float(input("Enter the temperature in °C: "))
checkTemperature(temperature)
