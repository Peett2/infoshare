my_tuple = (1, 2, 3)
# my_tuple[1] = 5
# nie zadziała bo tuple

still_tuple = (4,5,6,[7,8])
still_tuple[-1].append(9)
print(still_tuple)

my_tuple = my_tuple + (4,)
# musi zawierać przecinek
print(my_tuple)