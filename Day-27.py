# given an integer array, it'll return outputs of unique pairs that sum upto specific value k
# example input pair_sum([1,2,3,4], 4)
# would return (1,3) (2,2)
def pair_sum(arr, k): 
     
    if len(arr) < 2: 
        return arr      
    
    # sets for tracking
    seen = set()  
    output = set() 
    
    for num in arr:
        
        target = k-num 
        
        if target not in seen:  
            seen.add(num)
        else:
            output.add( ((min(num,target)), max(num,target)) ) 

    print( '\n'.join(map(str,list(output))))   

pair_sum([1,3,2,2], 4)