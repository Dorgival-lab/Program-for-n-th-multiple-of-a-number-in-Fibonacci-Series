# Python Program para encontrar a posição do n \ 'th múltiplo
# de um número k na série Fibonacci
  
def findPosition(k, n): 
    f1 = 0
    f2 = 1
    i =2;  
    while i!=0: 
        f3 = f1 + f2; 
        f1 = f2; 
        f2 = f3; 
  
        if f2%k == 0: 
            return n*i 
  
        i+=1
          
    return 
  
  
# Múltiplo não. 
n = 5; 
# Número de cujo múltiplo estamos encontrando 
k = 4; 
  
print("Position of n\'th multiple of k in"
                "Fibonacci Seires is", findPosition(k,n)); 
  
# Código contribuído por Dorgival Fernando 