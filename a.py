'''

num = [1,2,3,4,5,6,7,8]

def cube(num):
    for x in num:#using normal for loop
       if x % 2 != 0:
          print(x)
cube(num)
def cube(num):
    return num%2 != 0
#print(list(filter(cube,num)))

print(list(filter(lambda num:num%2 != 0,num)))

'''
names = ['ben','dan','sam','jose']
def greetings(names):
    for x in names:
        print('hello',x)
greetings(names)

print(list(map(lambda x:f'hello {x}',names)))

