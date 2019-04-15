/*
reverse a string using recursion.

*/

class Solution {
    public char[] reverseString(char[] s) {
        
        
        return helper(s,0,s.length-1);
    }    
    
    public char[] helper(char[] s,int start, int end){
        
        
        if (start>end)
            return s;
        char temp=s[start];
        s[start]=s[end];
        s[end]=temp;
        
        start++;
        end--;
        
        
        return helper(s,start,end);
        
    }
}
