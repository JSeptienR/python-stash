"""

Example of using function and class decorators for caching a function.
Prints Fibonacci series.

"""

def cached(f):
	cache = {}
	def wrapper(x):
		try:
			return cache[x]
		except:
			cache[x] = f(x)
			return cache[x]
	return wrapper


class Cached:
	def __init__(self, f):
		self.f = f
		self.cache = {}

	def __call__(self, x):
		cache = self.cache
		f = self.f
		try:
			return cache[x]
		except:
			cache[x] = f(x)
			return cache[x]


if __name__=='__main__':
	@cached
	def fibo(n):
		if n==0 or n==1:
			return 1
		else:
			return fibo(n-1) + fibo(n-2)
		
	for n in range(1000):
		print(fibo(n))
