'''------------------------------------------------------------
In this example we receive one parameter (inches). This 
function does not return any data.
-------------------------------------------------------------'''
def in2cm(inches):
    centimeters = inches * 2.54
    print centimeters

in2cm(1)
in2cm(2)
in2cm(10)
print ""

'''------------------------------------------------------------
Function receives one parameter and returns one value
-------------------------------------------------------------'''
def cm2in(centimeters):
    inches = centimeters/2.54
    return inches

i = cm2in(2.54)
print i
i = cm2in(5)
print i
i = cm2in(25.4)
print i
print ""

'''------------------------------------------------------------
Function receives two parameters and returns 2 values
-------------------------------------------------------------'''
def add_div(num1, num2):
    print num1, num2
    a = num1 + num2
    b = num1 / num2
    return a, b

add, div = add_div(10,2)
print add, div
add, div = add_div(num2 = 10, num1 = 2)
print add, div
print ""

'''------------------------------------------------------------
Local variables example. In this case la variable inside the
function changes value, but the outside variable not.
-------------------------------------------------------------'''
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist


# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist
print ""

'''------------------------------------------------------------
Example of defining a global variable
-------------------------------------------------------------'''
def changeme():
    global mylist
    "This changes a passed list into this function"
    mylist = [1,2,3,4]; # This would assig new reference in mylist
    print "Values inside the function: ", mylist


# Now you can call changeme function
mylist = [10,20,30];
changeme();
print "Values outside the function: ", mylist
print ""
