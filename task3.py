#1
x = int(input())
y = int(input())
print(f"{x+y},{x-y},{x*y},{x/y},{x//y},{x%y},{x**y}") 
#2
s = int(input())
print(s%10)
#3
z = int(input())
z1 = z//100
z2 = (z//100) % 10
z3 = z % 10
print(z1 + z2 + z3)
#4
c = int(input())
f = c * 9 / 5 + 32
print(f"{f:.1f}")
#5
a = int(input())
b = int(input())
print(a > b, a < b, a == b, a != b, a >= b )
#6
n = float(input())
print(f"{n ** 0.5:.3f}")
