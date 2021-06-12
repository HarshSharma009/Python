# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:19:54 2020

@author: abcd
"""

import string
import random

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))