>>> # menentukan bilangan genap
>>> genap = lambda x: x%2 == 0
>>> list(filter(genap, range(11)))
[0, 2, 4, 6, 8, 10]