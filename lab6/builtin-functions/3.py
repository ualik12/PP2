def palindrom(text):
    text1 = text[::-1]
    if text == text1:
        print('palindrom')
    else:
        print('not a palindrom')

text = str(input())
palindrom(text)