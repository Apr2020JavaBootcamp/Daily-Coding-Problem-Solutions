'''
Problem:

We say a number is sparse if there are no adjacent ones in its binary representation. 
Do this in faster than O(N log N) time.
For a given input N, find the smallest sparse number greater than or equal to N.
For example, 21 (10101) is sparse, but 22 (10110) is not.
'''

# FUNCTION TO PERFORM THE OPERATION
def get_next_sparse(num):
    binary = bin(num)[2:]

    new_str_bin = ""
    prev_digit = None
    flag = False

    for i, digit in enumerate(binary):
        if (digit == '1' and prev_digit == '1'):
            flag = True

        if (flag):
            new_str_bin += '0' * (len(binary) - i)
            break
        else:
            new_str_bin += digit
        prev_digit = digit

    if (flag):
        if (new_str_bin[0] == '1'):
            new_str_bin = '10' + new_str_bin[1:]
        else:
            new_str_bin = '1' + new_str_bin

    return int(new_str_bin, base=2)

# DRIVER CODE
print(get_next_sparse(21))
print(get_next_sparse(25))
print(get_next_sparse(255))