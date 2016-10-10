list1 = [2, 4, 6, 1, 9]


for i in range(len(list1)):
    for j in range(i+1, len(list1)):
        print(str(list1[i]) + str(list1[j]))