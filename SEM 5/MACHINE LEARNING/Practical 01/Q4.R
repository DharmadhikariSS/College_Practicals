# Satyajeet Sudhir Dharmadhikari
# TY CSE Roll No. 30
n <- 10
n1 <- 0
n2 <- 1
iteration <- 0

while (iteration < n){
	print(n1)
	n3 <- n1 + n2
	n1 = n2
	n2 = n3
	iteration = iteration +1
}