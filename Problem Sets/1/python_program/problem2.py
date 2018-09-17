import math
# Given
DL = 40                         # in kips
LL = 20                         # in kips
bolt_diameter = 7.0/8.0
hole_diameter = bolt_diameter + 1.0/8.0
L = 15
bolt_quantity = 3

# Assumptions
hole_distances = 2

# Factored load (required tensile strength)
Pn = 1.2 * DL + 1.6 * LL
print("Pn = " + str(Pn) + ' kips\n')

# From ASTM A36: Standard Specification for Carbon Structural Steel
Fy = 36
Fu = 58

# Sections = (Section_name, Ag, x, t, rx, main_leg_length)
sections = [('4x4x1/2', 3.75, 1.18, 0.5, 1.21, 4),
            ('4x4x1/4', 1.94, 1.09, 0.25, 1.25, 4),
            ('3x3x1/2', 2.75, 0.932, 0.5, 0.898, 3),
            ('3x3x1/4', 1.44, 0.842, .25, 0.93, 3),
            ('3x2x1/2', 2.25, 0.583, 0.5, 0.924, 3)]

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
    print("φtPn_tensile_yielding_lrfd = " + str(round(φtPn_tensile_yielding_lrfd, 2)))
    φtPn_tensile_yielding_asd = Fy * Ag / 1.67 * 2
    # print("φtPn_tensile_yielding_asd = " + str(round(φtPn_tensile_yielding_asd, 2)))

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
    print('U = ' + str(round(U, 2)))
    An = Ag - hole_diameter * t
    Ae = U * An
    φtPn_tensile_rupture_lrfd = 0.75 * Fu * Ae * 2
    print("φtPn_tensile_rupture_lrfd = " + str(round(φtPn_tensile_rupture_lrfd, 2)))
    φtPn_tensile_rupture_asd = Fu * Ae / 2.0 * 2
    # print("φtPn_tensile_rupture_asd = " + str(round(φtPn_tensile_rupture_asd, 2)))

    # Analysis for block shear
    print('= = = = = = = = = = = = = = =')
    print('Block Shear Failure')
    print('= = = = = = = = = = = = = = =')
    # Assume that distance from center of last bolt to tip of angle bar if 3inches
    dTip = 2
    # Solve for areas
    Agr = 0  # Gross area acted upon by shear
    Agt = 0  # Gross area acted upon by tension
    Anr = 0  # Net area acted upon by shear
    Ant = 0  # Net area acted upon by tension

    Agr = (dTip + hole_distances * (bolt_quantity - 1)) * t
    # Assume bolt is placed in the middle of one leg
    Agt = section[5] / 2 * t
    Anr = Agr - (bolt_quantity - 1 + 0.5) * hole_diameter * t
    Ant = Agt - 0.5 * hole_diameter * t
    print('Agr = ' + str(Agr))
    print('Agt = ' + str(Agt))
    print('Anr = ' + str(Anr))
    print('Ant = ' + str(Ant))

    Tn = 0
    if (Fu * Ant) >= (0.6 * Fu * Anr):
        Tn = (0.6 * Fy * Agr + Fu * Ant) * 2
    else:
        Tn = (0.6 * Fu * Anr + Fy * Agt) * 2
    φtPn_shear_block_capacity_lrfd = 0.9 * Tn
    print('φtPn_shear_block_capacity_lrfd = ' + str(round(φtPn_shear_block_capacity_lrfd, 2)))

    print('x x x x x x x x x x x x x x x x')
    print()

