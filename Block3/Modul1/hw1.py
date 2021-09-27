import numpy as np
#Exc.1
a = np.matrix('0.05,0.07,0; 0.05,0,0.06;1,1,1')
b = np.matrix('2250;1400;50000')
x1 = np.linalg.solve(a,b)
print(x1)

#Exc.2
a = np.matrix('1,1,1; -1,1,0;1,0,-1')
b = np.matrix('1328;120;100')
x2 = np.linalg.solve(a,b)
print(x2)


#Exc.3
a = np.matrix('3,0,3; 6,0.25,0;1,0.3333,1')
b = np.matrix('1;1;1')
x3 = np.linalg.solve(a,b)
print(x3)
a = (1/x3[0])
b = (1/x3[1])
c = (1/x3[2])
print(a, b, c)


#Exc.4
#1
a = np.matrix('1,1,1; 9,3,1;1,-1,1')
b = np.matrix('12;54;2')
x = np.linalg.solve(a,b)
print(x)
#2
a = np.matrix('1,1,1; 9,3,1;1,-1,1')
b = np.matrix('12;54;2')
a_inv = np.linalg.inv(a)
y = a_inv.dot(b)
print(y)


#Exc.5
def get_polimon(coord):
    n = len(coord)
    a = np.eye(n, dtype=int)
    b = np.zeros(n, dtype=int)
    s = 0
    for i in coord:
        for k in range(n):
            a[s,k] = i[0]**(n-k-1)
            print(a[s,k])
            print(a)
        b[s] = i[1]
        s +=1
    print(a)
    print(b)
    print(np.linalg.solve(a,b))


coord = [(1,12), (3,54), (-1,2), (10,6)]
get_polimon(coord)