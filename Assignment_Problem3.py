
 #Reverse the list of string 
def reverseString(array_list):
    # Creating Empty List
    list1 = []
    # Calculating a length of given string
    length = len(array_list)
    # using for loop to reverse iteration
    for i in range((length)-1, -1, -1):
        list1.append(array_list[i])
    return list1

array_list = ["h", "e", "l", "l", "o"]
print("The Given list:", array_list)
print("The Reverse list:",reverseString(array_list))


