def fibonacci():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a+b

if __name__ =='__main__':
	fibo = fibonacci()
	for _ in range(10):
		print(next(fibo))
		
