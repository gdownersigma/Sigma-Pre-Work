# script to return [min,max] from an array without using max() or min()
# author George Downer 07/10/25

test_data = [2, 4, 1, 0, 2, -1]


def find_min_max(num_array):
    minimum = 'x'  # assign default values
    maximum = 'x'

    for number in num_array:
        if minimum == 'x':  # if default value, set them both to first number
            minimum = number
            maximum = number
        if number < minimum:  # if smaller than minimum, becomes minimum
            minimum = number
        if number > maximum:  # if larger than maximum, becomes maximum
            maximum = number

    return [minimum, maximum]


print(find_min_max(test_data))
