class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            if nums[i] in map:
                result = [map.get(nums[i]), i]
                return result

            map[target-nums[i]] = i
        return [];
        