# Simple Exercise Of Function

'''Create a function named tripleprint  that takes a string as a parameter and prints that string 3 times in a row. So if I passed in the string hello  it would print hellohellohello

*Be sure to only create the function, don't call it. For example, don't write tripleprint("hello")  The exercise will do this for you.'''

word = str(input("Enter a string: "))

def tripleprint(word):
    return word*3

ans = tripleprint(word)
print(ans)
