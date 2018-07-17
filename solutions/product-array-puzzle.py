def bruteforce(arr):
    l = len(arr)
    prod = []
    for i in range(l):
        product = 1
        for j in range(l):
            if i != j:
                product *= arr[j]
        prod.append(product)
    return prod

def usingDivision(arr):
    product = 1
    for number in arr:
        product *= number

    prod = [product//x for x in arr]
    return prod

def withoutdivision(arr):
    l = len(arr)
    left = [1 for _ in range(l)]
    right = [1 for _ in range(l)]
    prod = [1 for _ in range(l)]

    for i in range(1,l):
        left[i] = arr[i-1] * left[i-1]

    for i in range(l-2, -1, -1):
        right[i] = arr[i+1] * right[i+1]

    for i in range(l):
        prod[i] = left[i] * right[i]

    return prod

if __name__ == "__main__":
    arr = [int(x) for x in input().strip().split()]
    print(bruteforce(arr))
    print(usingDivision(arr))
    print(withoutdivision(arr))