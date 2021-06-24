# Creating interction function which takes two lists as an argument
def intersection(list1, list2):
    # Calculating the length of list1
    lenght_list1 = len(list1)
    # Calculating the length of list2
    lenght_list2 = len(list2)
    # empty list
    list3 = []
    # using if condition to compare smaller list to large list
    if lenght_list1> lenght_list2:
        for i in list2:
            for j in list1:
                if i==j:
                    list3.append(i)
                    break
    else:
         for i in list1:
            for j in list2:
                if i==j:
                    list3.append(i)
                    break
    return list3

list1 = [1, 2, 2, 1]
list2 = [2, 2]


print(intersection(list1, list2))

#Output
# [2, 2]