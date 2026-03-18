#IMP QUES  S={} THEN type(s) = dictionary


#=====================================================
# PYTHON DICTIONARY – FULL ORGANIZED EXAMPLE + SUMMARY
# =====================================================

# -----------------------------
# BASIC PROPERTIES OF DICTIONARY
# -----------------------------
# Mutable → values can be changed
# Unordered → order not guaranteed (Python 3.7+ keeps insertion order but conceptually unordered)
# Keys must be UNIQUE
# Keys must be immutable (int, str, tuple allowed)
# Values can be ANY datatype
# Syntax → { key : value }

# -----------------------------
# CREATING A DICTIONARY
# -----------------------------
my_dict = {
    "key": "value",
    "person1": 100,
    "person2": 200,
    "list": [1, 2, 4],
    "tupleindict": (3, 4, 6),
    0: "tanish"   # integer key allowed
}

# -----------------------------
# ACCESSING VALUES
# -----------------------------
print(my_dict["key"])          # value
print(my_dict["person1"])      # 100
print(my_dict["tupleindict"])  # (3,4,6)
print(my_dict["list"])         # [1,2,4]
print(my_dict[0])              # tanish

# Safer access using get()
print(my_dict.get("person2"))  # 200
print(my_dict.get("unknown"))  # None (no error)


# -----------------------------
# MODIFYING VALUES
# -----------------------------
my_dict["person1"] = 999
print("Modified person1:", my_dict["person1"])


# -----------------------------
# ADDING NEW KEY–VALUE
# -----------------------------
my_dict["newkey"] = 555
print("After adding new key:", my_dict)


# -----------------------------
# REMOVING ITEMS
# -----------------------------
my_dict.pop("newkey")       # removes specific key
# my_dict.pop("wrong")      # KeyError if not found

del my_dict["person2"]      # delete key
# del my_dict["wrong"]      # KeyError

# popitem() removes last inserted pair
removed = my_dict.popitem()
print("Popitem removed:", removed)

# clear() empties dictionary
temp = {"a":1}
temp.clear()
print("After clear:", temp)  # {}


# -----------------------------
# ITERATION (LOOP)
# -----------------------------
marks = {
    "per1": 100,
    "per2": 200,
    "per3": 300,
    "per4": 400,
    "per5": 500,
    "per6": 600
}

print(marks.items())   # key-value pairs
print(marks.keys())    # only keys
print(marks.values())  # only values

# Loop through keys
for k in marks:
    print(k, marks[k])

# Loop through key-value
for k, v in marks.items():
    print(k, v)


# -----------------------------
# UPDATE DICTIONARY
# -----------------------------
marks.update({"per1": 900})   # modifies existing
marks.update({"per7": 700})   # adds new
print("After update:", marks)


# -----------------------------
# MEMBERSHIP TEST
# -----------------------------
print("per1" in marks)   # True
print(100 in marks)      # False (checks keys only)


# -----------------------------
# NESTED DICTIONARY
# -----------------------------
students = {
    "s1": {"math": 90, "eng": 80},
    "s2": {"math": 70, "eng": 60}
}
print(students["s1"]["math"])


# =====================================================
#                 SUMMARY SYNTAX NOTES
# =====================================================

# CREATION
# d = { "a":1, "b":2 }
# d = dict()

# ACCESS
# d["key"]
# d.get("key")

# ADD / MODIFY
# d["key"] = value
# d.update({"k":v})

# REMOVE
# d.pop("key")
# del d["key"]
# d.popitem()
# d.clear()

# VIEW METHODS
# d.keys()
# d.values()
# d.items()

# LOOP
# for k in d:
# for k,v in d.items():

# CHECK
# "key" in d

# NESTED
# d["outer"]["inner"]

# =====================================================
# QUICK MEMORY MAP
# Create → {}
# Access → d[key] / get()
# Add/Modify → d[key] = val / update()
# Remove → pop(), del, popitem(), clear()
# View → keys(), values(), items()
# Loop → for k,v in d.items()
# Special → Nested dictionaries
# =====================================================
