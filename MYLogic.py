def prime(n):
    if n%2==0:
        return False
    i = 3
    while i < n//2+1:
        if n % i == 0:
            return False
        i += 2
    return True
n = int(input())
if prime(n):
    print("True")
else:
    print("False")