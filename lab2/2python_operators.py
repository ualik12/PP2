#Python Arithmetic Operators:
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 % 5)
print(10 ** 5)
print(10 // 5)
#=================================================================================================================
#Python Assignment Operators:
x = 5
x += 3
x -= 3
x *= 3
x /= 3
x %= 3
x //= 3
x **= 3
x &= 3
x |= 3
x ^= 3
x >>= 3
x <<= 3
#=================================================================================================================
#Python Comparison Operators:
5 == 5
5 != 4
5 > 4
3 < 4
5 >= 3
2 <= 2
#=================================================================================================================
#Python Logical Operators:
# and
# or
# not
#Python Identity Operators:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
#=================================================================================================================
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
#=================================================================================================================
#Python Membership Operators:
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list
#=================================================================================================================
x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list
#=================================================================================================================
#Python Bitwise Operators:
x & y
x | y
x ^ y
~x
x << 2
x >> 2