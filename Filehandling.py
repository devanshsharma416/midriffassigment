# import os
# with open("Untitled-2.txt", 'r', encoding = 'utf-8') as f:
#     s = 5
#     new = f.read(s)
#     print(new, end = '')
#     while len(new) > 0:
#         print(f.read())
#         new = f.read(s)

# with open("Untitled-2.txt", 'r') as rf:
#     list1 = []
#     num = rf.readlines()
#     a = len(num) - 1
#     print(a)

# with open("text2.txt", 'r') as f:
#    line_number = 4
#    currentline = 1
#    for i in f:
#        if currentline == line_number:
#            print(i)
#            break
#        currentline = currentline + 1

f = open("text3.txt", 'wb')
a = f.write(b"devansh")
f.close()
       
        
    