#Cayley table, gives the products of two elements of a group, under the group base

'''
*******************Prevented multiple same values********************
'''

def cayley():
    
    #Initialize dictionary to map products and elements, list of elements
    dictionary_of_products={}
    m = int(input("What is M? \n")) 
    user_input = input("Write out the elements of the group: \n")
    list_of_elements = set(user_input.split(","))
    
    #dictionary headers init
    dictionary_of_products[0]=list(list_of_elements)
    dictionary_of_products[0].sort()
    
    
    #initialize the dictionary to map list of products
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

cayley = cayley()
keys = cayley.keys()
count = 0
for element in keys:
    if count ==1:
        print((len(keys)*2+1)*"-")
    print(str(element)+'|', *cayley[element])
    count +=1




