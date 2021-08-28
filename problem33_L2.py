"""
Write a python function to identify and return the number name of a given number.
The number should be in the range 1 to 1000. If the number is invalid, return -1.
Example:
Sample input	Expected output
1	one
15	fifteen
45	forty five
125	one hundred and twenty five
999	nine hundred and ninety nine
1000	one thousand
1211	-1
"""
def integer_to_english(number):
    string = ""
    search_list = ["units"]

    hundreds = {
        1: "One hundred",
        2: "Two hundred",
        3: "Three hundred",
        4: "Four hundred",
        5: "Five hundred",
        6: "Six hundred",
        7: "Seven hundred",
        8: "Eight hundred",
        9: "Nine hundred"
    }
    tens = {
        1: "Ten",
        2: "Twenty",
        3: "thirty",
        4: "fourty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"

    }

    units = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "Nine"
    }
    if len(str(number))==3:
        search_list=[hundreds,tens,units]
    if len(str(number))==2:
        search_list=[tens,units]
    for digit in str(number):
        string+=search_list[str(number).index(digit)][int(digit)] + " "
        #print(search_list[str(number).index(digit)])
        #print([int(digit)])
    return string
number=333
print(integer_to_english(number))

