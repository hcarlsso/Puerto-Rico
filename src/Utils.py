def iterate_and_remove(somelist, value):

    for i in reversed(range(len(somelist))):

        element = somelist[i]

        if element == value:
            del somelist[i]
            yield element
