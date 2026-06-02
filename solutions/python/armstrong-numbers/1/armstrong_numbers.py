def is_armstrong_number(number):
    # str_num = str(number)
    # res = 0
    # n_digits = len(str_num)
    # for num in str_num:
    #    res += int(num)**n_digits
    # return res == number    

    return sum(int(num)**len(str(number)) for num in str(number)) == number
    
   