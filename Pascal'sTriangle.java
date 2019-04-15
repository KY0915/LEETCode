/*
  Pascal's Triangle using recursion.
  
*/
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> l = new ArrayList<List<Integer>>();
        List<Integer> row = new ArrayList<Integer>();
        List<Integer> list = new ArrayList<Integer>();
        if (numRows==0)
            return l;
        if (numRows==1){
            row.add(1);
            l.add(row);   
            return l;
        }
        else{
            
            list.add(1);
            list.add(1);
            row.add(1);
            l.add(row);
            l.add(list);
            
        }    
            
        helper(l,numRows-1,1);
        return l;
    }

    public void helper(List<List<Integer>> allrows ,int nr,int n) {
        
        
        List<Integer> row = new ArrayList<Integer>();

       
        for (int i=0;i<allrows.get(n).size();i++){
            if(i==0){
                row.add(1);
            }
            else{
                row.add(allrows.get(n).get(i-1)+allrows.get(n).get(i));
            }
        }
        row.add(1);
        allrows.add(row);

        
        
        if (nr-1>n)
            helper(allrows,nr,n+1);

        
        
    }
}

