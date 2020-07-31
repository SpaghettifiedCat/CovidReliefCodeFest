alpha = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f', 7 : 'g', 8 : 'h', 9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o', 16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't', 21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y', 26 : 'z'}
string = "map"
string = string.replace('.', ' ')
print(string)
string = string.split()
print(string)
numbers = []
for word in string:
    number = []
    for letter in word:
        number.append(ord(letter) - 96)
    numbers.append(number)
print(numbers)
new = ""
for meow in numbers:
    word = ""
    for number in meow:
        word += alpha[(number + 2) % 26]
    new += word
    new += ' '
print(new)
    