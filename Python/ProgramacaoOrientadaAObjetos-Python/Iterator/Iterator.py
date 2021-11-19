nums = [7,8,9,5]

#For - Iterator function
print('\nfor:')
for i in nums:
    print(i)

#Iter
print('\niter:')
it = iter(nums)
print (it)

#__next__
print('\n__next__')
print(it.__next__())
print(it.__next__())


print(next(it))


# Tutorial disponível no YouTube, pelo canal 'Telusko'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=Dyu08G2l71c&ab_channel=Telusko
