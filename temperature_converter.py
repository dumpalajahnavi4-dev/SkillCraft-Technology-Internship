temperature = float(input("Enter temperature: "))

print("Select Current Unit")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

current = input("Enter choice (1/2/3): ")

print("\nConvert To")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

target = input("Enter choice (1/2/3): ")

if current == target:
    result = temperature

elif current == "1" and target == "2":
    result = (temperature * 9/5) + 32

elif current == "2" and target == "1":
    result = (temperature - 32) * 5/9

elif current == "1" and target == "3":
    result = temperature + 273.15

elif current == "3" and target == "1":
    result = temperature - 273.15

elif current == "2" and target == "3":
    result = (temperature - 32) * 5/9 + 273.15

elif current == "3" and target == "2":
    result = (temperature - 273.15) * 9/5 + 32

else:
    print("Invalid Input")
    exit()

units = {"1":"Celsius","2":"Fahrenheit","3":"Kelvin"}

print(f"\n{temperature} {units[current]} = {round(result,2)} {units[target]}")