class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         ll=[]
#         dl=[]  
#         for log in logs:
#             if log.split(' ')[1].isalpha():            
#                 ll.append(log)
#             else:
#                 dl.append(log)
#         def reorder(log):
#             splitLog=log.split(' ')
#             id,rest=splitLog[0], splitLog[1:]

#             return ' '.join(rest) +' '+ id
        
#         return sorted(ll,key=reorder)+ dl

            def get_keys(log):
                id,rest=log.split(' ', maxsplit=1)
                
                return (0,rest,id) if rest[0].isalpha() else (1,)
            
            return sorted(logs,key=get_keys)
