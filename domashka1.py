
def compar (a, b):
   if a > b:
      print(a)
   else: print(b)

def least (a, b, c):
    if b > a < c:
       print('a is less to b and c')
    elif a > b < c:
       print('b is less to a and c')
    elif b > c < a:
       print('c is less to b and a')
    else:
       pass

def module (x):
    x = abs(x)
    return x

def sum (a, b):
    c = a + b
    print(c)

def positive (n):
    if n > 0:
        print('number is positive')
    elif n == 0:
        print('ERROR - zero is neutral number')
    elif n < 0:
        print('number is negative')


if __name__ == '__main__':
   # compar(2, 3)
   # least(3, 4, 5)
   # modul(-10)
   # sum(2,3)
   # positive(0)