#Default Dict

class Counter(dict):
	"""Increments count whenever a stored key is encountered"""
	def __init__(self, default, *args, **kwargs):
		self.default = default
		super(dict, self).__init__(*args, **kwargs)

	def __missing__(self, key):
		return self.default

	def __setitem__(self, key):
		dict.

	def __getitem__(self, key):
		if key not in self.keys():
			return self.__missing__(key)
		else:
			self.val
			return dict.__getitem__(self, key)

def main():
	"""Do something"""
	x = Counter(0)
	x['a'] = 3
	print x
	print x['a']
	print x['b']

if __name__ == '__main__':
	main()