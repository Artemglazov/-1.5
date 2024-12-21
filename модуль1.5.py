immutable_var = 1,1.5,'string',True
print(immutable_var)
#immutable_var[2] = 5 особенность кортежа - неизменяемость
mutable_list = [1,2,3,False]
mutable_list[-1] = True
mutable_list[0] = 2
mutable_list[1] = 3
mutable_list[2] = 4
print(mutable_list)