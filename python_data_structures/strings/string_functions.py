#ALL STRING FUNCTIONS CREATE A NEW STRING AND ORIGINAL STRING REMAINS SAME..
# STRINGS ARE IMMUTABLE
name='tanish sanghavi'

print(len(name))
print(name.startswith('ta'))
print(name.endswith('sh'))
print(name.endswith('Ta'))
print(name.capitalize())

index=name.find("ang")
print(index)

c =name.count("a")
print(c)

name="bottle bottle cap"
print(name.replace("cap","opener"))
print(name.replace("bottle","opener"))
print(name.replace("bottle","opener").replace("opener","cap"))


