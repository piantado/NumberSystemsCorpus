import re
import numpy
from Shared import *
from Rule import *


import pyparsing
from pyparsing import Word, Group, QuotedString, Forward, StringEnd, Optional, Regex, Suppress
# Parser for the rules
f_expr = Regex(r"f\[\s*[\(\)pqr0-9\*\+\\-]+\s*\]") # F[...]
comma_expr = QuotedString("\"", escChar="\\") | f_expr # rhs of rules can be f_exprs and string literals
comma_list = Forward()
bracket_list = Suppress("{") + Group(comma_list) + Suppress("}")
comma_list << (comma_expr|bracket_list) + Optional(Word(",+",max=1) + comma_list)
full_expr = f_expr + Suppress("=") + Group(comma_list)
#x = 'f[p*1000+r] = f[p] , "pin" , {"te" , f[r]}'
#print x, "->", full_expr.parseString( x )
#quit()


class NumberSystem:
	"""
		This implements an entire number system, using a list of rules.
		self.rules stores a list of rules, which are ordered by generality(), and sorted as you add. This also
		supports ordered rules by re-ordering self.rules, since they are checked in order and escaped on match. 
	"""
	
	def __init__(self, trace=False):
		"""
			trace - should we display everything as we compute?
		"""
		self.trace = trace
		self.rules = []
		
	def add(self, r):
		if self.trace: print "# Adding", r
		self.rules.append(r)
		
		#TODO: very inefficient since we sort each time and recompute generality, but good enough for now
		self.rules.sort(key=lambda x: x.get_generality())
	
	
	def all_morphemes(self):
		"""
			Return the set of all morphemes in the language (all things occurring on RHS)
		"""
		all_morphemes = set()
		for r in self.rules:
			for k in filter(is_morpheme, r.rhs): all_morphemes.add(k) # add every non-recursion
			
		return all_morphemes
		
	def number_to_string(self, n, reset_stats=True): 
		"""
			A wrapper for f that resets all our relevant counters
			reset_stats - should we zero out all the stats we are tracking? NOTE: If False, then pay attention to the f_calls counter, since we break out of recursion when this exceed MAX_RECURSION
		"""
		
		if reset_stats:
			self.f_calls = 0 # keep track of the recursive calls
			self.morpheme_count = 0 # keep track of the total number of morphemes (rhs elements)
			self.rule_count = [0] * len(self.rules) # keep track of how many times we use each rule
			self.derivation_morphemes = set() # keep track of how many diff morphemes are used overall 
			
		if self.trace: print "# Converting ", n, "to string!"
		
		return self.f_internal(n)
	
	def f_internal(self, n):
		"""
			The f[n] function we wish to define. Should be used through number_to_string, not 
			called on it's own, since it counts recursion to allow us to break out
		"""
		if (n<0): return None # nothing here
		if self.f_calls > MAX_RECURSION: return None
		else: self.f_calls += 1
		
		if self.trace: print "#", "\t"*self.f_calls, "Calling f[%i]"%n
		
		for ri, rule in enumerate(self.rules):
			
			v = rule.apply_to(n, self.f_internal) # call the rule's apply_to, giving myself as a recursion
			
			if v: 
				p,q,sgn,r, s = v
				
				if self.trace: 
					print "#", "\t"*self.f_calls, "\tMatched ", "%i=%i*%i+%i"%(n,p,q,r), v, rule
				
				# track the stats
				self.morpheme_count += 1
				self.rule_count[ri] += 1
				for k in filter(is_morpheme, rule.rhs): self.derivation_morphemes.add(k) # add every non-recursion
				
				return s # break out
		if n == 0: return " " # We didn't match anything (unless overridden), so default to an empty string that is not None
		else:      return None
		
	def check(self, n=100, verbose=True, check_rule_use=False, check_unique=True):
		"""
			Check the output of this numeral system, making sure that derivations and everything appear to do the right thing.
			Returns True/False depending on whether it successfully works on 1..n
			
			n - the max number we go up to
			verbose - whether or not to echo output, telling what's not defined etc
			check_rule_use - if true, we warn if any rules were not used in 1...n (useful for debugging)
			check_unique - return False if this does not give rise to unique strings
		"""
		
		acculmulated_rule_count = numpy.array([0]*len(self.rules), dtype=int)
		seen_form = set() # what number words have we observed?
		
		for n in range(1,n):
			v = self.number_to_string(n)
			if v is None: 
				if verbose: print "*** ERROR:", n, " does not appear to be defined ***"
				return False # We don't pass
			else:
				if check_unique:
					if (v in seen_form): 
						if verbose: print "# Non-unique derivation of", n
						return False
					else: seen_form.add(v)
				
				acculmulated_rule_count += self.rule_count
				#if verbose: print n, NS.f_calls, NS.morpheme_count, "\""+v+"\""
		
		# Now at the end, warn if any rules were not used:
		if check_rule_use and any(acculmulated_rule_count == 0):
			if verbose: 
				print "# WARNING: The following rules were not used:"
				for k in numpy.where(acculmulated_rule_count==0)[0]: print "#\t", self.rules[k] 
				
			return False
				
		return True
		
	
	def add_rule_from_string(self, l):
		"""
			Parse a rule in the standard format. We'll do just a very simple parser, defined above
			e.g. 
				f[p*100+r] = f[p]+"\'s\u{e}r" , {"te" , f[r]}
		"""
		
		lhs, rhs = full_expr.parseString( l )
		
		r = re.search(r'\s*f\[\s*([0-9]+)\s*\]\s*', lhs)
		if r: # if we match a constant
			q = int(r.groups(VAR)[0])
			p = 1
			r = 0
			sgn = 1
		else: # Now we must extract pqr from lhs. It should be of the form p*q+r or p*q-r 
			p, q, sgn, r = re.search(r"([p0-9]+)\s*\*\s*([q0-9]+)\s*(\+|\-)\s*([r0-9]+)\s*", lhs).groups(VAR) 
			
			p = VAR if p == "p" else int(p) # convert these to VAR symbols
			q = VAR if q == "q" else int(q)
			r = VAR if r == "r" else int(r)
				
			if sgn == "+" or sgn==VAR: sgn=1 # convert sign to a multiplier
			else:                      sgn=-1
			
		# convert structured ParseResults to list
		parsed = [ x.asList() if isinstance(x,pyparsing.ParseResults) else x for x in rhs ] 
		
		if any(map(islist, parsed)): 
			# if we have a sublist, we had brackets in the rule (via our parsing rules)
			# so we must remove, and add a rule with r=0
			self.add(Rule(p,q, sgn, 0, filter(lambda x: not islist(x), parsed) )  )
			
			# and add the normal rule where we unlist
			self.add(Rule(p,q, sgn, r, flatten(parsed)  ))
		else:   
			self.add(Rule(p,q, sgn, r, parsed  ))


		