dic = {1: int(input("1 : ")), 2: int(input("2 : ")), 3: int(input("3 : "))}
total = 0
for value in dic.values():
    total += value
print(f"Sum of all value : {total}")

# print(sum(dic.values()))
