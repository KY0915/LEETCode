/*
  Pascal's Triangle using Constant Space
*/

class Solution {
    
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<Integer>();
        
        helper(rowIndex,row);
        return row;
    }
    
    public void helper(int rowIndex,List<Integer> row){
      
        if (rowIndex==0){
            row.add(1);
            return;
        }
        if (rowIndex==1){
            row.add(1);

        }  
        int j=1;
        int n=0;
        helper(rowIndex-1,row);
        if(rowIndex>1){
            for(int i=1;i<=rowIndex-1;i++){
                row.add(j++,row.get(i)+row.get(i-1));
                i++;
            }
            if (rowIndex%2==0){
                n=(rowIndex/2) -1;
            }
            else{
                n=(rowIndex/2);
                
            }
            int c=0;
            while(c<rowIndex-1){
                row.remove(j);
                c++;
            }
            
            for(int x=n; x>=0;x--){
                int num=row.get(x);
                row.add(num);
            }
        }
        
        
        
    }
}
