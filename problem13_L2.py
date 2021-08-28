"""
Write a python function which accepts three numbers and returns True if
a. one of the three numbers is "close" to any one of the other numbers
(differing from a number by at most 1), and
b.Number that is left out is "far", differing from both other values by 2 or more.
Return false if the above mentioned conditions are not satisfied.
Sample Input	Expected Output
4,1,3	True
5,6,7	False
"""
def three_numbers(num1,num2,num3):
    if len([num1,num2,num3])!=len(set([num1,num2,num3])) or num3-num2==1:
        return False
    elif abs(abs(num1-num2)-abs(num3-num2))==1:
        return True
    else:
        return False
print(three_numbers(4,1,3))
