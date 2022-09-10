def rotate(string, n):
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """
    string_as_list = []
    new_order = ""

    if n**2 > len(string) ** 2 or n == 0 or string == "":
        return string

    for letter in string:
        string_as_list.append(letter)

    if n > 0:
        for iter in range(n):
            letter_to_rotate = string_as_list.pop(0)
            string_as_list.append(letter_to_rotate)

    if n < 0:
        for iter in range(-n):
            letter_to_rotate = string_as_list.pop(-1)
            string_as_list.insert(0, letter_to_rotate)

    for item in string_as_list:
        new_order += item

    return new_order


string = "bob and julian love pybites!"
expected = "love pybites!bob and julian "
(print(expected, rotate(string, 15)))
