dic = {}
for i in range(3):
    key = input("Enter the key : ")
    value = input("Enter the value : ")
    dic.update({key: value})

dic = dict(dic.items())
print(dic)
