def twowaysort(arr, n):
    for i in range(0, n):
        if (arr[i] & 1):
            arr[i] *= -1
    arr.sort()
    for i in range(0, n):
        if (arr[i] & 1):
            arr[i] *= -1


n = int(input("Enter length of array: "))
a = []
for i in range(n):
    b = int(input("Enter element: "))
    a.append(b)
twowaysort(a, n)
print("Sorted: ")
for i in range(0, n):
    print(a[i], end = " ")

# Code by shreyansh sharma