#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv, stdin

def split(s, chars):
    "Splits s into lines no longer than a number of characters"
    result = tail = ""
    if len(s) < chars:
        return s
    index = s[0:chars].rfind(' ')
    result += s[0:index + 1] + "\n"
    tail += s[index + 1:]
    return result + split(tail, chars)

def main():
    "Wraps a text file to a maximum character width"
    if len(argv) == 2:
        chars = int(argv[1])
        for line in stdin:
            print split(line, chars),
    else:
        print 'Usage: python %s <characters>' % argv[0]

if __name__ == '__main__':
    main()
