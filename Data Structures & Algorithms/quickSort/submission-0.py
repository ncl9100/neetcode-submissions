# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs

    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> None:
        if e-s <=0:
            return 
        
        pivot = e
        left = s

        for i in range(s, e):
            if arr[i].key < arr[pivot].key:
                # swap
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left+=1
            
        # swap left with pivot
        temp = arr[left]
        arr[left] = arr[pivot]
        arr[pivot] = temp

        #run quick sort on left and right partitions

        self.quickSortHelper(arr, s, left-1)
        self.quickSortHelper(arr, left+1, e)

        
        