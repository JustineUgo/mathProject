

#Cayley table, gives the products of two elements of a group, under the group base

dictionary_values=[]
def cayley():
    
    dictionary={}
    
    
    m = int(input("What is M? \n")) 
    
    user_input = input("Write out the elements of the group: \n")
    
    list_of_elements = user_input.split(",")
    
    #headers init
    dictionary['0']=list_of_elements
    
    global dictionary_values
    
    #initialize the dictionary to map outputs
    for element in list_of_elements:
        list_of_operations=[]
        
        for operand in list_of_elements:
            calculation = int(element) * int(operand)
            
            if calculation<m:
                
                list_of_operations.append(calculation)
            else:
                list_of_operations.append(calculation%m)
            
        dictionary[int(element)] = list_of_operations
        
        dictionary_values.append(int(element))
    return dictionary

main = cayley()
for element in dictionary_values:
    print(element,main[element])



#print("\n"+str(cayley()))

