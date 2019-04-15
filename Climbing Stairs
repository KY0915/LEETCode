/*
  DP with an array solution for Climbing Stairs
  
*/

class Solution {
    public int climbStairs(int n) {        
    
        HashMap<Integer,Integer> cache=new HashMap<Integer,Integer>();
        int i=3;
        int[] arr=new int[n+1];
        
        
        
        if(n<3){
            return n;
        }
        else{
            arr[0]=0;
            arr[1]=1;
            arr[2]=2;
            while(i<=n){
                arr[i]=arr[i-1]+arr[i-2];
                i++;
            }
            
        }
        
        
        return arr[n];
    }
}
