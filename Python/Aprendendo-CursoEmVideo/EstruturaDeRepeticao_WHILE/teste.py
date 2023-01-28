import random

furniture = ['table', 'chair', 'rack', 'shelf']

#print(furniture[0:4])

furniture2 = furniture[:]
# ['cat', 'bat', 'rat', 'elephant']

furniture2.append('bed')
 
#print(furniture2)
# ['cat', 'bat', 'rat', 'elephant', 'dog']

#print(furniture)
# ['cat', 'bat', 'rat', 'elephant']

number = 3.1415926

#print(round(number, 2))

#print("%.2f" % number)

# print(f'O resultado de PI eh {number:.2f}')

print(random.sample([1, 2, 3, 4], 2))