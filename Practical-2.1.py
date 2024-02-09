lst = ['Python', 'Java', 'C++', 'JavaScript']

# Display the original list
print("Original list of programming languages:", lst)

# Append a new programming language
lst.append('Ruby')
print("List after appending 'Ruby':", lst)

# Extend the list with more programming languages
lst.extend(['Swift', 'Kotlin'])
print("List after extending with 'Swift' and 'Kotlin':", lst)

# Remove a programming language
lst.remove('Java')
print("List after removing 'Java':", lst)

# Reverse the list
lst.reverse()
print("List after reversing:", lst)

# Arrange the list in ascending order
lst_asc = sorted(lst)
print("List in ascending order:", lst_asc)

# Arrange the list in descending order
lst_desc = sorted(lst, reverse=True)
print("List in descending order:", lst_desc)