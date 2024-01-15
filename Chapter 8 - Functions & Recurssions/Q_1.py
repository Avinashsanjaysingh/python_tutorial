# Write a program using function to find greatest of three numbers.



def is_prime(x):
    for i in range(2,x):
        if ((x%i) == 0):
            return False
    return True
    
x = int(input("Enter the number: "))
while x < 3:
   x = int(input("Enter the number: "))


if is_prime(x):
    print("Prime")
else:
    print("not prime")



