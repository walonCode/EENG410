
multi_arr = [[1,2,3], [4,5,6]]
print(multi_arr[1][1])

arr = [23,56,7,78,899,9,0,2,4,5,6]

n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[i]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print(arr)           