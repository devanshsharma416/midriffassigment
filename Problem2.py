import requests
page_no = 1
number_of_users = 0
while True:
    url = "https://reqres.in/api/users?page="+str(page_no)
    number_of_users = number_of_users + len(requests.get(url).json())
    if not len(requests.get(url).json()['data']):
        break
    page_no = page_no + 1
print(number_of_users)