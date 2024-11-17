# Write a python function which converts inches to cms.

def inches_to_cms(inches):
    cm = inches*2.54
    return cm

inches = int(input("Enter number of inches: "))

cm = inches_to_cms(inches)

print(f"{inches} inches is equal to {cm} cm")