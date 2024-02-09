@@ -0,0 +1,15 @@
# Given list
List1 = [1, 2, 3, 4, ["python", "java", "c++", [10, 20, 30]], 5, 6, 7, ["apple", "banana", "orange"]]

# Extracting the word "orange" and "Python"
word_orange = List1[-1][-1]
word_python = List1[4][0].capitalize()

# Repeating the list five times without using loops
Repeated_List = [List1] * 5

# Display the extracted words and the repeated list
print("Word 'orange':", word_orange)
print("Word 'Python':", word_python)
print("Repeated List:")
print("\n".join(map(str, Repeated_List)))