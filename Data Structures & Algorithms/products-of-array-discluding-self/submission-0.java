class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        int product =1;
        for(int i=0; i<prefix.length; i++){
            if(i>0){
                prefix[i] = nums[i-1]*product;
                product = product * nums[i-1];
            }
            else{
                prefix[i] = product;
            }
        }
        System.out.println(Arrays.toString(prefix));
        product = 1;
        for(int j=suffix.length-1; j>=0; j--){
            if(j<suffix.length-1){
                suffix[j] = nums[j+1]*product;
                product = product * nums[j+1];
            }
            else{
                suffix[j] = product;
            }
        }
        System.out.println(Arrays.toString(suffix));
        for(int i=0; i<nums.length; i++){
            prefix[i] = prefix[i]*suffix[i];
        }
        return prefix;
    }
}  
