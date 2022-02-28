
# no.1 Find all the numbers from 1 to 1000 that are divisible by 8

# list1 = [i for i in range(1, 1001) if i % 8 == 0]
# print(list1)

# no.2 Find all the numbers from 1 to 1000 that have a 6 in them

# list1 = [i for i in range(1, 1001) if "6" in str(i)]
# print(list1)

# no.3 
# string = "Practice Problems to Drill List Comprehension in Your Head."
# Count the number of spaces in a string (use string above)

# string = "Practice Problems to Drill List Comprehension in Your Head."
# count_str = len([i for i in string if i == " "])
# print(count_str)

# no.4 Remove all the vowels in a string (use string above)

# string = "Practice Problems to Drill List Comprehension in Your Head."
# remove_v = "".join([i for i in string if i not in ['a', 'e', 'i', 'o', 'u']])
# print(remove_v)

# no.5 Find all the words in a string that are less than 5 letters (use string above)

# string = "Practice Problems to Drill List Comprehension in Your Head."
# word = string.split(" ")
# count = [i for i in word if len(i) < 5]
# print(count)

# no.6 Use a dictionary comprehension to count the length of each word in a sentence (use string above)

string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split(" ")
dic = {word: len(word) for word in words}
print(dic)
