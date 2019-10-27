def direct_product():
    
    main_list=[]
    
    N = input("Write the elements of the first list: \n")
    M = input("Write the elements of the second list: \n")
    
    n = N.split(",")
    m = M.split(",")
    
    begin='' #Initialize for the variable pair
    
    for element in n:
        for value in m:
            pair = tuple(element)+tuple(value)
            
            main_list.append(pair)
            
            if element==value:
                begin = pair
                
    print(begin,"=",end='')
    return main_list


print(direct_product())

