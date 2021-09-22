# def fizz_buzz(n):
#     if n%5 == 0  and n%3 == 0:
#         return "fizzbuzz"
#     elif n%5 == 0:
#         return "Buzz"
#     elif n%3 == 0:
#         return "fizz"
#     print(n)

# n = int(input("Enter the number"))
# print(fizz_buzz(n))

def string(input):
    rev = input[::-1]
    str = ""
    for i in rev:
        if i == 'a':
            rev = rev.replace(i, '1')
        elif i == 'e':
            rev = rev.replace(i, '0')
        elif i == 'i':
            rev = rev.replace(i, '2')
        elif i == 'o':
            rev = rev.replace(i, '4')
        elif i == 'u':
            rev = rev.replace(i, '5')
        else:
            rev

    print(rev + 'cae')
        
input = "banana"
string(input)

        


       




# a = int(input("Enter the number:"))
# fizz_buzz(a)

# # input = "apple"

# str_rev = input[::-1]

# for i in range(len(str_rev)):
#     if str_rev[i] == 'a':
#         pass
#     if str_rev[i] == 'e':
#         pass
#     if str_rev[i] == 'i':
#         pass
#     if str_rev[i] == 'o':
#         pass
#     if str_rev[i] == 'u':
#         pass

# print(str_rev)
    
# def square_area_differnce(num):

#     n1 = int(input())
#     n2 = int(input())

#     if n1<n2:
#         n1, n2 = n2, n1
#         return (2 * n1 * n1) - (2*n2*n2)
#     else:
#         return (2 * n1 * n1) - (2*n2*n2)




# num = int(input("enter the number"))
# square_area_differnce(num)