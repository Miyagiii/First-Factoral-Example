#Written by TheSpaceCowboy
#Date: 12/08/17
def FirstFactorial(num): 

    nums = []#contains all the numbers which will be used to times togther
    
    for x in range(0,num):#adds all the numbers we will be using to times into an array
        
        nums.append(x)
        
    for x in range(1,len(nums)):#this times togther all the numbers
        
        num = num*nums[x]
        
    return num
     
print(FirstFactorial(int(input())))
















  
