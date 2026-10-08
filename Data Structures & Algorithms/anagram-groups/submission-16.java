class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        int[] charArr = new int[26];
        HashMap<String, String> groupAnagram = new HashMap<String, String>(); 
        List<List<String>> result = new ArrayList<>();
        for(int i=0; i<strs.length; i++){
            if(strs[i].equals("")){
                String empty = Arrays.toString(charArr);
                groupAnagram.put(empty, groupAnagram.getOrDefault(empty, "")+"\"\""+",");
                continue;
            }
            //count frequency
            for(int j=0; j<strs[i].length(); j++){
                char ch = strs[i].charAt(j);
                int x = ch - 'a';
                charArr[x]++; 
            }
            String str_array = Arrays.toString(charArr);
            //use this array as key to hash map
            groupAnagram.put(str_array, groupAnagram.getOrDefault(str_array, "")+strs[i]+",");
            //reset charArr
            Arrays.fill(charArr, 0);
        }

        for(Map.Entry<String, String> entry: groupAnagram.entrySet()){
            System.out.println(entry.getValue());
            String[] temp = entry.getValue().split(",");
            List<String> list = new ArrayList<>(); 
            for(String str: temp){
                if(!str.equals("\"\"")){
                    list.add(str);
                }
                else{
                    list.add("");
                }
            }
            result.add(list);

        }

        return result;

    }
}
