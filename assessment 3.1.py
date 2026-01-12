s = input("Enter a string:")
print(f"Length of string is {len(s)}")

#2> convert a sentence to lower case
sentence = "skytus pvt Ltd"
print(sentence.lower())

#3> Replace space with underscore in a string
print(sentence.replace(" ","_"))

#4> Extract the first and last character of the string
str1 = "skytus"
print(str1[0], str1[-1])

#5> Reverse a string using slicing
print(str1[::-1])

#6> count how many time a letter appers in a string
letter = input("Enter a word: ")
print(str1.count(letter))

#7> check if word is present in sentence
word = input("Enter a word:")
if word in sentence:
    print("word found in sentence")
else:
    print("not found") 
    
#8> take name and age and print using f-string format
name = "Taksh"
age = 21 
print(f"name is {name} and age is {age}")

#9> remove extra space from the 
text = "   Hello World   "
result = text.strip()
print(result)

#10> Join a list of words into a single string
words = ["name = taksh", "is", "age = 21"]
result = "-".join(words)
print(result)
   
# 11. Create a list of ur 5 favourite movies
movies = ["Phir Hera Pheri","Moonfall","KGF","Badla","Drishyam"]

# 12. Add a new movie
movies.append("3 idiot")
print(movies)

# 13. Remove the first movie
movies.pop(0)
print(movies)

# 14. Sort numbers in ascending order
numbers = [45, 12, 78, 34, 23]
numbers.sort()
print("Sorted numbers:", numbers)

# 15. Reverse a list
numbers.reverse()
print("Reversed list:", numbers)

# 16. Find the largest number in a list
print("Largest number:", max(numbers))

# 17. Merge two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("Merged list:", merged_list)

# 18. Access last element without using index number
print("Last element:", merged_list[-1])

# 19. Create a nested list and access an inner element
nested_list = [[10, 20], [30, 40], [50, 60]]
print("Inner element:", nested_list[1][1])  # 40

# 20. Count how many times an element appears
count_list = [1, 2, 3, 2, 4, 2, 5]
print("Count of 3:", count_list.count(2))   