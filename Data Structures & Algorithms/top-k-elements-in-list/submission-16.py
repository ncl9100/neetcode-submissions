class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dict
            # key = unique value from input array, value = frequency 
        #create a bucket array of size of len(nums)
        #use a loop
            # iterate through items in dict
            # bucket[freq] = key
        #iterate through bucket array
            #stop at k
        
        dict = {}
        for i in range(0, len(nums)):
            if nums[i] in dict:
                dict[nums[i]] +=1
            else:
                dict[nums[i]] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in dict.items():
            buckets[value].append(key)
        
        result = []
        count = 0
        for i in range(len(buckets)-1, 0, -1):
            if buckets[i] != []:
                for x in buckets[i]:
                    result.append(x)
                    count+=1 
                    if count ==k:
                        return result       
        return result



        