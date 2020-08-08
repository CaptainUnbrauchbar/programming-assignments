






links = (2,(4,(6,())))
rechts = ((((),2),4),6)
fib = (1,(1,(2,(3,(5,(8,()))))))

x = filter(lambda x: x<0, fib)
y = filter(lambda x: x%2, fib)
z = filter(lambda x: x%2 == 0, fib)