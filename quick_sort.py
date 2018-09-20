import numpy as np

class QuickSort():
    def __init__(self):
        self.comparisons = 0

    def partition(self, A, l, r, pivot='first'):
        # takes an unsorted array A with start index l and final index r and 
        # returns a partitioned version, and the index of the pivot
        # print('calling partition on %s with l=%s and r=%s' % (A[l:r+1], l, r))
        
        self.comparisons += r-l

        ## CHOOSING PIVOT
        if pivot=='first':
            p = A[l]
        elif pivot=='last':
            p = A[r]
            # swap the first and last element
            A[l], A[r] = A[r], A[l] 
        elif pivot=='median':
            # compute median of first, last and middle (round down for even-length array) elements
            middle_index = ((r-l)//2)+l
            three_comps = [A[l], A[middle_index], A[r]]
            median = int(np.median(three_comps))
            if median == A[l]:
                p = A[l]
            elif median == A[middle_index]:
                p = A[middle_index]
                # swap the middle elem with first
                A[l], A[middle_index] = A[middle_index], A[l]
            else:
                p = A[r]
                # swap the first and last elems
                A[l], A[r] = A[r], A[l] 
        else:
            raise NotImplementedError('Invalid pivot selection. Supported types are: first, last, median')
        
        i = l+1
        for j in range(l+1, r+1):
            if A[j] < p:
                A[i], A[j] = A[j], A[i]
                i += 1
        A[l], A[i-1] = A[i-1], A[l]
        return A, i-1

    def sort(self, A, l, r):
        # print('Calling quick_sort on %s' %A)
        if r-l == 0: return A
        A, pivot_idx = self.partition(A, l, r, pivot='median')
        # we partitioned => increment comparisons:
        if pivot_idx - 1 - l >= 0:
            self.sort(A, l, pivot_idx-1)
        if r - pivot_idx - 1 >= 0:
            self.sort(A, pivot_idx+1, r)
        return A

    def get_comparisons(self):
        return self.comparisons

with open('data/quick_sort.txt') as f:
    content = f.readlines()
A = [int(x.strip()) for x in content]

''' 
test cases
first n elements of QuickSort.txt: first last median
10: 25 31 21
100: 620 573 502
1000: 11175 10957 9735

answers:
first pivot @ 10000: 162085
last pivot @ 10000: 164123
median pivot @ 10000: 138382
'''
quick_sort = QuickSort()
print('A = %s' % A)
input()
print(quick_sort.sort(A, 0, len(A)-1))
print('good algorithm!')
print('num comparisons: %d' % (quick_sort.get_comparisons()))
