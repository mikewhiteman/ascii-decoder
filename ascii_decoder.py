#!/usr/bin/env python3

import re

def convert_to_char(ascii_values):
	chars = []
	for val in ascii_values:
		val = int(val)
		if val >= 0 and val < 256:
			chars.append(chr(val))
	if chars:
		char_string = ''.join([str(char) for char in chars]) 
		return char_string
	else:
		return "[!] No valid ASCII values found..."

if __name__ == "__main__": 
    waf_text = input("Enter payloda containing ASCII encoding: ")
    ascii_values = re.findall(r'\d+', waf_text)
    output = convert_to_char(ascii_values)
    print(output)