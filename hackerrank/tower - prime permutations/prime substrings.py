# Python 3 program to Find all the
# ways to split the given string
# into Primes.
import time
import sys

primes = [True] * sys.maxsize
maxn = sys.maxsize-1

 
# Sieve of Eratosthenes
def sieve():
 
    primes[0] = primes[1] = 0   
    i = 2
     
    while i * i <= maxn:
        if(primes[i]):
            for j in range(i * i, maxn + 1, i):
                primes[j] = False
        i += 1
# Function Convert integer
# to binary string
def toBinary(n):
 
    r = ""
    while(n != 0):
        if(n % 2 == 0 ):
            r = "0" + r
        else:
            r = "1" + r
        n //= 2
     
    if (r == ""):
        return "0"
    return r
 
# Function print all the all the 
# ways to split the given string
# into Primes.
def PrimeSplit(st):
 
    cnt = 0
     
    # To store all 
    # possible strings
    ans = []
    bt = 1 << (len(st) - 1)
    n = len(st)
 
    # Exponetnital complexity 
    # n*(2^(n-1)) for bit 
    for i in range(bt):    
        temp = toBinary(i) + "0"
        j = 0
        x = n - len(temp)
        while(j < x):
            temp = "0" + temp
            j += 1
         
        j = 0
        x = 0
        y = -1
         
        sp = ""
        tp = ""
        flag = 0
         
        while(j < n):
            sp += st[j]
            if(temp[j] == '1'):            
                tp += sp + ','
                y = int(sp)
                 
                # Pruning step
                if(not primes[y]):
                    flag = 1
                    break
                sp = ""
            j += 1
         
        tp += sp
         
        if(sp != ""):
            y = int(sp)
            if(not primes[y]):
               flag = 1
        
        if(not flag):
           ans.append(tp)
     
    if(len(ans) == 0):
        print (-1)
     
    for i in ans:
        print (i)
 
# Driver code
if __name__ == "__main__":
    start = time.time()
    st = "11373"
    # st = "21373"
    # st = '323'
    # st = '53'
    # st = '5'
    st = '1133311'
    st = '3317771'
    st = '1350297079989171477791892123929141605573631151125933376097791877830238462471373933362476484818693477173990672289892448124097556197582379957168911392680312103962394732707409889862447273901522659'
    sieve()    
    PrimeSplit(st)

    end = time.time()
    total = start-end
    print(total)
 
# This code is contributed by Chitranayal