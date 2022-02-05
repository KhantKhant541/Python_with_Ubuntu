
while True:
    char = input("Enter an alphabet : ")

    if char.isalpha():
        break

if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u') or (char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
    print("It is a vowel.")
else:
    print("It is a consonant.")
