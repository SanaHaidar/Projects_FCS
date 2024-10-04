users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]
emptylist = []

print("Dave" in users)
print("Dave" in emptylist)

print('')

print(data[0])
print(users[-1])
print(data[-2])

print('')

print(users.index('Sara'))
print(users[0:2])
print(users[1:])
print(users[:3])
print(users[-3:-1])

print('')

print(len(data))
print('')

users.append('Elsa')
print(users)
print('')

users += ["Jason"]
print(users)
print('')

users.extend(['Robert', 'Jimmy'])
print(users)
print('')

# users.extend(data)
# print(users)
# print('')

users.insert(0, "bob")
print(users)
print('')

users[2:2] = ['Eddie', "Alex"]
print(users)
print('')

users[1:3] = ["Robert", "JPJ"]
print(users)
print('')

users.remove('bob')
print(users)
print('')

print(users.pop())  # return the last value
print(users)  # here the last value is delete
print('')

del users[0]
print(users)
print('')

# del data
data.clear()  # empties the list but the list still exsist
print(data)  # gives an error after del data since even though data is defined at the begining of the code it is now been deleted due to the command of the line above
print('')

users[1:2] = ['dave']
users.sort()
print(users)
print('')

# since dave was sorted at the end since it was not in capital this method allows 'dave' to be inserted at the begining and sort alphabatically
users.sort(key=str.lower)
# make sure you have the same type of data when sorting it hence str
print(users)
print('')


nums = [4, 42, 78, 2, 5]
nums.reverse()
print(nums)
print('')

# nums.sort(reverse=True)
# print(nums)
# print('')


# this global method does not modifiy the original list like the one before
print(sorted(nums, reverse=True))
print(nums)


# ways to copy list without being modified
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, 'Neil', True])
print(mylist)


# Tuples
mytuple = tuple(("Dave", 42, True))
anothertuple = (1, 4, 2, 8, 2, 2)
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

print('')
newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)
print(type(newlist))
print(type(newtuple))

print('')
print('')
print('')
# unpacking tuples
(one, two, *hey) = anothertuple
print(anothertuple)
print(one)
print(two)
print(hey)


print(anothertuple.count(8))
