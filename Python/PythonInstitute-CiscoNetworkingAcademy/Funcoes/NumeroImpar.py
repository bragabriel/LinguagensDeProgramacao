def is_prime(num):
    if(num)%2!=0:
        return True
    else:
        return False
        
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
