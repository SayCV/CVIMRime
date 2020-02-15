#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

"""

import os

SCRIPTS_DIR  = os.path.dirname(os.path.abspath(__file__))
TOP_DIR      = os.path.dirname(SCRIPTS_DIR)

def dict():
	f = open(TOP_DIR+'/dl/im_demo_orig.txt', 'r', encoding='utf-8')
	out=open(TOP_DIR+"/dl/im_demo_fix.txt", "w", encoding='utf-8')
	input = f.readlines()
	dict=[]
	for i in input:
		b=i.strip()
		if b not in dict:
			dict.append(b)
			#out.write(str(b)+'\n')
	#out.close()

	def custom_key(word):
		numbers = []
		cmpstr = word.split('\t')[1]
		for letter in cmpstr:
			numbers.append(letter)
		return numbers

	dict.sort(key=custom_key)
	data = dict
	for i in data:
		out.write(str(i)+'\n')

if __name__ == '__main__':
	
	dict()

