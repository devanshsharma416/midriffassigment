# str1 = "Geeksforgeeks"
# s = iter(str1)
# while True:
#     try:
#         item = next(s)
#         print(item)
#     except StopIteration:
#         break

class Test:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 5
        return self

    def __next__(self):
        x = self.x

        if x> self.limit:
            raise StopIteration
    
        else:
            self.x = x + 1
        return x

for i in Test(15):
    print(i)