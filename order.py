

#Order of group
#   This is the number of elements in the group
#Order of an element
#   The order of an element g, is the smallest positive number n, such that g^n = e, where e is the 'group identity' 


def order_of_group():
    user_input = input("Write the elements of the group, seperated by commas \n")
    
    group = user_input.split(',')
    
    #remove spaces(elements that are not numbers)
    num = group.count('')
    for i in range(num):
        group.remove('')
    
    return len(group)


def order_of_element():
    user_input = input("Enter the elements of the group \n")
    group = user_input.split(',')
    
    element = int(input("What element do you want the order of? \n"))
    group_base = int(input("What is the base of the group? \n"))
    group_identity=int(input("What is the group identity? \n"))
    
    #to interate through for powers
    for i in range(1, 100):
        calculation = element**i
        if calculation > group_base and (int(calculation%group_base)==group_identity):
            return i
        
        else:
            if int(calculation%group_base)==group_identity:
                return i
            


#print(order_of_group())
#print("\nThe order is ",order_of_element())
