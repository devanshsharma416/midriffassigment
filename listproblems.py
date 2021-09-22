
# # Qns - 1 
# # Reverse the given list

# # list1 = [6, 2, 3, 4, 5, 1]
# # start = 0
# # end = len(list1) - 1

# # while start < end:
# #     list1[start], list1[end] = list1[end], list1[start]
# #     start = start + 1
# #     end = end - 1
# # print(list1)

# # # Method - 2
# # list1 = [6, 2, 3, 4, 5, 1]
# # list2 = []

# # for i in range(len(list1)-1, -1, -1):
# #     list2.append(list1[i])

# # print(list2)

# # Qns - 2 Find the minimum and maximum value element in the list

# # list1 = [6, 2, 3, 4, 5, 1]
# # max = list1[1]

# # for i in list1:
# #     if i > max:
# #         max = i
# # print("The maximum element is: ", max)

# # list1 = [6, 2, 3, 4, 5, 1]
# # min = list1[0]

# # for i in list1:
# #     if i < min:
# #         min = i
# # print("The minimum element is: ",min)

# # Qns - 3: Find the kth max and min element in array

# # def element(list1, n):
# #     list1.sort()
# #     print(list1)

# #     return list1[n-1]

# # list1 = [6, 2, 3, 4, 5, 1]
# # n = 2
# # print(element(list1, n))

# # Move all the negative elements to one side of the array
# # list1 = [6, -1, -8, 2, 3, -9, 1, -1]
# # j = 0
# # for i in range(0, len(list1)):
# #     if list1[i] < 0:
# #        list1[i], list1[j] = list1[j], list1[i]
# #        j = j + 1
# # print(list1)

# # Qns - 5 Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

# # list1= [0, 2, 1, 2, 0]
# # dict1 = {}

# # Qns - 6 Cyclically rotate an array by one
# # list1 = [1, 2, 3, 4, 5]
# # n = len(list1) - 1
# # x = list1[n]

# # for i in range(n, 0, -1):
# #     list1[i] = list1[i - 1]
# # list1[0] = x
# # print(list1)

# # Qns - 7 Find the factorial of the largest  number

# # num = int(input("Enter the number: "))
# # fact = 1
# # while(num>0):
# #     fact = fact * num
# #     num = num - 1
# # print(fact)

# # Qns - 8 Merge two sorted array without using extra space
# # arr1 = [10, 12]
# # arr2 = [5, 18, 20]
# # for i in range(len(arr1)-1):
# #     for j in range(len(arr2)- 1):
# #         if arr1[i]>arr2[j] and arr1[i] < arr2 [j+1]:
# #             arr2.insert(j+1, arr1[i])
# # print(arr2)

# # Qns - 9 Find the duplicate in array of N+1 integers
# # list1 = [1, 2, 3, 4, 2, 7, 8, 8, 3]

# # for i in range(len(list1)-1):
# #     for j in range(i+1, len(list1)):
# #         if list1[i] == list1[j]:
# #             print(list1[j])

# # list1 = [4, 2, -3, 1, 6]

# # for i in range(len(list1)-1):
# #     for j in range(i+1, len(list1)):
# #         if list1[i] + list1[j] == 0:
# #             print(list1[j])

# # Qns - 10 Minimize the maximum difference between heights

# # def getMinDiff(arr, n, k):
# #     arr.sort()
# #     ans = arr[n - 1] - arr[0]
# #     small = 0
# #     big = 0

# #     for i in range(1, n):
# #         small = min(arr[0] + k, arr[i] - k) # finding minimum tower height
# #         big = max(arr[i - 1] + k, arr[-1] - k) # finding maximum tower height

# #         ans = min(ans, big-small) # Checking whether we get smaller value as result
# #     return ans

# # arr = [1, 10, 14, 14, 14, 15]

# # k = 6

# # print(getMinDiff(arr, len(arr), k))

# # Qns - 11 Count inversion (An array how far to being sorted)
# # arr = [1, 20, 6, 4, 5]
# # count = 0

# # for i in range(len(arr)-1):
# #     for j in range(i+1, len(arr)):
# #         if arr[i] > arr[j]:
# #             count = count + 1

# # print(count)

# # Qns - 12 Best time to buy and Sell stock
# # prices = [7,1,5,3,6,4]

