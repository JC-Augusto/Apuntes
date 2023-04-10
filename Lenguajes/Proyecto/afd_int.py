'''FD AUTOMATON -- LFP 2S2021'''

def state00( c): 
    '''State0'''
    try:
        if (int(c) > 0 and int(c) < 9):  
            dfa = 1 
        #-1 is used to check for any invalid symbol 
        else:  
            dfa = -1
        return dfa
    except:
        return -1
    

def state01( c):
    '''State1''' 
    try:
        if (int(c) > 0 and int(c) < 9):  
            dfa = 1 
        #-1 is used to check for any invalid symbol 
        else:  
            dfa = -1
        return dfa
    except:
        return -1
   
    
  
def isAccepted(cadena): 
    '''Returns True if the string is valid,
    and False if is not'''
    top = len(cadena)
    count = 0
    # dfa tells the number associated  
    # with the present dfa = state  
    dfa = 0

    while count < top:
        if dfa == 0:
            dfa = state00(cadena[count])
        elif dfa == 1:
            dfa = state01(cadena[count])
        count = count + 1

    if dfa == 1:
        return True
    else: 
        return False
   
    
if __name__ == "__main__" : 
    while True:
        string = input('Ingrese un número entero ')
        if (isAccepted(string)) :
            print("ACCEPTED") 
        else:
            print("NOT ACCEPTED") 