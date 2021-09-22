# def isHappyNumber(num):  
#     rem = sum = 0;  
      
#     #Calculates the sum of squares of digits  
#     while(num > 0):  
#         rem = num%10;  
#         sum = sum + (rem*rem);  
#         num = num//10;  
#     return sum;  
      
# num = 82;  
# result = num;  
   
# while(result != 1 and result != 4):  
#     result = isHappyNumber(result);  
   
# #Happy number always ends with 1  
# if(result == 1):  
#     print(str(num) + " is a happy number");  
# #Unhappy number ends in a cycle of repeating numbers which contain 4  
# elif(result == 4):  
#     print(str(num) + " is not a happy number");


# Python3 program to count
# amicable pairs in an array

# # Calculate the sum
# # of proper divisors
# def sumOfDiv(x):
# 	sum = 1
# 	for i in range(2, x):
# 		if x % i == 0:
# 			sum += i
# 	return sum

# # Check if pair is amicable
# def CheckAmicable(a, b):
# 	if sumOfDiv(a) == b and sumOfDiv(b) == a:
# 		return True
# 	else:
# 		return False

# def countPairs(arr, n):
# 	count = 0
# 	for i in range(0, n):
# 		for j in range(i + 1, n):
# 			if CheckAmicable(arr[i], arr[j]):
# 				count = count + 1
# 	return count

# list1 = [220, 284, 1184,
# 		1210, 2, 5]
# n1 = len(list1)
# print(countPairs(list1, n1))

# list2 = [2620, 2924, 5020,
# 		5564, 6232, 6368]
# n2 = len(list2)
# print(countPairs(list2, n2))

# x=int(input("Enter the first number:"))
# y=int(input("Enter the second number"))
# sum_of_x=0
# sum_of_y=0
# for i in range(1,x):
#     if(x%i==0):
#         sum_of_x=sum_of_x+i
# for i in range(1,y):
#     if(y%i==0):
#         sum_of_y=sum_of_y+i
# if(sum_of_x==y and sum_of_y==x):
#     print("Given numbers are amicable numbers")
# else:
#     print("Given numbers are not amicable")

# x=int(input('Enter first number : '))
# y=int(input('Enter second number : '))
# sum1=0
# sum2=0
# for i in range(1,x):
#     if x%i==0:
#         sum1+=i
# for j in range(1,y):
#     if y%j==0:
#         sum2+=j
# if(sum1==y and sum2==x):
#     print('Given numbers are Amicable!')
# else:
#     print('Given numbers are not Amicable!')


