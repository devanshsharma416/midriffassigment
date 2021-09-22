
# import requests
# req = requests.get('http://www.javatpoint.com/')
 
# print(req.encoding) # returns 'utf-8'
# print(req.status_code) # returns 200
# print(req.elapsed) # returns datetime.timedelta(0, 1, 666890)
# print(req.url) # returns 'https://edureka.co/'
 
# print(req.history) 
 
# print(req.headers['Content-Type'])

# import requests

# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
#     headers={'Accept': 'application/vnd.github.v3.text-match+json'},
# )


# json_result = response.json()
# repo = json_result['items'][0]
# print(f'Text matches: {repo["text_matches"]}')

# import requests
# json_data = {'username':'mathew','password':'1234'}
# r = requests.post('https://httpbin.org/post',data = json_data)

# print(r.json())

# import requests
# json_data = {'username':'mathew','password':'1234'}
# r = requests.post('https://httpbin.org/post',data = json_data)
# r_dictionary= r.json()
# print(r_dictionary['form'])

# num = int(input("Enter a number: "))  
  
# if num > 1:  
#    for i in range(2,num):  
#        if (num % i) == 0:  
#            print(num,"is not a prime number")  
#            print(i,"times",num//i,"is",num)  
#            break  
#    else:  
#        print(num,"is a prime number")  
         
# else:  
# #    print(num,"is not a prime number") 

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_sort_two_lists(left, right)

def merge_sort_two_lists(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)

    i = j = 0

    while i<=len_a and j<=len_b:
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    
    while i <len_a:
        sorted_list.append(a[i])  
        i+=1

      
    while j <len_b:
        sorted_list.append(a[j])
        j+=1

    return sorted_list


arr = [10, 3, 9, 54, 78, 23, 54]

print(merge_sort(arr))




    





