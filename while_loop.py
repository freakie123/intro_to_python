i = 10
while ( i < 20 ):
    i = i + 2
    print ( i )
    #counts the numbers 1 - 9
    #now prints even number 12- 20

def even():
    evennum = []
    num2=int(input("Enter Big Number"))
    num1=int(input("Enter Small Number"))
    
    num1
    while( num1 < num2):
        if num1%2 == 0:
            evennum.append(num1)
        
    return evennum







def reverse_evens():
    rev = even()
    rev.reverse()
    return rev
 
print(even())
print (reverse_evens())













