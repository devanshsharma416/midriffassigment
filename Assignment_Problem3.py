
#  #Reverse the list of string 
# def reverseString(array_list):
#     # Creating Empty List
#     list1 = []
#     # Calculating a length of given string
#     length = len(array_list)
#     # using for loop to reverse iteration
#     for i in range((length)-1, -1, -1):
#         list1.append(array_list[i])
#     return list1

# array_list = ["h", "e", "l", "l", "o"]
# print("The Given list:", array_list)
# print("The Reverse list:",reverseString(array_list))



# list1 = [1, 2, 3, 4, 5, 4, 4, 3, 1 ]
# list2 = []
# # list1 = set(list1)
# # p = len(list1)
# # print(p)
# count = 0
# for i in list
# print(count)

# list1 = [4, 4, 4, 3, 3, 3, 4, 3, 4, 3, 8]
# k = len(list1)
# for i in range(k-2):
#     if list1[i] == list1[i+1] and list1[i + 1] == list1[i+2]:
#         print(list1[i])

# Python program to print all
# the possible combinations

def comb(L):
	
	for i in range(3):
		for j in range(3):
			for k in range(3):
				
				# check if the indexes are not
				# same
				if (i!=j and j!=k and i!=k or i == j, i == k, j == k):
					print(L[i], L[j], L[k])
					
# Driver Code
comb([1, 2, 3])
