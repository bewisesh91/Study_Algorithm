def pal(string) :
    n = len(string) - 1
    for i in range(len(string)) :
        if string[i] != string[n-i] :
            return False
        else :
            pass
    
    return True

def recursive_pal(string) :
    if string[0] == string[-1] :
        recursive_pal(string[1:-1])
        return 
    else :
        return False
    
    


test_case = 'aababaa'
print(recursive_pal(test_case))