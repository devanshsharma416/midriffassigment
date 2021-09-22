# def insertionSort(list1):
#     n = len(list1)
#     for i in range(1, n):
#         k = list1[i]
#         j = i-1
#         while j>=0 and list1[j]>k:
#             list1[j+1] = list1[j]
#             j -= 1
#         else:
#             list1[j + 1] = k
#     return list1






# list1 = []
# n =  int(input("Enter the numbers of element:"))
# for i in range(n):
#     ele = int(input())
#     list1.append(ele)

# print(insertionSort(list1))

def insertion_sort(list1):
    for i in range(1, len(list1)):
        # Loop from the second element of the array until
        # the last element
        k = list1[i]
        j = i - 1
        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        while j>=0 and list1[j]>k:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            list1[j+1] = list1[j]
            j = j - 1
        else:
        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
            list1[j+1] = k
    return list1

list1 = [8, 4, 5, 1, 3]
print(insertion_sort(list1))