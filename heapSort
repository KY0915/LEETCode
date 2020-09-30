#How to create a heap and heapSort . for min, change largest to smallest and make smallest the smallest of l and r.
      def heapify(arr,n,i):
          largest=i
          l=2*i+1
          r=2*i+2

          if l< n and arr[l]> arr[i]:
              largest=l
          if r < n and arr[r] > arr[largest]:
              largest=r

          if largest!=i:
              arr[i],arr[largest]=arr[largest],arr[i]
              heapify(arr,n,largest)



      def heapSort(arr):
          n=len(arr)

          for i in range(n//2-1,-1,-1):
              heapify(arr,n,i)

          for i in range(n-1,0,-1):
              arr[0],arr[i]=arr[i],arr[0]
              heapify(arr,i,0)

        
