class Solution {

    public String encode(List<String> strs) {
        String str = "";
        if(strs.size() ==0){
            System.out.println("empty!");
            return str;
        }
        for(int i =0; i<strs.size(); i++){
                str = str+String.valueOf(strs.get(i).length())+"#"+strs.get(i);
        }
        System.out.println(str);
        return str;
    }

    public List<String> decode(String str) {
        if(str.length()==0){
            return new ArrayList<String>();
        }
        List<String> l = new ArrayList<>();
        int i =0;
        while(i<str.length()){
            int j = i;
            while(str.charAt(j)!='#'){
                j++;
            }
            int len = Integer.parseInt(str.substring(i, j));
            i=j+1;
            l.add(str.substring(i, i+len));
            i=i+len;
        }
        return l;
    }
}
