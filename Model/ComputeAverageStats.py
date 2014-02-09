"""
	Compute some average stats for each language. 
	
	TODO: This will be updated with what measures we want
"""

import numpy
import sys
from NumberSystem import *
from Shared import *
from math import log

Ns = numpy.array( range(1,101) )
def p(n): return 1.0/(n*n) ##TODO: NORMALIZE CORRECTLY

for f in sys.argv[1:]:

	NS = NumberSystem()

	for k in open(f, 'r'):
		
		if re.match("\\s*f\\[", k): NS.add_rule_from_string(k.strip())

	expected_length = 0.0
	expected_recurse = 0.0
	for n in Ns:
		v = NS.number_to_string(n)
		expected_length += float(NS.morpheme_count) * p(n)
		expected_recurse += float(NS.f_calls) * p(n)
	
	M = len(NS.all_morphemes())

	print q(f), expected_length, expected_recurse, M