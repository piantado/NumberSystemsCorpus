import re
from copy import copy
import types
from Shared import *

class Rule:
	"""
		This implements the a rule, as a list of concatenated strings with
		potentially recursive sub-expansions (involving any pythonic expression of p,q,r)
		Here, the recursive rhs f[x] calls are stored as functions, lambda p,q,r, recurse: ... . Where 
		"recurse" is the recursive call (NumberSystem.f_internal)
	"""
	def __init__(self, p, q, sgn, r, rhs):
		
		self.__dict__.update(locals())
		
		self.raw_rhs = copy(rhs) # before we convert to functions, store this
		
		# compile the function calls on the rhs into the right form, e.g.
		#lambda p,q,r, recurse: recurse(p)
		# so the rhs stores a list of strings, or lambda calls for the recursion
		for i, k in enumerate(self.rhs):
			m = re.match("f\\[(.+)\\]",k) # if it's a recursive call, construct a function to compute it
			if m:
				expr = m.groups(0)[0]
				self.rhs[i] = eval( "lambda p,q,r, recurse: recurse("+expr+")" )
	
	def __str__(self):
		return "Rule(%i,%i,%i,%i -> [%s])" % (self.p, self.q, self.sgn, self.r, " ".join(self.raw_rhs) )
	
	def get_generality(self):
		""" 
			Higher numbers give 'worse' rules in terms of generality.
			This is for choosing the rule which is most specific (e.g. constants first)
		"""
		return (self.p==VAR)+(self.q==VAR)+(self.r==VAR)
		
	def apply_to(self, n, recurse):
		"""
			Attempts to apply this rule to n (using recurse for recursion on the rhs)
			If inapplicable, returns None
		"""
		assert (self.q is not VAR) # this must be specified
		assert isinstance(self.sgn, int)
		
		# first, use check_can_apply to recover the matching pqr, or None if no match
		p,q,r = self.p, self.q, self.r # this stores what the matched pqr are
		
		if n > 0: # only do this if n>0; for n=0, we skip this and require p,q,r=selfs
			if self.p is VAR:
				if self.r is VAR:  p,r = divmod(n, self.q)
				else:              p = (n-self.sgn*self.r) / self.q # integer division, so it may not equal n -- this is checked l8r
			else:
				if self.r is VAR: r = (n-self.p*self.q)*self.sgn
				else:             pass # just fixed
		if p*q+self.sgn*r != n or abs(r) >= q: return None
		
		# Now loop through the RHS, expanding
		ret = ""
		for k in self.rhs: 
			if isinstance(k, types.FunctionType): 
				below = k(p,q,r, recurse)
				if not below: return None # if we failed lower somewhere
				else:         ret = ret + below
			else:                 ret = ret + k # just append this token
		
		return p,q,self.sgn,r, ret
