num = int(input("Enter a number :"))

if num >= 3:
    for i in range(2,num):
        if num % i==0:
            print(f"{num} is not a Fibonacci number.")
            break
        else:
            print(f"{num} is a Fibonacci number.")
            break
elif  num == 0 or num == 1 or num ==2:
    print("Enter a number bigger than 2")