
string1 = "p1=Khant Pyae Phyo,p2=Arkar Min,p3=Nang Yin Lao Hsaing,p4=Hnin Ei Shwe Yee"

list1 = []

for item in string1.split(","):
    temp = item.split("=")
    list1.append(temp)

dic = dict(list1)
for key, value in dic.items():
    print(f"{key} : {value}")
