def twoNumberSum(array, targetSum):
    result = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                result.append(array[i])
                result.append(array[j])
    return result 
