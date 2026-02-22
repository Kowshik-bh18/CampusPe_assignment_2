# bill splitter program
# this calculates restaurant bill sharing

try:
    total = float(input("total bill: "))
    people = int(input("number of people: "))
    tax = float(input("tax percentage: "))
    tip = float(input("tip percentage: "))

    tax_amt = total * tax / 100
    after_tax = total + tax_amt
    tip_amt = after_tax * tip / 100
    final = after_tax + tip_amt

    print("subtotal:", total)
    print("tax:", tax_amt)
    print("after tax:", after_tax)
    print("tip:", tip_amt)
    print("total:", final)
    print("per person:", final / people)

except:
    print("invalid input")
