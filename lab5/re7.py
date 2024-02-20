import re


snake = "snake_case_rara_uwu_ni!"
snake1 = "_" + snake
capital = snake1.upper()
camel = ""
i = 0
while i !=len(snake1):
    if snake1[i] == '_':
        camel = camel + capital[i+1]
        i = i +2
    else:
        camel = camel + snake1[i]
        i += 1
print(camel)