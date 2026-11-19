# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s <= 0 :
            return pairs
        
        mid = (s + e) // 2
        self.mergeSortHelper(pairs, s, mid)
        self.mergeSortHelper(pairs, mid+1, e)
        self.merge(pairs, s, mid, e)

        return pairs
    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> None:
        
        L = arr[s: m+1]
        R = arr[m+1: e+1]

        i = 0 # left
        j = 0 # right
        k = s #arr

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
        
        while i < len(L):
            arr[k] = L[i]
            k+=1
            i+=1
        while j < len(R):
            arr[k] = R[j]
            k+=1
            j+=1

