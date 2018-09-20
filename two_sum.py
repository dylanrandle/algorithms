## two-sum problem from Coursera Algorithms specialization

def load_data():
    with open('downloads/2sum.txt') as f:
        data = f.readlines()
    return list(map(int, data))

data = load_data()

def two_sum(input_list, lower_bound, upper_bound):
    """
    Compute the number of target values t in the interval [lower_bound, upper_bound]
    such that there are distinct numbers x,y in input_list that satisfy:
    x + y = t
    """
    # initialize the main hash-table
    hash_map = {}
    
    # build the hash-table for the t interval
    t_list = list(range(lower_bound, upper_bound+1))
    t_map = {}
    for t in t_list:
        t_map[t] = False

    iter_num = 0
    for x in input_list:
        iter_num += 1
        print('Iter num %d' %iter_num)
        if x not in hash_map:
            hash_map[x] = True

        ## check if y = t - x in hash_map
        for t in t_list:
            if t-x == x: # dont allow duplicates 
                continue
            if t-x in hash_map:
                ## record this t as satisfying the condition
                t_map[t] = True

    count = 0
    for t_bool in list(t_map.values()):
        if t_bool:
            count += 1
    return count

print(two_sum(data, -10000, 10000))
