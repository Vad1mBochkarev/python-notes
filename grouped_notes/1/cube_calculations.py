def calc_cube_perimeter(side):
    return side * 12

one_cube_perimeter = calc_cube_perimeter(3)

full_length = one_cube_perimeter * 8

print('Необходимый метраж палок для 8 кубов:', full_length)

def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6

    return cube_area


one_cube_area = calc_cube_area(3)

full_area = one_cube_area * 8

print('Необходимая площадь стекла для 8 кубов, кв.м:', full_area)
