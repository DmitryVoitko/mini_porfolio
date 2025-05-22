word = 'Привет'

first_part = word[:len(word) // 2]
print(first_part[::-1])

second_part = word[len(word) // 2:]
print(second_part[::-1])

print(first_part[::-1] + second_part[::-1] )