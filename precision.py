import math
num = 25.74356801

# using trunc() function
print("The value is:",math.trunc(num))
 
# using ceil() function
print ("The ceiling value is:",math.ceil(num)) 
 
# using floor() function
print ("The floor value is:", math.floor(num)) 

num = 25.73796211
 
# using "%" operator
print ('The value is: %.3f'%num) 
 
# using format() function
print ("The value is: {0:.3f}".format(num)) 
 
# using round() function
print ("The value is:",round(num,5))


