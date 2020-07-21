x = int(input('Enter a year : '))
def leap(x):
    return (lambda x: print(x,"is a leap year") if x%4==0 and x%100!=0 or x%400==0 else print(x,'is not a leap year'))(x)
leap(x)