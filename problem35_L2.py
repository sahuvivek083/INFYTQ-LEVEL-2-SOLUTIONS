"""
[University of Texas CS370 Challenge Spring 2011]

Write a python function which accepts any number in the range of 1 to 4999 (both inclusive) and returns the equivalent roman numeral of it.

Sample input	Expected output
1	            I
1796	        MDCCXCVI
4998	        MMMMCMXCVIII

Here are the basics:
I	The easiest way to note down a number is to make that many marks - little I's. Thus I means 1, II means 2, III means 3.
    However, four strokes seemed like too many....
V	So the Romans moved on to the symbol for 5 - V. Placing I in front of the V — or placing any smaller number in front of any
    larger number — indicates subtraction. So IV means 4. After V comes a series of additions - VI means 6, VII means 7, VIII means 8.
X	X means 10. But wait — what about 9? Same deal. IX means to subtract I from X, leaving 9. Numbers in the teens, twenties and thirties
    follow the same form as the first set, only with X's indicating the number of tens. So XXXI is 31, and XXIV is 24.
L	L means 50. Based on what you've learned, I bet you can figure out what 40 is. If you guessed XL, you're right = 10 subtracted from 50.
    And thus 60, 70, and 80 are LX, LXX and LXXX.
C	C stands for centum, the Latin word for 100. A centurion led 100 men. We still use this in words like "century" and "cent." The subtraction
    rule means 90 is written as XC. Like the X's and L's, the C's are tacked on to the beginning of numbers to indicate how many hundreds
    there are: CCCLXIX is 369.
D	D stands for 500. As you can probably guess by this time, CD means 400. So CDXLVIII is 448. (See why we switched systems?)
M	M is 1,000. You see a lot of Ms because Roman numerals are used a lot to indicate dates. For instance, this page was written in the
    year of Nova Roma's founding, 1998 CE (Common Era; Christians use AD for Anno Domini, "year of our Lord").
    That year is written as MCMXCVIII. But wait! Nova Roma counts years from the founding of Rome, ab urbe condita. By that reckoning Nova
    Roma was founded in 2751 a.u.c. or MMDCCLI.
"""
def change_to_roman(number):
    string=""
    search_list=[]
    units={
        1:'I',2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"
    }
    tens={
        1:"X",2:"XX",3:"XXX",4:"XL",5:"L",6:"LX",7:"LXX",8:"LXXX",9:"XC"
    }
    hundreds={
        1:"C",2:"CC",3:"CCC",4:"CD",5:"D",6:"DC",7:"DCC",8:"DCCC",9:"CM"
    }
    thousands={
        1:"M",2:"MM",3:"MMM"
    }
    if len(str(number))==4:
        search_list=[thousands,hundreds,tens,units]
    if len(str(number))==3:
        search_list=[hundreds,tens,units]
    if len(str(number))==2:
        search_list=[tens,units]
    for digit in str(number):
        string+= search_list[str(number).index(digit)][int(digit)]
    return string
number=2356
print(change_to_roman(number))

