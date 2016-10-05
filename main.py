#!/usr/bin/env python
#
# Decode binary message in Bush's 'Sixteen Stone' album cover.
#

PO = True

def get_file_lines():
    fh = open("cover.data", "r")
    lines = []
    for line in fh:
        lines.append(line)
    fh.close()
    return lines

def get_file_string(reverse=False):
    fh = open("cover.data", "r")
    lines = []
    for line in fh:
        lines.append(line.strip())
    fh.close()
    lines = reverse and reversed(lines) or lines
    return "".join(lines)

def get_letter(binary):
    binary = binary.replace("?", "1") # TODO: switch
    intval = int(binary, 2)
    char = chr(intval)
    if PO: print "Binary:", binary, "Int:", intval, "Char:", char
    return char

def rev(val):
    return val[::-1]

def print_lines(lines, start, length, reverse=False):
    letters = []
    for line in lines:
        line = line.strip()
        bits = reverse and rev(line) or line
        letters.append(get_letter(bits[start:start+length]))
    print "Message:", "".join(letters)

def print_string(string, bit_size):
    print "String:", string, "len:", len(string)
    start = bit_size * -1
    offset = len(string)
    letters = []
    while offset > 0:
        bits = string[start:offset]
        if not bits: break
        #print "bits:", bits, "start:", start, "offset:", offset, "size:", bit_size
        letters.append(get_letter(bits))
        start = start - bit_size
        offset = offset - bit_size
    print "Message:", "".join(letters)


#print_lines(5, 4)

"""
for start in range(0, 6):
    print_lines(get_lines(), start, 8)
"""

print_string(get_file_string(reverse=False), 6)
