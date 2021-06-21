  
def smallest_divisible(number):
    factors = []
    '''
    This part of function obtains factors of all the numbers in range.
    '''
    for n in range(1,number+1):
        current_value = n
        factor = 2
        current_factors = []
        
        while current_value > 1:
            if current_value % factor == 0:
                current_value = current_value / factor
                current_factors.append(factor)
            else: 
                factor += 1
        
        
        '''
        This loop ensures that the only minimum number of factors is a result of previous loop
        '''

        for cf in current_factors:
            if current_factors.count(cf) > factors.count(cf):
                factors.append(cf)

    '''
    This part multiplies all the factors
    '''
    product = 1
    for factor in factors:
        product = product*factor
    return product


# print(divisible(20))
print(smallest_divisible(20))