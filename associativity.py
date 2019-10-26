

#associativity 
#(a*b)*c = a*(b*c)

def is_associative(first, second, third):
    
    a = int(first)
    b = int(second)
    c = int(third)
    operator = input("What operator are you testing for? \n")
    
    
    if operator == '*':
        left = (a*b)*c
        right = a*(b*c)
        
        if left == right:
            return "It is closed under associativity"
        return "It is not closed under associativity"
    
    elif operator == '+':
        left = (a+b)+c
        right = a+(b+c)

        
        if left == right:
            return "It is closed under associativity"
        return "It is not closed under associativity"
        
    
a = input("Input the first number: ")
b = input("Input the second number: ")
c = input("Input the third number: ")
    
print(is_associative(a, b, c))
