"""
Tom is working in a shop where he labels items. Each item is labelled with a number between
num1 and num2 (both inclusive).
Since Tom is also a natural mathematician, he likes to observe patterns in numbers.
Tom could observe that some of these label numbers are divisible by other label numbers.
Write a Python function to find out those label numbers that are divisible by another label
number and display how many such label numbers are there totally.
Note:- Consider only the distinct label numbers. The list of those label numbers should be
considered as a set.
"""
def check_numbers(num1,num2):
    num_set=set()
    num_list=list(range(num2,num1-1,-1))
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            if num_list[i] % num_list[j]==0:
                num_set.add(num_list[i])
    count=len(num_set)

    return [num_set,count]
num1=2
num2=20
print(check_numbers(num1,num2))




