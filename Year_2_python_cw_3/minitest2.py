#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 11:50:41 2021

@author: Ning Xu
"""

"""
MATH20621 - Mini test 2
Student name: Ning Xu
Student id:   10726153
Student mail: ning.xu-8@student.manchester.ac.uk
"""

# Feel free to add other functions you find useful.

def check(X):
    for i in X:
        if i != 0:
            return True
    return False

# Problem 1
def cross(X, Y):
    """
    Compute the cross-product of two vectors X and Y 
    which are lists containing integers and floats.
    This function can only compute for vectors has less or equal to 3 elements.
    """
    # TODO: add your code
    if len(X)>3 or len(Y)>3:
        raise ValueError("at least one of the vectors contains more than three elements")
    for i in range(len(X)):
        if type(X[i]) != int and type(X[i]) != float:
            raise TypeError("at least one of the vectors contains a non-int ir non-float")
    for i in range(len(Y)):
        if type(Y[i]) != int and type(Y[i]) != float:
            raise TypeError("at least one of the vectors contains a non-int ir non-float")
    while (len(X)<3):
        X.append(0)
    while (len(Y)<3):
        Y.append(0)
    result = [X[1]*Y[2]-X[2]*Y[1],X[2]*Y[0]-X[0]*Y[2],X[1]*Y[0]-X[0]*Y[1]]
    return result

# Problem 2
def magic(L):
    """
    The function checks whether L, a list with n elements, 
    each of which is itself a list with n integer elements 
    satisfing the following conditions:
    the elements in each row sum to the same number s
    the elements in each column sum to the same number s
    the elements along the two diagonals sum to the same number s.
    If it holds, then L is a magic square.
    """
    # TODO: add your code
    sum0 = 0
    for k in L[0]:
        sum0 = sum0 + k  

    for i in range(1,len(L)):
        row = L[i]
        sum1 = 0
        for j in row:
            sum1 = sum1 + j
        if sum1 != sum0:
            return False
    
    sum2 = 0
    for i in L:
        sum2 = sum2 + i[0]    
        
    for j in range(1,len(L[0])):
        sum3 = 0
        for k in L:
            sum3 = sum3 + k[j]
        if sum3 != sum2:
            return False
    
    dia1 = 0
    dia2 = 0
    for i in range(len(L)):
        dia1 = dia1 + L[i][i]
        dia2 = dia2 + L[i][len(L)-i-1]
    if (dia1 != dia2):
        return False
    return True

# Problem 3
def benford(s):
    """
    This function takes a string argument s 
    and can returns a list L of tuples (d, f). 
    Where, d is a nonzero digit between 1 and 9 
    and f is the frequency of that digit 
    appearing first (left-most) in the numbers contained in s. 
    Both d and f should be integers. 
    """
    # TODO: add your code
    result = []
    strings = []
    anum = []
    num = ['0','1','2','3','4','5','6','7','8','9','0']
    st = ''
    count = 0
    num_count = 0
    for i in s:
        if i in num:
            st = st + i
            num_count = num_count + 1
        elif i == '.':
            if count==0:
                count =  1
                st = st + i
            else:
                count = 1
                if num_count != 0:
                    strings.append(st)
                st= '.'
                num_count = 0
        else:
            if st != '' and num_count != 0:
                strings.append(st)
            st = ''
            count = 0
            num_count = 0
    for word in strings:
        for i in word:
            if i in num:
                if int(i)!=0:
                    anum.append(i)
                    break
    
    con = [0,0,0,0,0,0,0,0,0,0]
    for i in anum:
        b = int(i)   
        con[b] = con[b]+1
    maxi = 0
    maxarg = 100
    while check(con):    
        for j in range(10):
            if con[j]> maxi:
                maxi = con[j]
                maxarg = j
            elif con[j] == maxi and j<maxarg:
                maxi = con[j]
                maxarg = j
        result.append((maxarg,maxi))
        con[maxarg] = 0
        maxi = 0
        maxarg = 100
    return  result

# main() function for all the testing
def main():
    # do your testing here
    
    #test for cross(X, Y)
    try:
        L = cross([1, 3.2], [-1.9, 3.7, 2.1, 9])
    except ValueError:
         print("at least one of the vectors contains more than three elements")
    except TypeError:
         print("at least one of the vectors contains a non-int or non-float")
    L = cross([1, 3], [-1.2, 3.2, 2])
    print(L)
    
    #test for magic(L)
    L = [[2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]]
    print(magic(L))
    
    L=[[2,16,13,3],
       [11,5,8,10],
       [7,9,12,6],
       [14,4,1,15]]
    print(magic(L))
    
    L=[[1,3,5],
       [2,6,7],
       [4,1,3]]
    print(magic(L))
    
    #test for benford(s)
    s = "test 123.456.78.003... test 32-16,2.3 .00 test."
    print(benford(s))
    s = "test 345638 ... 890. .098-986 jiug.."
    print(benford(s))
    return
    
main() # call main() function to run all tests