"""
	Simple checking for the hypotheses.
	
	Use via:
		python check.py ../Languages/birom.py
		
		or
		
		python check.py ../Language/*.py
"""
import numpy
import sys
from NumberSystem import *
from Shared import *
from math import log

			
for f in sys.argv[1:]:
	print "# Loading file ",f
	NS = NumberSystem()
	for k in open(f, 'r'):
		print k
		if re.match("\\s*f\\[", k):
			NS.add_rule_from_string(k.strip())
	
	for n in range(1,100):
		v = NS.number_to_string(n) # call first so we get f_calls
		#print NS.distinct_morphemes
		print q(f), n, NS.f_calls, len(NS.derivation_morphemes), q(v)
	
	NS.check(verbose=True, check_rule_use=True, check_unique=True)


# Curious: what happens if we just load all the rules and scramble them?
"""
import random
NS = NumberSystem()

# Let's load up one of the files
for f in ["barea.py", "birom.py", "boro.py", "car_nicobarese.py", "carib.py"]:
	print "# Loading file ",f
	for k in open("../Languages/"+f):
		if re.match("\\s*f\\[", k): NS.add_rule_from_string(k.strip())

# Now shuffle up
for rrr in xrange(100):
		
	random.shuffle(NS.rules)
	NS.rules.sort(key=lambda x: x.get_generality()) # and sort

	#print NS.check()
	if NS.check():
		#print "HERE", NS.number_to_string(1), NS.check()
		for n in range(1,100):
			v = NS.number_to_string(n, reset_stats=True) # call first so we get f_calls
			print rrr, n, NS.f_calls, len(NS.distinct_morphemes), q(v)
"""
