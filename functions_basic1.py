def a():
    return 5
print(a())

predicted 5

def a():
    return 5
print(a()+a())

predicted 10

def a():
    return 5
    return 10
print(a())

predicted 5

def a():
    return 5
    print(10)
print(a())

predicted 5

def a():
    print(5)
x = a()
print(x)

I came up with print nothing
It printed 5
           None

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

predicted 3  5  8  #Did not print 8 because the + in the second print is not part of the function?


def a(b,c):
    return str(b)+str(c)
print(a(2,5))

predicted 7     #printed 25. So it just concatinated the two strings.

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

predicted 100 10 


def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3)) 

predicted  7  14  #I did not get the 21. Not sure why this one printed this "print(a(2,3) + a(5,3))"
# and three problems up it did not print this "print(a(1,2) + a(2,3))"


def a(b,c):
    return b+c
    return 10
print(a(3,5))

predicted 8

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

predicted  500 300  # I did not pick up on the second and the last 500


b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

predicted 500 500 300 300 500  # I returned the extra 300

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

predicted 500 500 300  # Definitely need to keep working on these algos!!!

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

predicted 1  2  # I missed the b()function call

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

predicted 1 3 10 5  # Not sure why 5 printed before 10