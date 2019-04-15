class Solution {
    public int fib(int N) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        int ans=0;
        if (map.containsKey(N)){
            return map.get(N);
        }
        
        if (N <2){
            return N;
        }
        else{    
            ans=fib(N-1)+fib(N-2);
        }
        
        map.put(N,ans);
        
        return ans;
        
        
    }
}
