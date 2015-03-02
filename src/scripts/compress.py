#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv, stdin, stdout

def duplicate(s, bound):
    res = ""
    toks = s.split(",")
    for i in range(bound):
        res += reduce(lambda a, b: a + "," + b, 
                map(lambda s: s + "_%d" % (i + 1), toks)) + ","
    return res[:-1]

def main(bound):
    """Compresses several csv rows into one"""
    i = -1
    buf = ""
    for line in stdin:
        line = line.strip()
        # print duplicated header
        if i == -1:
            print duplicate(line, bound)
        # flush buffer
        elif i % bound == bound - 1:
            print buf + line
			buf = ""
        # compress rows into buffer
        else:
            buf += line + ","
        i += 1

if __name__ == "__main__" and len(argv) == 2:
    main(int(argv[1]))
