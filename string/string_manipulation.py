def func(input_string):

    m = {}

    for i in range(len(input_string)):

        c = input_string[i]

        m[c] = i

    return m

func("Hello World!")