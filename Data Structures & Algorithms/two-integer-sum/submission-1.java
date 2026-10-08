class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>(); 
        for(int i=0; i<nums.length; i++){
            map.put(target-nums[i], i);
        }
        int[] sol = new int[2];
        int x=-1; int y=-1;
        for(int i=0; i<nums.length; i++){
            if(map.containsKey(nums[i])){
                x=i;
                y=map.get(nums[i]);
                if(x!=y){
                    break;
                }
            }
        }
        if(x>y){
            sol[0] = y;
            sol[1] = x;
        }
        else{
            sol[0] = x;
            sol[1] = y;
        }
        return sol;
    }
}
