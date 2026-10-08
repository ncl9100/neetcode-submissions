class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int maxFreq = 0; 
        for(int i=0; i<nums.length; i++){
            map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
            if(map.get(nums[i]) > maxFreq){
                maxFreq = map.get(nums[i]);
            }
        }
        //bins for each frequency
        List<Integer>[] buckets = new List[nums.length];
        for(Map.Entry<Integer, Integer> entry: map.entrySet()){
            int freq = entry.getValue();
            //System.out.println("freq = "+freq);
            int item = entry.getKey();
            //System.out.println("key = "+item);
            if(buckets[freq-1]==null){
                buckets[freq-1] = new ArrayList<>();
            }
            buckets[freq-1].add(item);
            System.out.println("plz no error i beg");
        }
        int counter = 0;
        int[] mostFrequent = new int[k];
        for(int i = buckets.length-1; i>=0; i--){
            if(counter==k){
                return mostFrequent;
            }
            if(buckets[i]!=null){
                System.out.println("hooray");
                for(int j = 0; j<buckets[i].size(); j++){
                    mostFrequent[counter] = buckets[i].get(j);
                    counter++;
                }
            }
        }
        System.out.println(counter);
        return mostFrequent;

    }
}
