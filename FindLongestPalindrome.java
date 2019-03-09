class Solution {
    int start=0; int end=0;
    public String longestPalindrome(String s) {
        
        if (s.length()<2)
            return s;
        
        for(int i=0; i< s.length()-1;i++)
        {
    
            central(s,i,i);
            central(s,i,i+1);
        }
       
    
        return s.substring(start,start+end);
        
    }
    public void central(String s, int l, int r){
        
        while (l>=0 && r<s.length() &&s.charAt(l)==s.charAt(r))
        {
            l--;
            r++;
        }
        
        if (end<r-l-1)
        {
            start=l+1;
            end=r-l-1;
            System.out.println(start);
                
        }
    }
}
