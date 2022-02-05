
dic = {1: "Khant Pyae Phyo", 2: "Arkar Min", 3: "Nang Yin Lao Hsaing", 4: "Hnin Ei Shwe Yee"}

print("Sorting with value : ")
dic = sorted(dic.items(), key=lambda x: x[1])
dic = dict(dic)
print(dic)
