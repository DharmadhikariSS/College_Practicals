#       Dharmadhikari Satyajeet Sudhir
#       TY CSE Roll No. 30

n = 10
n1, n2 = 0, 1
iteration = 0

print("First 10 Fibonacci numbers:")
while iteration < n:
   print(n1)
   n3 = n1 + n2
   n1 = n2
   n2 = n3
   iteration += 1
