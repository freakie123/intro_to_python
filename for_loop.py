for i in range (1,11):
    print (i)
#prints range form 1 t0 10 11 exclusive


for j in [1 ,2 ,3]:
    print (j)

#prints 1 2 3

for v in range (0,19):
    print (v)
#prints 1-18



def rep():
    x = 1
    mul = "****"
    while x < 5:
        x = x + 1
        print (mul)


rep()



# Function to demonstrate printing pattern 
def pypart(n): 
    
    # outer loop to handle number of rows 
    # n in this case 
    for i in range(0, n): 
    
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
        
            # printing stars 
            print("* ",end="") 
    
        # ending line after each row 
        print("\r") 
    
# Driver Code 

pypart(4) 


