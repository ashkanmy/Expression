from expression import Variable

a = Variable(1)
b = Variable(2)
c = Variable(3)
d = Variable(4)
e = Variable(5)
f = Variable(6)
g = Variable(7)


#z = a+b+c+d*e
z = a*b+c*d+e
#z = a*b+c*d*e
#z = a*b*c*d*e

z_s = str(z)
#print(z_s)
#print(z.tree) # this should become print(z.expression)
print(z.newTree()) 
