import collections

MAX_RECURSION = 15 # How far down in derivations can we recurse without breaking out?

VAR = -9999 # Used internally to represent p/q/r as a variable (e.g. not specified) in f[...] =

def q(x): return "\""+str(x)+"\""

def islist(x): return isinstance(x,list) or isinstance(x,tuple)

def flatten(l):
	# via http://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists-in-python
	out = []
	for el in l:
		if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
			for sub in flatten(el): out.append(sub)
		else:   out.append(el)
	return out

def is_morpheme(k):
	"""
	For the RHS of rules, check if its a morpheme (instead of a function or a concatenator)
	"""
	return isinstance(k, str) and (k != ',') and (k != '+')
	