# # max = 0

# # for i in range(1, len(prices)):
# #     if prices[i] - prices[i - 1] > 0:
# #         max += (prices[i] - prices[i - 1])

# # print(max)

# # # Qns - 13 find all pairs on integer array whose sum is equal to given number
# # list1 = [1, 5, 7, 1]
# # num = 6
# # count = 0
# # for i in range(len(list1)-1):
# #     for j in range(i+1, len(list1)):
# #         if list1[i] + list1[j] == num:
# #             print(list1[i], list1[j])
# #             count+=1
# #             print(count)
# # Qns - 14 find common elements In 3 sorted arrays

# # list1 = [1, 5, 10, 20, 40, 80] 
# # list2 = [6, 7, 20, 80, 100] 
# # list3 = [3, 4, 15, 20, 30, 70, 80, 120] 

# # # for i in list1:
# # #     for j in list2:
# # #         for k in list3:
# # #             if i == j == k:
# # #                 print(i, end = ' ')

# # n1 = len(list1) 
# # n2 = len(list2) 
# # n3 = len(list3) 

# # i = 0
# # j = 0
# # k = 0

# # while(i<n1, j < n2, k < n3):
# #     if list1[i] == list2[j] and list2[j] == list3[k]:
# #         print(list1[i], end = ' ')
# #         i += 1
# #         k += 1
# #         j += 1
# #     elif list1[i] < list2[j]:
# #         i += 1
# #     elif list2[j] < list3[k]:
# #         j += 1
# #     else:
# #         k += 1

# # Qns - 9 find the largest sum contigous subarray

# # from sys import maxint
# # def Maxsubarray(list1, n):
# #     # max_so_far = 0
# #     max_so_far = -maxint-1
# #     max_ending_here = 0

# #     for i in range(n):
# #         max_so_far = max_so_far + list1[i]

# #         if max_so_far < 0:
# #             max_so_far = 0
        
# #         elif(max_so_far < max_ending_here):
# #             max_so_far = max_ending_here

# #     return max_so_far

# # list1 = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
# # n = len(list1)

# # print(Maxsubarray(list1, n))

# # Qns 29 - Median of sorted array

# # def median(list1):
# #     for i in range(len(list1)-1):
# #         for j in range(i+1, len(list1)):
# #             if list1[i]<list1[j]:
# #                 list1[i], list1[j] = list1[j], list1[i]

# #         median = len(list1)//2

# #     return list1[median]

# # list1 = [90, 100, 78, 89, 67]
# # print(median(list1))

# # Qns - 30

# # arr1 = [10, 12]
# # arr2 = [5, 18, 20]
# # arr3 = []
# # for i in range(len(arr1)-1):
# #     for j in range(len(arr2)):
# #         if arr1[i]<arr2[j]:
# #             arr3.append(arr1[i])
# #         else:
# #             arr3.append(arr2[j])
    

# # String Problem - 1 Reverse the string
# # s = ["h","e","l","l","o"]

# # u = []

# # for i in range(len(s)-1, -1, -1):
# #     u.append(s[i])
# # print(u)

# # Linked List Reversed Problem

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LL:
#     def __init__(self):
#         self.head = None

#     def display(self):
#         node = self.head
#         if node is None:
#             print("The list is empty")
#         else:
#             while node:
#                 print(node.data, ">>", end = '')
#                 node =  node.next
                
#     def reverse(self):
#         prev = None
#         current = self.head

#         while current:
#             next = current.next
#             current.next = None
#             prev = current
#             current = next
#             self.head = prev


# n = LL()
# n.head = Node(1)
# n2 = Node(2)
# n.head.next = n2
# n3 = Node(3)
# n2.next = n3
# n.reverse()
# n.display()

        
# class Solution:
# 	def isPalindrome(self, S):
# 		self.a = S[::-1]
# 		self.count = 0
# 		if self.a == S:
# 		    self.count += 1
# 		    return self.count
		
# 		return self.count

# s = Solution()
# S = input()
# print(s.isPalindrome(S))            
        
string1 = "geeksforgeeks"
count = 0
strin2 = ''


for i in string1:
    if i in string1:
        count += 1
        if count>1:
            print(i, count)



    
    
        

        
