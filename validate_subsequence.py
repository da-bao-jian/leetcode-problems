def isValidSubsequence(array, sequence):
    # Write your code here.
    order = {}
    res = []
    decoy = []
    for i in range(len(array)):
        order[array[i]]=i
    for j in sequence:
        if j in order:
            res.append(order[j])
            order[j] -=1
        else:
            return False
    print(res)
    decoy = res[:]
    decoy.sort()
    if res == decoy:
        return True
    else: 
        return False