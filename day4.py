from math import gcd

a, b = 12, 18
c = 36

lcm = a * b // gcd(a, b)
lcm = lcm * c // gcd(lcm, c)

total = lcm // a + lcm // b + lcm // c

g = gcd(total, lcm)

print(f"Sum = {total // g}/{lcm // g}")
