import requests
r1 = requests.get('https://my-json-server.typicode.com/typicode/demo/posts')
r2 = requests.get('https://my-json-server.typicode.com/typicode/demo/comments')
print(r1.status_code)

dic = r1.json()
dic1 = r2.json()
list1 = []

post1 = dic[0]
post2 = dic[1]

comment1 = dic1[0]
comment2 = dic1[1]
if post1['id']== comment1['id']:
    post1['body'] = "some comment"
    list1.append(post1)


if post2['id'] == comment2['id']:
    post2['body'] = 'some comment'
    list1.append(post2)
   

print(list1)




