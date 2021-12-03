"""
This program is written to implement binary search algo to search a target in a sorted list with time O(logn) and space O(1) complexity.
"""



def binary_search(lst1, target):
    start = 0
    end = len(lst1)
    while start <= end:
        mid = start + ( end - start ) // 2
        if lst1[mid] < target:
            start = mid + 1
        elif lst1[mid] > target:
            end = mid - 1
        else:
            return mid

if __name__ == "__main__":
    lst2 = [1, 2, 3, 4, 5, 6]
    tgt = 6
    idx = binary_search(lst2, tgt)
    print(idx)
