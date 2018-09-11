# Advanced Design of Metal Structures

### Chapter 1: Tension Members

#### 1.1 Nominal Strength

Strength of tension member maybe described in terms of any of the limits states that will govern.

##### 1.1.1 Limit States

1. Yielding of gross section
   $$
   T_n = F_y\cdot A_g
   $$
   *where:*

   $T_n$ - nominal strength

   $F_y$ - yield stress of steel

   $A_g$ - gross cross-sectional area of the member

2. Fracture of the effective net area
   $$
   T_n = F_u\cdot A_e
   $$

   $$
   A_e = U\cdot A_n
   $$

   *where*:

   $F_u$ - specified minimum tensile strength

   $A_e$ - effective net area

   $U$ - reduction coefficient (efficiency factor)

   $A_n$ - net area of cross section (less area of holes)
   $$
   U = 1 - \dfrac{\bar{x}}{L} \leq 0.90
   $$
   *where:*

   $\bar{x}$ - distance of centroid of element to the plane of the load transfer. This shall be $\bar{x}$ or $\bar{y}$ of a section, whichever is higher.

   $L$ - length of connection in the direction of loading

3. Block shear fracture


#### 1.2 Net Area

When the connection is either bolted or riveted, holes must be created at the connection reducing its net area.

**Total size of hole:**

- Standard allowance = $\dfrac{1}{16}$ inch larger than diameter of rivet or bolt
- Damage on the edge during punching = $\dfrac{1}{32}$ inch on 1 side making it $\dfrac{1}{16}$ inch on both
- Summing up, the total deduction or hole diameter is the diameter of bolt or rivet plus $\dfrac{1}{8}$inch ($3.2mm$).

*Note:* This is just one method of making hole in the member. Two (2) other methods are more expensive but produces better strength, although often ignored during the design.



#### 1.3 Staggered Holes

In the case of staggered holes, more than one (1) path should be investigated to determine the controlling section or we could say the weakest section of the member.

<figure><img src="D:\Personal\Masteral\AdvancedDesignOfMetalStructures\Notes\images\Stagered-Holes.jpg" style="display: block; width: 75%; margin: auto auto;"/><figcaption>Figure 1.1: Staggered Holes</figcaption></figure>

From Figure 1.1, distance BC is equal to $s$. In this case, which is a staggered holes connection, we should investigate both the path for AB and AC.

1. For the path AB:

   Net width = AB - (hole diameter + $\dfrac{1}{8}$inch)

2. For the path AC:

   Net width = AB - 2(hole diameter + $\dfrac{1}{8}$inch) + $\dfrac{s^2}{4g}$

