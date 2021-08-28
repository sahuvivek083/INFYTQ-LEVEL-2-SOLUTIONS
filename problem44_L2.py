"""
UC Berkley CS61A Fall 2011 Final
The D33P language includes three types of tokens: open parentheses, close parentheses, and integers.
An expression is well-formed if it contains balanced parentheses, and each integer correctly indicates
its depth: the number of nested sets of parentheses that surround that integer.
Implement correct depth, which takes a list of tokens as input and returns True if and only if a prefix
of the input is a well-formed D33P expression.
Assume that the input contains a balanced set of nested parentheses with single-digit positive integers
surrounded by parentheses.You only need to check that the integers indicate the correct depths.
Sample Input	Expected Output
list('(1)')	True
list('(2)')	False
list('((2)((3)))')	True
list('((3)(2))')	False
"""

def check_correct_depth(input_list, depth=0):
    count = 0
    status = ""

    for i in input_list:
        if i == "(":
            count += 1

        if i == ")":
            count -= 1

        if i.isdigit():
            if count == int(i):
                status += "True"

            else:
                status += "False"
                break

    if "False" not in status:
        return True

    else:
        return False

input_list1 = list('(1)')
input_list2 = list('(2)')
input_list3 = list('((2)((3)))')
input_list4 = list('((2)(3))')
input_list5 = list('((3)(2))')
input_list6 = list('(((3)((4))(3))(2)((3)))')

output = check_correct_depth(input_list4)
print ("Input list:", input_list4)
print (output)
