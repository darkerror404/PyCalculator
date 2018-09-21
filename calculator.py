'''Simple Python Calculator'''

#A Function For Add Number
def add(x,y):
    return x + y

#A Function For Minus Number
def minus(x,y):
    return x - y

#A Function For Multiply Number
def multiply(x,y):
    return x * y

#A Function For Divide Number
def divide(x,y):
    return x / y

#Print Zone
print("Choice Your Operator:")
print("1.Add")
print("2.Minus")
print("3.Multiply")
print("4.Divide")

#Input Zone
choice = input("Choice Operator 1/2/3/4 :")

num1 = int(input("First Number"))
num2 = int(input("Second Number"))

#Calculate Function
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,'=', minus(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))

else:
    print("404 Number Not Found")