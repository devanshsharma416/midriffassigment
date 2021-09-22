


# # # import os
# # # import shutil 
    
# # # # Source path 
# # # source = "D:\Python Project\test_file.py"
    
# # # # Destination path 
# # # destination = 'D:\Python Project\javatpoint'
    
# # # # Copy the content of 
# # # # source to destination 
# # # dest = shutil.copy(source, destination) 
    
# # # # Print path of newly  
# # # # created file 
# # # print("Destination path:", dest)

# # # import os
# # # import shutil


# # # # hello.txt file will be copied 
# # # source = r'D:\Python Project\javatpoint\hello.txt'


# # # # In the newly created foloder
# # # destination = r'D:\Python Project\NewFile\hi.txt'
# # # # Storing the new path of hello.txt file

# # # dest1 = shutil.copyfile(source, destination)


# # # # Print the new path
# # # print(dest1)

# # # importing os module
# # import os

# # # importing shutil module
# # import shutil


# # # It is source path
# # src = r'D:\Python Project\javatpoint'

# # # It is destination path
# # dest = r'D:\Python Project\NewFolder'

# # # Copy the content of
# # # source to destination
# # dest1 = shutil.copytree(src, dest)


# # # Now we print path of newly
# # # created file
# # print("Destination path:", dest1)

# # Python program to demonstrate
# # shutil.rmtree()

# # import shutil
# # import os

# # # location
# # location_dir = r"D:\Python Project\NewFile"

# # # directory
# # directory = r"D:\Python Project\javatpoint"

# # # path
# # path1 = os.path.join(location_dir, directory)

# # # removing directory
# # shutil.rmtree(path1)

# # importing shutil module
# import shutil
	
# # search the file
# cmd = 'python'
	
# # Using shutil.which() method
# locating = shutil.which(cmd)
	
# # Print result
# print(locating)

# Python program to explain shutil.copy() method
	
# # importing shutil module
# import shutil

# # It is a source path
# source = r"D:\Python Project\NewFolder"

# # It is a destination path
# destination = r"D:\Python Project\NewFolder"

# try:
# 	shutil.copy(source, destination)
# 	print("File copied successfully.")

# # If the given source and path are same
# except shutil.SameFileError:
# 	print("Source and destination represents the same file.")

# # If there is no permission to write
# except PermissionError:
# 	print("Permission denied.")

# # For other errors
# except:
# 	print("Error occurred while copying file.")




# sentence = "This is a cat"
# sen = sentence.split(' ')
# for i in sen:
#     rev_str = i[::-1]
#     print(rev_str, end = ' ')

Number = int(input("Enter range: "))  
 
for num in range(1,Number + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num, end = ' ')




