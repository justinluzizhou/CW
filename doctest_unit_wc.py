def count(input_name):
    """
    >>> count('testinputs/test1')
    (7, 7, 14)
    >>> count('testinputs/test2')
    (10, 10, 47)
    >>> count('testinputs/test3')
    (14, 14, 60)
    >>> count('testinputs/test4')
    (10, 11, 35)
    >>> count('testinputs/fizzbuzz.py')
    (13, 71, 422)
    >>> count('testinputs/rainfall.py')
    (25, 97, 711)
    >>> count('testinputs/test0')
    (0, 0, 0)
    """
    try:
        a = open(input_name, "r")
        total = a.read()
        LineC = total.count('\n')
        WordC = len(total.split())
        a.close()

        b = open(input_name, "rb")
        total = b.read()
        CharC = len(total)
        b.close()

        return LineC, WordC, CharC

    except IOError:
        print("We don’t handle that situation yet!")
        exit(0)

def flagout(flag, LineC, WordC, CharC, filename):
    """
    >>> flagout([1,0,0], 14, 0 ,0, 'testinputs/test1')
    14 testinputs/test1
    >>> flagout([1,1,0], 25, 4 ,90, 'testinputs/test1')
    25 4 testinputs/test1
    >>> flagout([1,1,1], 25, 4 ,90, 'testinputs/test1')
    25 4 90 testinputs/test1
    >>> flagout([1,1,1], 2523, 434 ,290, 'testinputs/rainfall')
    2523 434 290 testinputs/rainfall
    >>> flagout([1,1,1], 1233, 123 ,321, 'testinputs/handsome')
    1233 123 321 testinputs/handsome
    """
    if flag == [1,0,0]:
        print(LineC, filename)
    elif flag == [0,1,0]:
        print(WordC, filename)
    elif flag == [0,0,1]:
        print(CharC, filename)
    elif flag == [0,1,1]:
        print(WordC, CharC, filename)
    elif flag == [1,0,1]:
        print(LineC, CharC, filename)
    elif flag == [1,1,0]:
        print(LineC, WordC, filename)
    elif flag == [1,1,1]:
        print(LineC, WordC, CharC, filename)
    else:
        return

def out(list,flag):
    """
    >>> out(['testinputs/test4'], [1,1,1])
    10 11 35 testinputs/test4
    >>> out(['testinputs/test4'], [1,1,0])
    10 11 testinputs/test4
    >>> out(['testinputs/test4','testinputs/test1'], [1,1,0])
    10 11 testinputs/test4
    7 7 testinputs/test1
    17 18 total
    >>> out(['testinputs/test4','testinputs/test1'], [1,0,0])
    10 testinputs/test4
    7 testinputs/test1
    17 total
    >>> out(['testinputs/test4','testinputs/test1','testinputs/test3'], [1,1,1])
    10 11 35 testinputs/test4
    7 7 14 testinputs/test1
    14 14 60 testinputs/test3
    31 32 109 total
    >>> out(['testinputs/test4','testinputs/test1','testinputs/test3','testinputs/test4'], [1,1,1])
    10 11 35 testinputs/test4
    7 7 14 testinputs/test1
    14 14 60 testinputs/test3
    10 11 35 testinputs/test4
    41 43 144 total
    >>> out(['testinputs/test4','testinputs/test1','testinputs/test3','testinputs/test4','testinputs/rainfall.py'], [1,1,1])
    10 11 35 testinputs/test4
    7 7 14 testinputs/test1
    14 14 60 testinputs/test3
    10 11 35 testinputs/test4
    25 97 711 testinputs/rainfall.py
    66 140 855 total
    >>> out(['testinputs/test4','testinputs/test1','testinputs/test3','testinputs/test4','testinputs/rainfall.py','testinputs/fizzbuzz.py'], [1,1,1])
    10 11 35 testinputs/test4
    7 7 14 testinputs/test1
    14 14 60 testinputs/test3
    10 11 35 testinputs/test4
    25 97 711 testinputs/rainfall.py
    13 71 422 testinputs/fizzbuzz.py
    79 211 1277 total
    >>> out(['testinputs/test4','testinputs/test1','testinputs/test3','testinputs/test4','testinputs/rainfall.py','testinputs/fizzbuzz.py','testinputs/test0'], [1,1,1])
    10 11 35 testinputs/test4
    7 7 14 testinputs/test1
    14 14 60 testinputs/test3
    10 11 35 testinputs/test4
    25 97 711 testinputs/rainfall.py
    13 71 422 testinputs/fizzbuzz.py
    0 0 0 testinputs/test0
    79 211 1277 total

    """
    total_lines, total_words, total_chars = 0, 0, 0
    for filename in list:
        LineC, WordC, CharC = count(filename)
        flagout(flag, LineC, WordC, CharC, filename)
        total_lines += LineC
        total_words += WordC
        total_chars += CharC
    if len(list) > 1:
        flagout(flag, total_lines, total_words, total_chars, 'total')

if __name__ == "__main__":
    import doctest
    # The following command extracts all testable docstrings from the current module.
    doctest.testmod()
