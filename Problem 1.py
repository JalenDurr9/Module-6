Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> list = []
>>> for i in range(0, 10):
	r = random.randrange(20, 30)
	list.append(r)

	
>>> print(list)
[25, 24, 22, 24, 27, 28, 24, 21, 20, 24]
>>> 