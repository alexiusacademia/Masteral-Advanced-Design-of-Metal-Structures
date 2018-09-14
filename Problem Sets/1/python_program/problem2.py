import math
# Given
DL = 40                         # in kips
LL = 20                         # in kips
bolt_diameter = 7.0/8.0
hole_diameter = bolt_diameter + 1.0/8.0
L = 15
bolt_quantity = 3

# Assumptions
hole_distances = 3

# Factored load (required tensile strength)
Pn = 1.2 * DL + 1.6 * LL
print("Pn = " + str(Pn) + ' kips\n')

# From ASTM A36: Standard Specification for Carbon Structural Steel
Fy = 36
Fu = 58

# Sections = (Section_name, Ag, x, t, rx)
sections = [('4x4x1/2', 3.75, 1.18, 0.5, 1.21),
            ('3x3x1/2', 2.75, 0.932, 0.5, 0.898)]

for section in sections:
    print('Try ' + section[0] + ':')
    Ag = section[1]
    x = section[2]
    t = section[3]
    r = section[4]

    print("Slenderness ratio = " + str(L / (r / 12)))

    # Tensile yielding
    print('= = = = = = = = = = = = = = =')
    print('Tensile Yielding\n= = = = = = = = = = = = = = =')
    φtPn_tensile_yielding_lrfd = 0.9 * Fy * Ag * 2
    print("φtPn_tensile_yielding_lrfd = " + str(φtPn_tensile_yielding_lrfd))
    φtPn_tensile_yielding_asd = Fy * Ag / 1.67 * 2
    print("φtPn_tensile_yielding_asd = " + str(φtPn_tensile_yielding_asd))

    # Tensile rupture
    print('= = = = = = = = = = = = = = =')
    print('Tensile Rupture')
    print('= = = = = = = = = = = = = = =')
    U1 = 1 - x / ((bolt_quantity-1) * hole_distances)   # Case 2 From Table D3.1 (Shear Lag factors for Connections to Tension Members)
    U2 = 0.6                                            # Case 8 From Table D3.1 (Shear Lag factors for Connections to Tension Members)
    U = 0

    if U1 > U2:
        U = U1
    else:
        U = U2
    print('U = ' + str(U))
    An = Ag - hole_diameter * t
    Ae = U * An
    φtPn_tensile_rupture_lrfd = 0.75 * Fy * Ae * 2
    print("φtPn_tensile_rupture_lrfd = " + str(φtPn_tensile_rupture_lrfd))
    φtPn_tensile_rupture_asd = Fy * Ae / 2.0 * 2
    print("φtPn_tensile_rupture_asd = " + str(φtPn_tensile_rupture_asd))

    print('x x x x x x x x x x x x x x x x')
    print()

# # Try L4x4x1/2 angle
# print('Try L4x1/2 angles:')
# Ag = 3.75
# x = 1.18
# t = .5
# # For 2 angles spaced 3/8in
# ry = 1.83
# rx = 1.21
# r = rx
# if rx < r:
#     r = rx
# if ry < r:
#     r = ry
#
# print("Slenderness ratio = " + str(L / (r / 12)))
# print()
# # Tensile yielding
# print('= = = = = = = = = = = = = = =')
# print('Tensile Yielding\n= = = = = = = = = = = = = = =')
# φtPn_tensile_yielding_lrfd = 0.9 * Fy * Ag * 2
# print("φtPn_tensile_yielding_lrfd = " + str(φtPn_tensile_yielding_lrfd))
# φtPn_tensile_yielding_asd = Fy * Ag / 1.67 * 2
# print("φtPn_tensile_yielding_asd = " + str(φtPn_tensile_yielding_asd))
#
# # Tensile rupture
# print('= = = = = = = = = = = = = = =')
# print('Tensile Rupture')
# print('= = = = = = = = = = = = = = =')
# U1 = 1 - x / ((bolt_quantity-1) * hole_distances)   # Case 2 From Table D3.1 (Shear Lag factors for Connections to Tension Members)
# U2 = 0.6                                            # Case 8 From Table D3.1 (Shear Lag factors for Connections to Tension Members)
# U = 0
#
# if U1 > U2:
#     U = U1
# else:
#     U = U2
# print('U = ' + str(U))
# An = Ag - hole_diameter * t
# Ae = U * An
# φtPn_tensile_rupture_lrfd = 0.75 * Fy * Ae * 2
# print("φtPn_tensile_rupture_lrfd = " + str(φtPn_tensile_rupture_lrfd))
# φtPn_tensile_rupture_asd = Fy * Ae / 2.0 * 2
# print("φtPn_tensile_rupture_asd = " + str(φtPn_tensile_rupture_asd))
#
