"""
Given an integer n, write a python function to return true, if it is possible to represent it as
a sum of the squares of two different integers,else return false.
"""
def check_integer(n):
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if (i*i)+(j*j)==n:
                return True
    else:
         return False

n=20 #17,41,68etc
print(check_integer(n))
#or

def check_squares(number):
    flag = 0
    for i in range(1, number + 1):
        for j in range(i + 1, number + 1):
            if (i * i) + (j * j) == number:
                flag = 1
                break
    if flag == 1:
        return True
    else:
        return False
number = 68
print(check_squares(number))


