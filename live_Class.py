n1 = (10, 20, 30, 40, 50)
n1_list = list(n1)
n1_list[0], n1_list[-1] = n1_list[-1], n1_list[0]
n1 = tuple(n1_list)
print("The swapped tuple is ", n1)