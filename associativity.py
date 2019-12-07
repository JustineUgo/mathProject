

#associativity 
#(a*b)*c = a*(b*c)

def is_associative(first, second, third):
    
    a = int(first)
    b = int(second)
    c = int(third)
    operator = input("What operator are you testing for, * OR + ? \n")
    
    
    if operator == '*':
        left = (a*b)*c
        right = a*(b*c)
        
        if left == right:
            left_operation = "({}*{})*{} =".format(a,b,c)
            right_operation = "{}*({}*{}) =".format(a,b,c)
            print("{0}{1}\n{2}{3}".format(left_operation, left, right_operation, right))
            
            return "It is closed under associativity"
        return "It is not closed under associativity"
    
    elif operator == '+':
        left = (a+b)+c
        right = a+(b+c)

        
        if left == right:
            left_operation = "({}+{})+{} =".format(a,b,c)
            right_operation = "{}+({}+{}) =".format(a,b,c)
            print("{0}{1}\n{2}{3}".format(left_operation, left, right_operation, right))
            
            return "It is closed under associativity"
        return "It is not closed under associativity"
        
    
a = input("Input the first number, a: ")
b = input("Input the second number, b: ")
c = input("Input the third number, c: ")
    
print(is_associative(a, b, c))
