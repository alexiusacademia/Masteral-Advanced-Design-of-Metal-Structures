# Problem #1

### I. Problem

Given a non-standard WF shape shown below with ($Fy = 36 ksi$, $Fu = 58 ksi$). The bolts are $\dfrac{3}{4}"$ in diameter. The connection is bolted at the flange and web as shown. Use LRFD method. Use effective gage distance between the flange hole and web hole, $g^*$.

<figure><img src="D:\Personal\Masteral\AdvancedDesignOfMetalStructures\Problem Sets\1\images\section-detail.jpg" /><figcaption>Figure 1.1 Section details</figcaption></figure>



Determine:

1. The value of equivalent gage distance between the web and the adjacent hole $g^*$.
2. The tensile capacity $\phi T_n$ using LRFD method.
3. The allowable tensile load $\dfrac{T_n}{\Omega_t}$ using FS of 1.67 for yielding at gross section and 2.0 for fracture at the connection.
4. Is there a possible failure path if the member is connected at the web only?

### II. Solutions

1. First is to determine the hole diameters of the section. 
   $$
   diameter = \dfrac{3}{4} + \dfrac{1}{8} = \dfrac{7}{8}"
   $$

2. To solve for the equivalent gage distance, $g^*$, half of the flange was first considered (consider this as a leg). Connecting the end of the leg to the end of the web as shown below:

   <figure><img src="D:\Personal\Masteral\AdvancedDesignOfMetalStructures\Problem Sets\1\images\g.jpg" />
       <figcaption>Figure 2.1</figcaption>
   </figure>

   $$
   g^* = 2 \frac{1}{16} + 1 \frac{9}{16} + \frac{7}{16} + \frac{7}{16}
   $$

   <div style="text-align: center; width: 100%; border: 2px solid black; padding: 15px; font-weight: bolder; font-size: 2em;">g* = 4 <sup>1</sup>/<sub>2</sub>"</div>

3. From Figure 1.1, (flattened section), gross sectional area is calculated, $A_g = 23.0 in^2$.

4. Also from figure 1.1, (flattened section), several paths of failures are determined and analyzed, taking into account the non-uniformity of thickness of the section. The following paths are analyzed using `python` programming:

   - A - G
   - C - K
   - A - E - I - F - G

5. Tensile capacity, $\phi_t T_n$ using LRFD method:

   - Calculating yielding at gross section

     $\phi_t Tn = 0.90 \cdot Fy \cdot A_g$, obtains $\phi_t Tn = 745.20 kips$.

   - This analyses of the three (3) paths gives that the path A-G is has the least net area so this path governs and should be analyzed for rupture at connections.
     $$
     A_{net} = A_g - \sum D\cdot t + \sum \dfrac{s^2}{4g}\cdot t
     $$
     $A_{net} = 18.19 in^2$

   - Calculating the tensile capacity for rupture at connection, 
     $$
     \phi_t Tn =  0.75 \cdot Fu \cdot A_{net}
     $$







 obtains $\phi_t Tn = 791.16$. 

 Since yielding at gross section governs, the tensile capacity based on **LRFD** method is

 <div style="text-align: center; width: 100%; border: 2px solid black; padding: 15px; font-weight: bolder; font-size: 2em;">&phi;<sub>t</sub>T<sub>n</sub> = 745.20 kips</div>

6. Allowable tensile load $\dfrac{T_n}{\Omega_t}$ using ASD method

   - Calculating yielding at gross section

$$
\dfrac{T_n}{\Omega} = \dfrac{Fy\cdot A_g}{1.67}
$$
 	obtains $\dfrac{T_n}{\Omega} = 495.81 kips$ 

   - Using the same net area above, tensile rupture at connection,

     $$
     \dfrac{T_n}{\Omega} = \dfrac{Fu \cdot A_{net}}{2.0}
     $$

     obtains $\dfrac{T_n}{\Omega} = 527.44 kips$

     Since yielding at gross section governs as well, the allowable tensile load based on **ASD** is

     <div style="text-align: center; width: 100%; border: 2px solid black; padding: 15px; font-weight: bolder; font-size: 2em;"><sup>T<sub>n</sub></sup>/<sub>&Omega;</sub> = 495.81 kips</div>

7. Possible path failure if member is connected at web only. To find this, first is obtaining the tensile failure at weakest path, removing the holes at the thicker portion of the section then compare it to tensile block shear failure taken at A-C-D-F.

   <figure><img src="D:\Personal\Masteral\AdvancedDesignOfMetalStructures\Problem Sets\1\images\WebConnectionOnly.jpg" style="display: block; width: 75%; margin: auto auto;" /><figcaption>Figure 2.2: Connections at web only</figcaption></figure>

   By calculations, the following are obtained:

   **Tensile rupture at connection at path**

   $\phi_t T_n = 849.07 kips $

   **Block shear capacity**

   $\phi_t T_n = 370.91 kips$

   <div style="text-align: center; width: 100%; border: 2px solid black; padding: 15px; font-weight: bolder; font-size: 1.2em;">Since the block shear capacity is less than the tensile rupture capacity, there will be no path of failure for tensile rupture as the block shear will fail first. Rather, the path will be that of block shear failure.</div>

# Problem # 2

### I. Problem

Select a double angle tension member to carry (40 kips DL) and (20 kips LL), member is (15ft) long and will be connected to any one leg by single line of $\dfrac{7}{8}$" diameter bolts. Use A-36 steel. Assume 3 bolts per line.

### II. Solution

1. Factored load
   $$
   T = 1.2(40) + 1.6(20)
   $$

   $$
   T = 80.00 kips
   $$

2. Section selection

3. Checking for slenderness ration $\dfrac{L}{r} \leq 300$

4. xdfgdfg









References:

American Institute of Steel Construction, Specification for Structural Steel Buildings, 2016

