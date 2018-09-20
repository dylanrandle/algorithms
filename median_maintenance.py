from heapq import heappop, heappush

def read_data():
    stream = []
    with open('data/median.txt') as f:
        data = f.readlines()
        for d in data:
            stream.append(int(d))
    return stream

def maintain_median(input_stream):
    left_heap = [] ## these values will be negated so that extract-min will get the maximum value (once negated again)
    right_heap = []
    medians = []
    medians.append(input_stream[0])
    # initialize both heaps by taking first two values
    if input_stream[0] > input_stream[1]:
        heappush(right_heap, input_stream[0])
        heappush(left_heap, -input_stream[1])
        medians.append(input_stream[1]) # median of two elements will be first element, aka smaller element
    else:
        heappush(right_heap, input_stream[1])
        heappush(left_heap, -input_stream[0])
        medians.append(input_stream[0])
    # iterate over remainder of stream
    for i, val in enumerate(input_stream[2:]):
        # determine which heap to place value in
        left_max = -left_heap[0]
        right_min = right_heap[0]
        if val < left_max:
            heappush(left_heap, -val)
        elif val > right_min:
            heappush(right_heap, val)
        else:
            ## place val in left_heap by convention
            heappush(left_heap, -val)
        ## balance heaps
        while abs(len(left_heap)-len(right_heap)) > 1:
            if len(left_heap) > len(right_heap):
                # pop from left heap and place in right
                heappush(right_heap, -heappop(left_heap))
            else:
                # pop from right and place in left
                heappush(left_heap, -heappop(right_heap))
        ## both heaps are balanced, new element was added, and therefore the median is now left_max or right_min
        if len(left_heap) == len(right_heap) or len(left_heap) > len(right_heap): 
            ## even number => left_max is the min, left_heap is bigger => left_max is the min
            medians.append(-left_heap[0])
        else:
            medians.append(right_heap[0])
    return medians

print('Answer is %d' % (sum(maintain_median(read_data()))%10000))
