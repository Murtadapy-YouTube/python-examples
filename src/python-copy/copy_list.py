import copy


"""
Changing on the original list won't
affect on the copies as Python always
creates new objects on the update
"""
x = [1, 2, 3]
y = x.copy()

print("value of x:", x)
print("value of y:", y)

x[0] = 10

print("value of x:", x)
print("value of y:", y)


"""
Changing on the original list will
affect on the copies as Python does
not update list memory referece on
appending
"""
x = [[1, 2], 2, 3]
y = x.copy()

print("value of x:", x)
print("value of y:", y)

x[0].append(3)

print("value of x:", x)
print("value of y:", y)


"""
copy.deepcopy() solves the previous
problem as it creates new objects in
the memory of recursively of the given list
"""
x = [[1, 2], 2, 3]
y = copy.deepcopy(x)

print("value of x:", x)
print("value of y:", y)

x[0].append(3)

print("value of x:", x)
print("value of y:", y)
