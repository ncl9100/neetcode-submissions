class Solution {
    public int longestConsecutive(int[] nums) {
        //idk
        //move array items to hashmap
            //HashMap<Element, Index>
        //setup max - track max length sequence
        //iterate through array
            //if reach start of sequence (nums-1) does not exist
            //start building sequence while loop
                //increment counter
                //check if nums[i+1] is in hashmap
        //at the end, if counter > max, set max to counter
        HashMap<Integer, Integer> map = new HashMap<>(); 
        for(int i=0; i<nums.length; i++){
            map.put(nums[i], i);
        } //fill hashmap with array values
        int max = 0; //longest sequence
        int counter = 0;
        for(int i=0; i<nums.length; i++){
            if(map.get(nums[i]-1)==null){
                //start building sequence
                System.out.println("start building sequence");
                counter++;
                while(map.get(nums[i]+counter)!=null){
                    System.out.println(map.get(nums[i]+counter));
                    counter++;
                    System.out.println("counter = "+counter);
                }
                if(counter>=max){
                    max = counter;
                }
                counter = 0;
            }
        }
        return max;

    }
}
