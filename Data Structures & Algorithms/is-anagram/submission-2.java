class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<String, Integer> map1 = new HashMap<String, Integer>();
        HashMap<String, Integer> map2 = new HashMap<String, Integer>();
        for(int i=0; i<s.length(); i++){
            char letter = s.charAt(i);
            String str = String.valueOf(letter);
            map1.put(str, map1.getOrDefault(str, 0)+1);
        }
        for(int i=0; i<t.length(); i++){
            char letter = t.charAt(i);
            String str = String.valueOf(letter);
            map2.put(str, map2.getOrDefault(str, 0)+1);
        }

        for(String key: map1.keySet()){
            if(!map1.get(key).equals(map2.get(key))){
                return false;
            }
        }
        if(s.length()==t.length()){
            return true;
        }
        return false;
    }
}
