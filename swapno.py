

# using thord variabl

"""x=input("ente")
y=input("ente")
temp=0
temp=x
x=y
y=temp
print(x,y)"""

# without third vaibale
"""x=input("ente")
y=input("ente")
x,y = y,x
print(x,y)"""

#  using fumction

# Python Program to Swap Two Numbers

def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    print("After Swapping two Number: {0} and {1}".format(a, b))
num1 = input(" Please Enter the First Value : ")
num2 = input(" Please Enter the Second Value : ")
swap_numbers(num1, num2)
