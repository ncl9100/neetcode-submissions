class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        arr = []
        for x, y in freq.items():
            arr.append([y, x])
        arr.sort()

        results = []
        while len(results) < k:
            results.append(arr.pop()[1])

        return results


        
        