

num1 = int(raw_input("enter first num"))
num2 = int(raw_input("enter second num"))

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# function  to add two numbers 
def add(x, y):
   return x + y

#  function to subtract two numbers 
def subtract(x, y):
   return x - y

#  function to multiply two numbers
def multiply(x, y):
   return x * y

#  function to divide two numbers
def divide(x, y):
   return x / y


# Take input from the user 
choice = raw_input("Enter choice(1/2/3/4):")


if choice=='1':
	print(num1, "+",num2,"=",add(num1,num2))

elif choice=='2':
	print(num1, "-",num2,"=",add(num1,num2))


elif choice=='3':
	print(num1, "*",num2,"=",add(num1,num2))

elif choice=='4':
	print(num1, "/",num2,"=",add(num1,num2))

else:
	print("invalid output")



