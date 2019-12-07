#Cayley table, gives the products of two elements of a group, under the group base

'''
*******************Prevented multiple same values********************
'''

def cayley():
    
    #Initialize dictionary to map products and elements, list of elements
    dictionary_of_products={}
    m = int(input("What is M? \n")) 
    user_input = input("Write out the elements of the group, seperated with commas: \n")
    list_of_elements = set(user_input.split(","))
    list_of_elements = list(list_of_elements)
    list_of_elements.sort() #ascend the list, since input was set
    
    #dictionary headers init
    dictionary_of_products[0]=list_of_elements
    
    
    #maps lists of products to "element"
    for element in list_of_elements:
        list_of_product=[]
        
        for operand in list_of_elements:
            product = int(element) * int(operand)
            
            if product<m:
                list_of_product.append(product)
            else:
                list_of_product.append(product%m)
            
        dictionary_of_products[int(element)] = list_of_product
        
    return dictionary_of_products

#constructs the table
cayley = cayley()
print(cayley)
keys = cayley.keys()
count = 0
for element in keys:
    if count ==1: # prints out the horizontal line after first row
        print((len(keys)*2+1)*"-")
    print(str(element)+'|', *cayley[element]) #empties list with spaces
    count +=1




