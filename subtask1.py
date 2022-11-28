# the codw below shows a number "n" and we try to fing a number "q" that if we atke the square of "q" itis less than or equal to "n" for example, n=99, q=81 (9*9)
# first 1 define my function, where b=0 and a=1
#on line 7, i let b**2 to be greater n and n to be greater than a**2
# line 10 and 11 is a loop that says until we get to the largest squared number less or equal to n, we keep adding 1, but when we get to the largest squared number, we break the loop.
def myFunc(n):
    b=0
    a=1
    
    while(b**2 >n or n>a**2):
        b=b+1
        a=a+1
    q=b**2
    print(q)
        
myFunc(150)   
