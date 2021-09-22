def sort(list1):
    # for traversal the loop
    for i in range(len(list1)-1, 0, -1):
        # for swapping the loop
        for j in range(i):
            if list1[j]> list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1
list1 = []
n = int(input("Enter the number of element: "))
for i in range(0, n):
    ele = int(input())
    list1.append(ele)

print(sort(list1))