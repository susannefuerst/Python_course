# fill the python code

# 1. assign an integer to the variable x

# 2. assign the content of x to the variable y

# 3. increase the content of x by 13

# 4. decrease the content of y by 3

# 5. assign an empty list to the variable z

# 6. put x and y in this list

# 7. run this file in Python3 and make sure no error occurs

# 8. push this file in your repository

if __name__ == '__main__':
    assert type(x) is int, '1. x is not an integer'
    assert y is x, '2. y is not assigned to the content of x'
    assert type(x) is int, '3. x is not an integer anymore'
    assert type(y) is int, '4. y is not an integer anymore'
    assert type(z) == list, '5. z is not a list'
    assert len(z) <= 2, '6. list length is too long'
    assert len(z) >= 2, '6. list length is too short'
    assert type(z[0]) == int, '6. first element in the list is no integer'
    assert type(z[1]) == int, '6. second element in the list is no integer'
    print('Congratulations, homework successfully solved!')
