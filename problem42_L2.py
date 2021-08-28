"""
Write a function maxvalue_in_column(pixel_grid)
that, given a list of lists of integers, creates a list of integers that includes the maximum value found in each column of pixel_grid.
You can assume that pixel_grid will always contain at least one row and one column and that the values in pixel_grid will be between 0 and 255
and that each row will contain the same number of columns.
Here are a few examples. After the following code is executed:
If pixel_grid contains	Col_list will be
l1 = [
    [ 4, 2, 3],
    [16, 5, 0],
    [3, 200, 6],
    [0, 10, 12]
  ]

outer index: 0
    inner index: 0
    inner index: 1
    inner index: 2

outer index: 1
    inner index: 0
    inner index: 1inner index: 2

outer index: 2
    inner index: 0
    inner index: 1
    inner index: 2

outer index: 3
    inner index: 0
    inner index: 1
    inner index: 2

for i in range(len(l1) - 1):
    print (l1[inner index][outer index])

output: [ 16, 200, 12 ]

[ [ 4 ],
[ 16 ],
[ 3 ],
[ 0 ] ]	[ 16 ]

[ [ 4, 2, 3] ]	[ 4, 2, 3 ]
[ [6] ]	[ 6 ]
"""
def maxvalue_in_column(pixel_grid):
    if len(pixel_grid) == 1:
        result_list = [max(pixel_grid[0])]

    else:
        main_list = []

        for out_idx in range(len(pixel_grid) - (len(pixel_grid) - len(pixel_grid[0]))):
            sub_list = []

            for in_idx in range(len(pixel_grid[out_idx]) + 1):
                sub_list.append(pixel_grid[in_idx][out_idx])

            main_list.append(sub_list)

        result_list = [max(inner_list) for inner_list in main_list]

    return result_list

pixel_grid = [[ 4, 2, 3],
            [16, 5, 0],
            [ 3, 200, 6],
            [ 0, 10, 12]]

pixel_grid1 = [[ 4, 8 ],
             [ 16, 20 ],
             [ 3, 25 ],
             [ 0, 18 ]]


pixel_grid2 = [[ 4, 2, 3]]
pixel_grid3 = [[6]]

print("Pixel grid is:")

for i in pixel_grid2:
    print(i)

output = maxvalue_in_column(pixel_grid2)print("The maximum values of each column are: ", output)
