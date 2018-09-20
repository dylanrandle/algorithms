# Merge Sort Algorithm

def merge_sort(input_array):
    ''' takes input_array of length n and returns a sorted array 
        among friends, we are assuming only distinct values passed in
        and also among friends, we are assuming an even array length (n power of 2)
    '''
    n = len(input_array)
    left = input_array[:int(n/2)]
    right = input_array[int(n/2):]
    if (len(left) == 1 or len(left) == 0) and (len(right) == 1 or len(right) == 0):
        # merge and return
        if left and right:
            if left[0] > right[0]:
                return [left[0], right[0]]
            else:
                return [right[0], left[0]]
        elif left:
            return [left[0]]
        else:
            return [right[0]]
    else:
        # recursive calls
        sorted_arr = []
        left = merge_sort(left)
        right = merge_sort(right)
        l = 0
        r = 0
        for i in range(n):
            if l < len(left) and left[l] > right[l]:
                sorted_arr.append(left[l])
                l += 1
            else:
                sorted_arr.append(right[l])
                r += 1

merge_sort([1, 4, 2, 9, 5, 6])