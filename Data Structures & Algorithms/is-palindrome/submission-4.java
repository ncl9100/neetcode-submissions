class Solution {
    public boolean isPalindrome(String s) {
        String clean_string = s.replaceAll("[^a-zA-Z0-9]", "");
        System.out.println(clean_string);
        int i=0; int j = clean_string.length()-1;
        System.out.println("j = "+j);
        while(i<j){
            if(!(clean_string.substring(i, i+1).toLowerCase().equals(clean_string.substring(j, j+1).toLowerCase()))){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
