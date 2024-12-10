"""Se propone el alogitmo de euclides para hallar el maximo comun divisor
gcd(m,n)=gcd(n,m mod n)"""

def euclides(m,n):
    while n!=0:
        r=m%n
        m=n
        n=r
    return m
print(euclides(12,20))