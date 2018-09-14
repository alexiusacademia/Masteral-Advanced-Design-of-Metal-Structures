import functions.geometries as geom
import functions.arith as arith
from math import *

# Coordinates of all holes with thickness
holes = [(2, 20, 2), (2, 15.5, 0.5), (2, 12.5, 0.5), (2, 6.5, 0.5), (2, 2, 2),
         (5.5, 12.5, 0.5), (5.5, 9.5, 0.5), (8.5, 15.5, 0.5), (8.5, 6.5, 0.5)]

paths = [(0, 1, 2, 3, 4),
         (7, 8),
         (0, 1, 2, 6, 3, 4)]

# Properties
Fy = 36
Fu = 58

net_areas = []

hole_diameter = 7.0/8.0

gross_area = 4 * 2 + 14 * 0.5 + 4 * 2
print("Gross area = " + str(round(gross_area, 2)))
print()

for i in range(len(paths)):
    point_ids = paths[i]

    corrections = 0;

    for j in range(len(point_ids) - 1):
        current_point_id = point_ids[j+1]
        prev_point_id = point_ids[j]

        s = geom.getS(holes[current_point_id], holes[prev_point_id])
        g = geom.getG(holes[current_point_id], holes[prev_point_id])

        correction = pow(s, 2) / (4 * g) * arith.average(holes[current_point_id][2], holes[prev_point_id][2])
        corrections += correction

    hole_areas = 0
    for id in point_ids:
        hole_area = hole_diameter * holes[id][2]
        hole_areas += hole_area

    net_area = gross_area - hole_areas + corrections
    net_areas.append(net_area)

    print("Path " + str(i+1) + ": " + str(round(net_area, 2)) + ' in^2')
    print('\u2211Dt = ' + str(round(hole_areas, 2)) + ' sq.in.', end=', ')
    print('\u2211s^2/4g = ' + str(round(corrections, 2)))
    print('= = = ')

minimum_net_area = net_areas[0]

for na in net_areas:
    if na < minimum_net_area:
        minimum_net_area = na

print("Minimum net area = " + str(round(minimum_net_area, 2)))
print()

print("LRFD Analysis\n= = = = = = =")
φtPn = 0.9 * Fy * gross_area
print('φtPn = ' + str(round(φtPn, 2)) + ' kips =======> Yielding of gross section')
φtPn = 0.75 * Fu * minimum_net_area
print('φtPn = ' + str(round(φtPn, 2)) + ' kips =======> Tensile rupture at connection')

print()
print("ASD Analysis\n= = = = = = =")
Pc = Fy * gross_area / 1.67
print('Pn/\u03A9t = ' + str(round(Pc, 2)) + ' kips =======> Yielding of gross section')
Pc = Fu * minimum_net_area / 2.0
print('Pn/\u03A9t = ' + str(round(Pc, 2)) + ' kips =======> Tensile rupture at connection')

print()
print("Analysis if the connections are in the web only")
print('= = = = = = = = = = = = = = = = = = = = = = = =')

path = (1, 2, 3)
# Length of connection along loading = 6.5 inches
x = .25
L = 6.5
U = 1 - x / L
if U > 0.9:
    U = 0.9
t = 0.5

hole_areas = 3 * hole_diameter * t
An = gross_area - hole_areas
Ae = U * An
φtPn = 0.75 * Fu * Ae
print("φtPn = " + str(round(φtPn, 2)) + " kips")

# Analyze block shear failure to see what will govern
# Case 1 - Path A-C-D-F
# Solve for areas in path
Agr = 0     # Gross area acted upon by shear
Agt = 0     # Gross area acted upon by tension
Anr = 0     # Net area acted upon by shear
Ant = 0     # Net area acted upon by tension

Agr = 2 * 8.5 * t
Agt = 9 * t
Anr = Agr - 1.5 * hole_diameter * t * 2
Ant = Agt - 2 * (0.5 * hole_diameter * t)

shear_yielding = False
Tn = 0

if (Fu * Ant) >= (0.6 * Fu * Anr):
    shear_yielding = True
    Tn = 0.6 * Fy * Agr + Fu * Ant
else:
    shear_yielding = False
    Tn = 0.6 * Fu * Anr + Fy * Agt

φtTn = Tn * 0.9
print("φtTn = " + str(round(φtTn, 2)) + " kips")