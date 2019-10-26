
#verify if addition to a subgroup is a partion of the Universal set

def coset():
    
    base_of_universal = int(input("What is the base of the universal set? \n"))
    writing_of_subgroup = input("Specify, the subGroup\n")
    
    #Remove elements of subgroup into subgroup variable
    beginning_of_elements = writing_of_subgroup.index("{") + 1
    elements_of_subgroup = writing_of_subgroup[beginning_of_elements:-1]
    subgroup = elements_of_subgroup.split(",")
    
    #add possible members that will result in partions of universal set
    for member in range(1,base_of_universal+1):
        
        coset=[]
        
        #append sum of member and subgroup element 
        for element_of_subgroup in subgroup:
            coset.append(int(element_of_subgroup) + member)
            
        #verify if its a coset
        if any([element >= base_of_universal for element in coset]):
            break
        
        print(member,'+(',writing_of_subgroup[0],')=', end='')
        print(coset)
    
    print("\nAre cosets of the Universal set, since they are partitions of the set.")
    
    
    
    
    
coset()
    
    