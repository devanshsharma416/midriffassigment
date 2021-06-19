# import requests
# r1 = requests.get('https://my-json-server.typicode.com/typicode/demo/posts')
# r2 = requests.get('https://my-json-server.typicode.com/typicode/demo/comments')
# print(r1.status_code)

# dic = r1.json()
# dic1 = r2.json()
# list1 = []

# s = dic[0]
# s1 = dic[1]

# s2 = dic1[0]
# s3 = dic1[1]
# if s['id']==s2['id']:
#     s['body'] = "some comment"
#     list1.append(s)


# if s1['id'] == s3['id']:
#     s1['body'] = 'some comment'
#     list1.append(s1)
   

# print(list1)

import requests
for i in range(1,13):
    str1 = 'https://reqres.in/api/users?page'
    r = requests.get(str1,'=',i)
    s = r.json()
    print(s)



