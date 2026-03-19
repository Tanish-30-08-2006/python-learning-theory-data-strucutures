# -----------------------------
# SET BASICS
# -----------------------------

demo = {1, 3, 4, 5}
print(demo)  
# Sets are UNORDERED → output order may change each run
#SETS CAN HAVE DIFFERENT DATATYPES IN IT 


# -----------------------------
# CLEARING A SET
# -----------------------------
demo.clear()  
# clear() removes ALL elements → set becomes empty

demo = {1, 2, 3, 4, 4, 3, 2, 1}
print(demo)
# Duplicate values automatically removed
# Output will be {1,2,3,4}


# -----------------------------
# UPDATE (UNION IN-PLACE)
# -----------------------------
demo.update([4, 5])
print("After update:", demo)
# update() adds elements from another iterable
# No duplicates added
# Modifies the same set


# -----------------------------
# DISCARD vs REMOVE
# -----------------------------
demo.discard(4)
# discard() removes element if present
# If not present → NO ERROR

# demo.remove(50)
# remove() removes only existing element
# If not present → KeyError

print("After discard:", demo)


# -----------------------------
# DIFFERENCE
# -----------------------------
p = {1, 2, 3, 6, 7}
q = {2, 3}

print(p.difference(q))  
# Elements in p but NOT in q → {1,6,7}

print(q.difference(p))  
# Elements in q but NOT in p → set()


# -----------------------------
# SUBSET & SUPERSET
# -----------------------------
print(p.issuperset(q))  
# True → p contains all elements of q

print(q.issubset(p))    
# True → q is inside p


# -----------------------------
# QUICK SUMMARY NOTES
# -----------------------------
# {} → Set
# Unordered
# No duplicates
# Unindexed (cannot use demo[0])
# Mutable container but elements unique
#
# Important Methods:
# add(x)               → add one element
# update(iterable)     → add multiple
# remove(x)            → error if x not found
# discard(x)           → no error
# clear()              → empty set
# pop()                → remove random element
# union()              → new set
# intersection()       → common elements
# difference()         → subtract sets
# issubset()           → check subset
# issuperset()         → check superset
# =====================================================
# PYTHON SET – FULL ORGANIZED EXAMPLE + SUMMARY
# =====================================================

# -----------------------------
# BASIC PROPERTIES OF SET
# -----------------------------
# Sets are unordered → Element order changes
# Sets are unindexed → Cannot use s[0]
# No duplicates allowed
# Mutable container (can add/remove items)
# Elements must be immutable (int, str, float, tuple)

s = set()      # Creating empty set

s.add(1)
s.add(8)
s.add(2)
s.add(3)

print(s)  
# Order will look random because sets are unordered

# lists []   tuples ()   sets {}

# -----------------------------
# LENGTH
# -----------------------------
print(f"Length: {len(s)}")


# -----------------------------
# REMOVE ELEMENT
# -----------------------------
s.remove(8)  
# remove(x) → error if x not found
print("After remove:", s)


# -----------------------------
# POP (RANDOM REMOVE)
# -----------------------------
print("Random popped:", s.pop())  
# pop() removes any random element
print("After pop:", s)


# -----------------------------
# CLEAR
# -----------------------------
temp_set = s
temp_set.clear()
print("After clear:", temp_set)  # set()


# -----------------------------
# UNION & INTERSECTION (NEW SET)
# -----------------------------
print("UNION AND INTERSECTION – NEW SETS")

s1 = {1, 2, 3}
s2 = {3, 4, 5, 6}

s3 = s1.union(s2)          # new set
s4 = s1.intersection(s2)   # new set

print("Union:", s3)
print("Intersection:", s4)


# -----------------------------
# UNION & INTERSECTION (MODIFY ORIGINAL)
# -----------------------------
print("UNION AND INTERSECTION – MODIFY ORIGINAL")

s1.update(s2)              # union in-place
print("s1 after update:", s1)

s1.intersection_update(s2) # intersection in-place
print("s1 after intersection_update:", s1)


# =====================================================
#                 SUMMARY SYNTAX NOTES
# =====================================================

# CREATION
# s = {1,2,3}
# s = set()          → empty set
# {}                 → dictionary, not set

# ADDING
# s.add(x)           → add one element
# s.update(iterable) → add many elements

# REMOVING
# s.remove(x)        → error if not found
# s.discard(x)       → no error
# s.pop()            → remove random
# s.clear()          → empty set

# LENGTH
# len(s)

# UNION
# s.union(t)         → new set
# s | t
# s.update(t)        → modify s
# s |= t

# INTERSECTION
# s.intersection(t)  → new set
# s & t
# s.intersection_update(t) → modify s
# s &= t

# DIFFERENCE
# s.difference(t)
# s - t

# SYMMETRIC DIFFERENCE
# s.symmetric_difference(t)
# s ^ t

# CHECKING
# s.issubset(t)
# s.issuperset(t)
# x in s
# x not in s

# LOOP
# for item in s:
#     print(item)

# FROZEN SET
# fs = frozenset([1,2,3])  → immutable set

# =====================================================
# QUICK MEMORY MAP
# Create → {} / set()
# Add → add(), update()
# Remove → remove(), discard(), pop(), clear()
# Ops → |  &  -  ^
# Check → issubset(), issuperset(), in
# Loop → for x in set
# Special → frozenset()
# =====================================================
