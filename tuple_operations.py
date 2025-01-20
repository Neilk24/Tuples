tuple_x = ('tuple', True, 3.14159, 69)
print(tuple_x)

tuple_y = (2, 4, 6, 8, 1, 3, 5, 7, 9, 3, 5, 6, 4, 1, 5, 7, 9)
print(tuple_y)

tuple_y = tuple_y + (6, )
print(tuple_y)
print(tuple_y.count(5))

slicers = tuple_y[7:11]
print(slicers)

skibidi_slicers = tuple_y[:16]
print(skibidi_slicers)



















