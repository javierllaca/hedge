#!/usr/bin/python
# -*- coding: utf-8 -*-

from re import finditer
from sys import stdin

def clean_line(line):
    """Return line without <img> and <a> tags"""
    clean = line
    regex = r'<img(.*?)/>|<a(.*?)</a>'	
    matches = finditer(regex, clean)
    for match in matches:
        clean = clean.replace(match.group(), '')
    return clean

def main():
    """Parse xml and print only content enclosed in <post> tags"""
    post = False
    for line in stdin:
        if any(x in line for x in ['</post', '<quote']):
            post = False
        elif post and line.strip():
            clean = clean_line(line).strip()
            if clean:
                print clean
        elif any(x in line for x in ['<post', '</quote']):
            post = True

if __name__ == '__main__':
    main()
