# age calculator program
# this creates approximate age details

from datetime import datetime

try:
    birth_year = int(input("enter birth year: "))
    current_year = datetime.now().year
    age = current_year - birth_year

    print("age:", age)
    print("months:", age * 12)
    print("days:", age * 365)
    print("hours:", age * 365 * 24)
    print("minutes:", age * 365 * 24 * 60)
    print("years until 100:", 100 - age)

except:
    print("invalid input")
