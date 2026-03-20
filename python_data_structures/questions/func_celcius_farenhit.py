
def ctof(temp):
    return (round((9/5)*temp +32,5))

temp =float(input("enter temp in celcius: "))
print(f"temp in farenhit: {ctof(temp):0.5f}")

