i = 10
while ( i < 20 ):
    i = i + 2
    print ( i )
    #counts the numbers 1 - 9
    #now prints even number 12- 20

def even():
    evennum = []
    num1=int(input("Enter small Number"))
    num2=int(input("Enter big Number"))
    
    
    for num in range( num1, num2):
        if num1 % 2 == 0:
            evennum.append(num1)
        
    return evennum
print(even())






def reverse_evens():
    rev = even()
    rev.reverse()

    return rev


reee=reverse_evens()
print (reee)













