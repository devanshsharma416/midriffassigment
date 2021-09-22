

# # class Employee:
# #     def __init__(self, first_name, last_name):
# #         self.first_name = first_name
# #         self.last_name = last_name

# #     # Getter
# #     @property
# #     def fullname(self):
# #         return '{} {}'. format(self.first_name, self.last_name)

# #     # It allows us to use the function as the attributes
# #     @property
# #     def email(self):
# #         return '{}.{}@gmail.com'. format(self.first_name, self.last_name)
    
# #     @fullname.setter
# #     def fullname(self, name):
# #         first_name, last_name = name.split(' ')
# #         self.first_name = first_name
# #         self.last_name = last_name
    
# #     @fullname.deleter
# #     def fullname(self):
# #         print('Deleted ')
# #         self.first_name = None
# #         self.last_name = None

    
# # e1 = Employee('John', 'Snow')

# # e1.fullname = "Devansh Sharma"

# # print(e1.first_name)
# # print(e1.last_name)
# # print(e1.email)
# # print(e1.fullname)

# # del e1.fullname

# with open("text2.txt", 'r') as f:
#    dict1 = {}
#    max = 0
#    name = "hello"
# #    for i in f.readlines():
#    for i in f:
#         dict2 = {}
#         user, words= i.rstrip('\n').split(':') # split the list in user and words
#         wor =words.strip().split(' ')
#         for words in wor:
#             words = words.lower()
#             dict2[words]= dict2.get(words, 0) + 1
#         if len(dict2) > max:
#             max = len(dict2)
#             name = user
            
#         dict1[user] = dict2
 
#    print(dict1) 
#    print(name, 'is used', max, 'unique words')
#    print(user, words)

    
           

       
#     #    new_set = set(a)
#     #    print(new_set)
#     #    word_count = len(new_set)
#     #    print(word_count)

# # with open('text2.txt', 'r') as f:
# #     dict1 = {}
# #     max = 0
# #     name = "hello"
# #     for i in f.readlines():
# #         dict2 = {}
# #         user, words = i.rstrip('\n').split(':')
# #         words = words.strip().split(' ')
# #         for wor in words:
# #             wor = wor.lower()
# #             dict2[wor] = dict2.get(wor, 0) + 1
# #         if len(dict2)>max:
# #             max = len(dict2)
# #             name = user
# #         dict1[user] = dict2
# #     print(dict1)
# #     print(user, 'is used', max, 'words')



# # with open('text2.txt', 'r') as f:
# #     dict1 = {}
# #     max = 0
# #     name = " "
# #     for i in f.readlines():
# #         dict2 = {}
# #         user, words = i.strip('\n').split(':') # split the user and words 
# #         words = words.strip().split(' ')
# #         for wor in words:
# #             wor = wor.lower()
# #             dict2[wor] = dict2.get('wor', 0) + 1

# #         if len(dict2)>max:
# #             max = len(dict2)
# #             name = user

# #         dict1[user] = dict2
# #     print(dict1)
# #     print(name, 'is used', max)
 
  

with open("text2.txt", 'r') as f:
    dict1 = {}
    max = 0
    name = "Hello"
    for i in f.readlines():
        dict2 = {}
        user, words = i.strip('\n').split(":")
        print(user, words)
        words = words.strip().split()
        for wor in words:
            wor = wor.lower()
            dict2[wor] = dict2.get('wor', 0) + 1

        dict1[user] = dict2
        
        if len(dict2)>max:
            max = len(dict2)
            name = user
    print(name, 'is used', max)



# with open("text2.txt", 'r') as f:
#     dict1 = {}
#     max = 0
#     name = "hello"
#     for i in f.readlines():
#         user, words = i.strip('\n').split(':')
#         print(user, name)