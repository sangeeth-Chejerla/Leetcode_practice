import collections
"""
def find_duplicates(arr):
    count = collections.Counter(' '.join(map(str, arr)).split())
    duplicates = {int(k): v for k, v in count.items() if  v > 1}
    #ignore v if you want  only key.
    return duplicates
res = find_duplicates([1, 2, 1])
print(res)"""

# Output: {1: 2}

"""
def find_duplicates_2(arr):
    res = []
    for i in arr:
        if arr[abs(i)-1] < 0:
            res.append(abs(i))
        else:
            arr[abs(i)-1]*= -1

    return res

result = find_duplicates_2([1, 2, 3,3,2,7,3,2,1])
print(result)
"""


def find_duplicates_3(arr):
    values = collections.Counter(arr)
    list1 = []

    for k,v in values.items():
        if v > 1:
            list1.append(k)
    return list1

result2 = find_duplicates_3([1, 2, 3,3,2,7,3,2,1])
print(result2)
      