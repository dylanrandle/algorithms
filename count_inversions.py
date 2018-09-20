# divide and conquer examples

def sort_and_count_inversions(A, n):
    # takes list A of interegers length n
    # returns sorted A and the count of the number of inversions
    # inversion is defined as: (i,j) with i<j such that A[i] > A[j].
    if n == 1:
        # base case
        return A, 0 
    else:
        half = n//2
        first_half = A[:half]
        second_half = A[half:]
        B, x = sort_and_count_inversions(first_half, len(first_half)) # split the input into first half, and make recursive call
        C, y = sort_and_count_inversions(second_half, len(second_half)) # "" second half ""
        if isinstance(B, int):
            B = [B]
        if isinstance(C, int):
            C = [C]
        D, z = merge_and_count_inversions(B, C, n) # implement merge subroutine, but count number of inversions in O(n)
        return D, x+y+z

def merge_and_count_inversions(B, C, n):
    # takes two sorted arrays B and C, and merges them while counting number of inversions
    if len(B) == 0 or len(C) == 0:
        raise Exception('Somehow B or C was empty list.')

    if len(B) == 1 and len(C) == 1:
        if B[0] > C[0]:
            return [C[0], B[0]], 1
        else:
            return [B[0], C[0]], 0
    else:
        i = 0 # counter for B
        j = 0 # counter for C
        D = []
        inversions = 0
        for _ in range(n):
            if i < len(B) and j < len(C):
                if B[i] > C[j]:
                    D.append(C[j])
                    inversions += len(B) - i # increment inversions by number of elements remaining in B
                    j += 1
                else:
                    D.append(B[i])
                    i += 1
            else:
                # one of the arrays is done
                if i == len(B):
                    # dump rest of C into D
                    D.extend(C[j:])
                    break
                else:
                    # dump rest of B into D
                    D.extend(B[i:])
                    break
        return D, inversions

with open('data/integer_array.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

D, inversions = sort_and_count_inversions(content, len(content))
print(inversions)
    
