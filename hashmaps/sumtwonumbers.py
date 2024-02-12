def twosums(arr, target):
    dictNums = dict()
    for i in range (len(arr)):
        numComplement = target - int(arr[i])
        if numComplement in dictNums.keys():
            return [i, dictNums[numComplement]]
        else:
            dictNums[arr[i]] = i
    return None


arr = [4, 67, 5, 23, 1 , 89, 43, 2, 78, 13, 14, 17, 16, 6]
result = twosums(arr, 45)
print(result)
for a in result:
    print(arr[a])