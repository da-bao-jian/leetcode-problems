def threeNumberSum(array, targetSum):
    # Write your code here.
    res = []
    array.sort()
    for i in range(len(array)): 
        right = len(array)-1
        left = i+1
        while left < right: 
            if  array[i]+array[left]+array[right] == targetSum: 
                res.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif array[i]+array[left]+array[right] < targetSum: 
                left += 1
            else:
                right -= 1
    return res
