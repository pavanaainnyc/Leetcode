arr = list(map(int, input().split()))
flag = True
for i in range(len(arr)):
    if arr[i] != i:
        flag = False
        break
print("Perfect Array" if flag else "Not Perfect")