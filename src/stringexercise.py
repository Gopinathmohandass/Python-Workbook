import string


fruit = "banana"
m = fruit[0]
print(m)

print(list(enumerate(fruit)))


ix = 0
while ix < len(fruit):
    letter = fruit[ix]
    print(letter)
    ix += 1


for c in fruit:
    print(c)

prefix = "JKLMOPQ"
suffix = "ack"

for p in prefix:
    print(p + suffix)


str = "Hello World"
new_str = "J" + str[1:len(str)]
str = new_str
print(str)

def vowels_remover(str, vowels):
    """Remove the vowels from the input and print"""
    #vowels="aeiouAEIOU"
    final_str = ""
    for c in str:
        if c not in vowels:
            final_str += c
    return final_str

vowels="aeiouAEIOU"
print(vowels_remover("Hi, How are you", vowels))

def find(str, alpha, start):
    """Return the index of the string where the alpha is found. If not found return -1"""
    ix = start
    while ix < len(str):
        if str[ix] == alpha:
            return ix
        ix += 1
    return -1

print(find("Hello", "e", 1))
print(find("Hello", "x", 1))
print(find("banana", "a", 2))

def count(str, alpha):
    """Count thye number of times the alpha appears in the string"""
    counter = ix = 0
    while ix < len(str):
        if str[ix] == alpha:
            counter += 1
        ix += 1

    counter = 0
    for ix in str:
        if ix == alpha:
            counter += 1
    return counter

print(count("hello", "l"))
print(count("hello", "j"))


str = "banana"
print(str.find("a",0, 5))


#punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
print(vowels_remover("Hi! How are you?", string.punctuation))





