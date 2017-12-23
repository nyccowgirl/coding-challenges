"""You are given an n x n 2D matrix that represents an image. Rotate the image
by 90 degrees (clockwise).

Example:
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be:
rotate_image(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]

b = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
rotate_image(b) =
    [[13, 9, 5, 1],
     [14, 10, 6, 2],
     [15, 11, 7, 3],
     [16, 12, 8, 4]]

>>> rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]

>>> rotate_image([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
[[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]

"""


def rotate_image(lst):
    """Rotate matrix 90 degrees clockwise."""

    length = len(lst)
    rotate = []
    i = 0

    while i < length:
        temp_lst = []
        x = length - 1
        while x >= 0:
            temp_lst.append(lst[x][i])
            x -= 1
        rotate.append(temp_lst)
        i += 1

    return rotate


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
