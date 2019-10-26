

#Cayley table, gives the products of two elements of a group, under the group base

def cayley():
    m = int(input("What is M? \n")) 
    
    first = int(input("What is the first number? \n"))
    second = int(input("What is the second number? \n"))
    
    #returns answer based on m
    calculation = first * second
    if calculation < m:
        return int(calculation)
    return int(calculation % m)
    
print("\n"+str(cayley()))

