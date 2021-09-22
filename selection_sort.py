# list1 = [8, 7, 5, 6, 0, 7]
# min_value = list1[0]
# for i in range(1,len(list1)):
#     if min_value<list1[i]:
#         min_value = list1[i]
# print(min_value)

def selection_sort(list1):
    n = len(list1)
    for i in range(n):
        min_pos = i

    for j in range(i+1, n):
        if list1[j] < list1[min_pos]:
            min_pos = j
        list1[i], list1[min_pos] = list1[min_pos], list1[i]
    return list1

list1 = [10, 20, 5, 6, 4, 7]
print(selection_sort(list1))






    
