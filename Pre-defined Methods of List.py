n1=[1, 3, 7, 5, 0, 2, 9, 5, 4, 6, 8]
print(n1)
# Append Method: list_name.append(Value_to_add) -> Add the element at the end of the list
n1.append(3)
print("After appending 3: ",n1)   # [1, 3, 7, 5, 0, 2, 9, 5, 4, 6, 8, 3]
# Sorting Method: list_name.sort() -> Sort the list in ascending by default and for descending order we have to use list_name.sort(reverse=True)
n1.sort()
print("The list after sorting in ascending order: ",n1)   # [0, 1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9]
n1.sort(reverse=True)
print("The list after sorting in descending order: ",n1)  # [9, 8, 7, 6, 5, 5, 4, 3, 3, 2, 1, 0]
# Reverse Method: list_name.reverse() -> Use to reverse the list
n1.reverse
print("The list after reversing: ",n1)
# Insert Method: list_name.insert(index, value) -> Use to add element at the specified index
n1.insert(2, 588)
print("After the adding of 588 at 2nd index: ",n1) # [9, 8, 588, 7, 6, 5, 5, 4, 3, 3, 2, 1, 0]
# Remove Method: list_name.remove(Value) -> Use to remove the value from the list
n1.remove(588)
print("After the removing of 588: ",n1) # [9, 8, 7, 6, 5, 5, 4, 3, 3, 2, 1, 0]
# Pop Method: list_name.pop(index_number) -> Use to pop the element on the specified index
n1.pop(5)
print("After the pop of element on the 5th index: ",n1) # [9, 8, 7, 6, 5, 4, 3, 3, 2, 1, 0]