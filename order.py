

#Order of group
#   This is the number of elements in the group
#Order of an element
#   The order of an element g, is the smallest positive number n, such that g^n = e, where e is the 'group identity' 

class Order:
    
    def __init__(self, group, element, base, identity):
        self.group = group
        self.element = element
        self.group_base = base
        self.group_identity = identity
        
        
    def order_of_group(self):
        
        return "\nThe order of the group, is the number of elements in the group, which is: {}".format(len(self.group))

    def order_of_element(self):
        
        #to interate through for powers
        for power in range(1, 100):
            calculation = self.element**power
            
            if calculation < self.group_base:
                print("{}**{} = {}".format(self.element, power, calculation))
                if calculation == self.group_identity:
                    return "\nThe order of {}, is:".format(power)
            
            else:
                calculation = calculation%self.group_base
                print("{}**{} = {}".format(self.element, power, calculation))
                if calculation == self.group_identity:
                    return "\nThe order of {}, is:".format(power)
            

user_input = input("Write the elements of the group, seperated by commas \n").split(",")
element = int(input("What element do you want the order of? \n"))
group_base = int(input("What is the base of the group? \n"))
group_identity=int(input("What is the group identity? \n"))

obj = Order(user_input, element, group_base, group_identity)
print(obj.order_of_group())
print(obj.order_of_element())

