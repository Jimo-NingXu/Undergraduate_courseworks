"""
MATH20621 - Mini test 1
Student name: Ning Xu
Student id:   10726153
Student mail: ning.xu-8@student.manchester.ac.uk
"""

# Feel free to other functions you find useful.
def prime(n):
    """
    Returns `True` if `n` is a prime number and `False` otherwise.
    This was problem 3 of the week 3 home exercises.
    """
    if n < 2:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True

# Problem 1
def lucasprime(n):
    """
    Return 'True' if n is a lucas_number and a prime number and 'False' otherwise.
    """
    # TODO: add your code
    L0 = 2
    L1 = 1
    lucas_number=[1,2]
    a=n
    while a > 1:
        nxtL=L0+L1
        L0=L1
        L1=nxtL
        a-=1
        lucas_number.append(L1)
    if n in lucas_number and prime(n)==True:
            return(True)
    else:
            return(False)
        
# Problem 2
def twinprime(n):
    """
    Returns A twin prime  𝑝 that is the largest prime number less than n
    and is either 2 less or 2 more than another prime number.
    """
    # TODO: add your code
    Prime_numbers=[]  
    for i in range(1,n+3):
       if prime(i)==True:
          Prime_numbers.append(i)     
          Prime_numbers.sort(reverse=True)
    a=len(Prime_numbers)
    a=int(a)
    for b in range(1,a):
        c=int(Prime_numbers[b-1])
        d=int(Prime_numbers[b])
        if c-d==2:
          return(d)
        else:
           continue
    return(None)

# Problem 3
def credit(n, mode="verify"):
    """
    Check the mode of the input, 
    if the mode is 'verify' or undefined, 
    return 'True' if the number is a valid credit code, return 'False' otherwise.
    If the mode is 'calculate' and the length of input is 15,
    return the single check digit based on the input n,
    return 'None' if the length of the input n is not 15.
    """
    # TODO: add your code


    if mode== 'verify':
         number_list=[]
         number_list2=[]
         total=0
         nlength=len(str(n))
         if nlength==16:
             nvstr=str(n)[0:15]
         for i in range(len(nvstr)):
             if i%2==0:
                 number_list.append(int(nvstr[i])*2)
             else:
                 number_list.append(int(nvstr[i]))
         for i in number_list:
             if len(str(i))==2:
                 number_list2.append((int(str(i)[0]))+int(str(i)[1]))
             else:
                 number_list2.append(i)
         for i in number_list2:
             total=total+i
         if (total+int(str(n)[15]))%10==0:
             return True
         else:
             return False
    if mode== 'calculate':
         number_list3=[]
         number_list4=[]
         nclength=len(str(n))
         ncstr=str(n)
         total=0
         if nclength==15:
             for i in range(15):
                 if i%2==0:
                     number_list3.append(int(ncstr[i])*2)
                 else:
                     number_list3.append(int(ncstr[i]))
             for i in number_list3:
                 if len(str(i))==2:
                     number_list4.append(int(str(i)[0])+int(str(i)[1]))
                 else:
                     number_list4.append(i)
             for i in number_list4:
                 total=total+i
             x=total//10       
             code=10*(x+1)-total
             return (code)
         else:
             return(None)  

# main() function for all the testing
def main():
    print("should return True:   ", lucasprime(2207))
    print("should return False:  ", lucasprime(-7))
    print("should return 29:     ", twinprime(29))
    print("should return True:   ", credit(4578423013769219, 'verify'))
    print("should return False:  ", credit(4578423023769219, 'verify'))
    print("should return 9:      ", credit(457842301376921, 'calculate'))
    
main() # call main() function to run all tests