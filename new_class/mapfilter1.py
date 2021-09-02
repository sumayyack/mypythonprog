lst=[2,3,4,5,6]

# sguare of all numbers _map

#def square(num):
#    return num**2
#squares=list(map(square,lst))
#print(squares)


#def cube(num):
#    return num**3
#cubes=list(map(cube,lst))
#print(cubes)


#OR
squares=list(map(lambda num:num**2,lst))
print(squares)


cubes=list(map(lambda num:num**3,lst))
print(cubes)