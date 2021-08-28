"""
Write a Python function to rotate the list of elements by N positions.
The function should return the rotated list.
Sample Input
Input list: [1, 2, 3, 4, 5, 6]
Number of positions to be rotated = 2
Expected Output
[5, 6, 1, 2, 3, 4]
Input list: [1, 2, 3, 4, 5, 6]
Number of positions to be rotated = 4
[3,4,5, 6, 1, 2]Note : Assume that number of positions to be rotated
is always a value >= 0 and <= length of the input list.
"""
def rotate_list(input_list,n):
    output_list=input_list[-n:]

    diff_list=list(set(input_list)-set(output_list))
    output_list.extend(diff_list)
    return output_list
input_list=[1, 2, 3, 4, 5, 6]
output_list=rotate_list(input_list,2)
print(output_list)


