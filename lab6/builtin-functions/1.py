# Variant - 1
def multipleNum(l):
    result = 1
    for i in l:
        result *= i
    return result


n = input("Введи список чисел: ")

list1 = [int(num) for num in n.split()]

print(multipleNum(list1))
# Variant - 2

numbers = input("Vedy chesla: ").split()
product = 1
for number in numbers:
    product *= int(number)
print(product)
