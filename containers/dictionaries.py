#!/usr/bin/env python3


if __name__ == '__main__':
    # Dictionaries store pairs of things, a key and a value.  Keys have to be unique, but you can have replicated
    # values.  Here are a few ways to create dictionaries.
    # https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
    a = {}
    b = {1: 2}  # The key is 1, the value is 2
    c = {2: 'two', 'word': 'stuff'}  # 2 elements, 1st key is 2, value is 'two', 2nd key is 'word', value is 'stuff'
    d = dict()
    print(a, b, c, d)

    # You access the elements of the dictionary like this
    a = {'one': 1, 'two': 2, 'couple': 2}
    print(a['one'])  # a[key] returns value paired with that key

    # You can add a new element like this
    print(a)
    a['three'] = 3
    print(a)

    # And delete like this
    del a['one']
    print(a)

    # If the element already exists, then assignment changes the value
    print(a)
    a['one'] = 123  # changes 1 to 123
    print(a)

    # You can also change a value this way
    a['one'] = a['one'] + 333  # Gets the current value and adds 333
    print(a)

    # Dictionary keys have to be immutable (technically, they have to be hashable, but it usually amounts to the same
    # thing), because of the way that dictionaries work under the hood.  This means that, for example, you can't use a
    # list as a key.
    #a[[1, 2]] = 1  # Uncomment this to see how an immutable type doesn't work as a key

    # But, a tuple will work just fine.
    a[(1, 2)] = 1
    print(a)

    # You can construct dictionaries with dictionary comprehensions.  These work just like list comprehensions.  This
    # example will build a dictionary of numbers and their squares.
    #   This is the equivalent of [x for x in range(10)] for lists,
    #   but notice the curly brackets and the key: value construction
    a = {x: x * x for x in range(10)}
    print(a)

    # Here's another example, also showing the use of the zip function.  This is not how you would do this for real,
    # but it's a good example of how you can build dictionaries from lists.
    a_list = list(range(10))
    b_list = [x * x for x in a]
    my_dict_v1 = {k: v for (k, v) in zip(a_list, b_list)}
    print(my_dict_v1)

    # This is exactly the same as the above (in terms of functionality)
    # just broken down a bit. Notice that list_of_tuples is a generator,
    # not a list - but you can think of it as a list of tuples
    #   zip can take 2 or more lists - but the lists have to be
    #   the same length
    my_dict_v2 = {}
    list_of_tuples = zip(a_list, b_list)  # zip creates a generator that returns tuples
    for k, v in list_of_tuples:
        my_dict_v2[k] = v   # my_dict[key] = value
    print(my_dict_v2)

    # This does the same thing as the above, just all at once
    #   Notice the calculation of the key AND the value from x
    my_dict_v3 = {x: x * x for x in range(10)}
    print(my_dict_v3)

    # There are FOUR ways to loop over all of the elements in a
    #  dictionary: a, a.items(), a.keys(), and a.values()
    # .items gets the key and the value as a pair
    my_dict = {'one': 1, 'two': 2, 'couple': 2}
    for k, v in my_dict.items():
        print('{0} -> {1}'.format(k, v))

    # You can also iterate over the keys or the values.  If you just iterate over the dictionary, then you get the keys.
    print('just dictionary: ', end='')  # The end='' replaces the return with zilch
    for x in my_dict:
        print(x, end=' ')

    # The keys
    print('\nkeys(): ', end='')
    for k in my_dict.keys():
        print(k, end=' ')

    # The keys and use the key to get the corresponding value
    print('\nkeys(), values: ', end='')
    for k in my_dict.keys():
        print("{0} -> {1}  ".format(k, my_dict[k]), end=' ')

    # The values only
    print('\nvalues(): ', end='')
    for v in my_dict.values():
        print(v, end=' ')
    print()
