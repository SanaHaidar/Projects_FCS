# Dictionaries values that are in key value pairs
band = {
    "vocals": "Plant",
    "guitar": "Page",
}
band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))
print('')
print('')
print('')

# Access items
print(band["vocals"])
print(band.get("vocals"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify if key exist
print("guitar" in band)
print("banana" in band)

# change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

print('')
print('')
print('')

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "bonham"
print(band)

# pop item removes the last item added , return its value and turn the rest into tuples
print(band.popitem())  # tuple
print(band)
print('')
print('')
print('')
# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)
band2.clear()
print(band2)
del band2

# # copy dictionnaries
# # not a copy but a reference (refering to the same place in memory/ adding removing to band2 will alternate band as well)
# band2 = band
# print("bad copy!")
# print(band2)
# print(band)
# band2['drums'] = "dave"
# print(band)

# copy method
band2 = band.copy()
band2["drums"] = "Dave"
print(band)
print(band2)


# or use the dict() construtor function
band3 = dict(band)
print("Good copy!")
print(band3)
print('')
print('')
print('')
# nested  dictionaries this means that the value for a key pair can be another dictionary

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])
print('')
print('')
print('')

# Sets

nums = {
    1, 2, 3, 4
}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))
print('')
print('')
print('')

# No duplicated allowed
nums = {1, 2, 2, 3}
print(nums)
print('')
print('')
print('')

# True is a dupe of 1 and False is a dupe of 0.
nums = {1, True, 2, False, 3, 4, 0}
print(nums)
print('')
print('')
print('')
# check if a value in a set
print(2 in nums)
print('')
print('')
print('')

# but you cannot refer to an element in index position or a key

# Add a new element to a set
nums.add(8)
print(nums)
print('')
print('')
print('')
# Add elements from a set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)
print('')
print('')
print('')


# You can use update with lists, tuples and dictionaries too


# Mege two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}
mynewset = one.union(two)
print(mynewset)
print('')
print('')
print('')
# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)


# Keep everything except the duplicate
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
