"""

@author:Zizhou Lu
@file: wcfinal.py
@time: 16/01/2020 17:41
@file_desc: word count application
    For example: input "wc -w test1" in terminal
                 outputs the word count of the test1 file

"""

import argparse
import sys

total_lines_num = 0
total_words_num = 0
total_bytes_num = 0
total_chars_num = 0
max_line_length = 0

def rearrange_args(arguments):
    """
    # bubble all the flags
    Args:
        arguments: all the flags

    Returns:
        result_args
    """

    result_args = []
    flag_args = []
    file_args = []

    for a in arguments:
        if a == '-l' or a == '-w' or a == '-c' or a == '-m' or a == '-L':
            flag_args.append(a)
        else:
            file_args.append(a)
    flag_args = list(set(flag_args))
    for flag in flag_args:
        result_args.append(flag)
    for file in file_args:
        result_args.append(file)
    return result_args

def print_wc(is_l, is_w, is_c, is_m, is_L, line, word, byte, char, max_length, file_name):
    """
    # define how to print wc

    Args:
        is_l: line count flag
        is_w: word count flag
        is_c: char count flad
        is_m: max_length flag
        is_L: Longest line count flag
        line: line count
        word: word count
        byte: byte count
        char: char count
        max_length: max_length count
        file_name: the file name

    Returns:
        Result and file name

    """
    line_str = " {:>6}".format(line) if is_l else ""
    word_str = " {:>6}".format(word) if is_w else ""
    byte_str = " {:>6}".format(byte) if is_c else ""
    char_str = " {:>6}".format(char) if is_m else ""
    max_length_str = " {}".format(max_length) if is_L else ""
    file = " {}".format(file_name)
    if is_l is False and is_w is False and is_c is False and is_m is False and is_L is False:
        return " {:>6} {:>6} {:>6} {}".format(line, word, byte, file_name)
    else:
        return line_str + word_str + char_str + byte_str + max_length_str + file



def mini_wc(is_l, is_w, is_c, is_m, is_L, files):
    """
    # How to count line, word, char, max_length, Longest line
    Args:
        is_l: line flag
        is_w: word flag
        is_c: char flag
        is_m: max_length flag
        is_L: Longest line flag
        files:

    Returns:

    """
    global total_lines_num, total_words_num, total_bytes_num, total_chars_num, max_line_length
    try:
        f = open(files)
        lines_num = 0
        words_num = 0
        bytes_num = 0
        chars_num = 0
        store_length = 0
        for line in f.readlines():
            lines_num += 1
            words_num += len(line.split())
            if len(line) > store_length:
                if line[-1:] == '\n':
                    store_length = len(line) - 1
                else:
                    store_length = len(line)
            for letter in line:
                bytes_num += len(letter.encode("utf8"))
                chars_num += len(letter)
        f.close()
        lines_num -= 1
        total_lines_num += lines_num
        total_words_num += words_num
        total_bytes_num += bytes_num
        total_chars_num += chars_num
        max_line_length += store_length
        return print_wc(is_l, is_w, is_c, is_m, is_L, lines_num, words_num, bytes_num, chars_num, store_length, files)
    except IOError:
        return "No such file or directory"


def wc(is_l, is_w, is_c, is_m, is_L, file_list):
    for file in file_list:
        if file is "-":
            while True:
                try:
                    f = open("temp.txt", "w+")
                    message = input()
                    f.write(message)
                    f.close()
                    a = list()
                    a.append("temp.txt")
                    b = wc(flag_l, flag_w, flag_c, flag_m, flag_L, a)
                    if b:
                        print(b)
                except KeyboardInterrupt:
                    sys.exit()
        else:
            print(mini_wc(is_l, is_w, is_c, is_m, is_L, file))
    is_print = True
    if len(file_list) == 1:
        is_print = False
    elif len(file_list) == 0:
        is_print = False
    if is_print:
        return print_wc(is_l, is_w, is_c, is_m, is_L, total_lines_num, total_words_num, total_bytes_num,
                        total_chars_num, max_line_length, "total")
    return None

def WChelp():
    """
    # print the help message
    Returns:

    """
    expected = """
                -c, --bytes            only count bytes
                -m, --chars            only count the character
                -l, --lines            only count lines
                    --files0-from=F    read input from the files specified by
                           NUL-terminated names in file F;
                           If F is - then read names from standard input
                -L, --max-line-length  only count longest lines
                -w, --words            print the word counts
                    --help     display this help and exit
                    --version  output version information and exit
                                                   '"""
    return expected



def WCversion():
    expected = "wc.py Copyright (C) 2018 Software Enigneering Written by T18835ZL(Zizhou LU)"

    return expected

if __name__ == '__main__':

    args = sys.argv
    result_list = []
    for arg in args[1:]:
        result_list.append(arg)

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-c',

                      action='store_true',
                      default=False,
                      help='only count bytes')

    parser.add_argument('-w',

                      action='store_true',
                      default=False,
                      help='only count words')

    parser.add_argument('-l',

                      action='store_true',
                      default=False,
                      help='only count lines')

    parser.add_argument('-L',

                      action='store_true',
                      default=False,
                      help='only count longest lines')

    parser.add_argument('-m',

                      action='store_true',
                      default=False,
                      help='only count the char')
    parser.add_argument('--files0-from', action="append",
                   help="read input from the files specified by NUL-terminated names in file F;If F is - then read names from standard input")
    parser.add_argument('--help', action="store_true", help="display this help and exit")
    parser.add_argument('--version', action="store_true", help="output version information and exit" )
    parser.add_argument('file', help='iput files', nargs='*')
    result = parser.parse_args(rearrange_args(result_list))


    flag_l = result.l
    flag_w = result.w
    flag_c = result.c
    flag_m = result.m
    flag_L = result.L
    flag_fileFrom = result.files0_from
    flag_help = result.help
    flag_version = result.version
    file_arg = result.file

    if flag_help is True or flag_version is True:
        if flag_help is True and flag_version is False:
            print(WChelp())
        elif flag_help is False and flag_version is True:
            print(WCversion())
        else:
            indexOfHelp = result_list.index("--help")
            indexOfVersion = result_list.index("--version")
            if indexOfHelp < indexOfVersion:
                print(WChelp())
            else:
                print(WCversion())
    elif flag_help is False and flag_version is False and flag_fileFrom is not None:
        if flag_fileFrom[0] == '':
            print("python3 wc.py: cannot open '' for reading: No such file or directory")
        elif flag_fileFrom[0] == '-':
            while True:
                try:
                    file_input_from_command = input()
                    a = file_input_from_command.split("\x00")
                    b = a[:len(a) - 1]
                    wc_result = wc(flag_l, flag_w, flag_c, flag_m, flag_L, b)
                    if wc_result:
                        print(wc_result)
                except KeyboardInterrupt:
                    sys.exit()
        else:
            with open(flag_fileFrom[0]) as data:
                a = data.read()
                b = a.split("\x00")
                c = b[:len(b) - 1]
                wc_result = wc(flag_l, flag_w, flag_c, flag_m, flag_L, c)
                if wc_result:
                    print(wc_result)
    else:
        if len(file_arg) == 0:
            print("No such file or directory")
        else:
            wc_result = wc(flag_l, flag_w, flag_c, flag_m, flag_L, file_arg)
            if wc_result:
                print(wc_result)
