# structuralUnstability
Check the classification of two and three dimensional reflexive polytopes for those that are structurally unstable

Structural stability was introduced in [arxiv link] as a means to study the non-solvability of a type of real Monge ampere equation
on singular affine manifolds related to reflexive polytopes. We also check which reflexive polytopes are what we call Li-admissable. A concept first introduced in [https://arxiv.org/abs/2301.12983].

The result of which reflexive polytopes that are structurally unstable, structurally strictly semistable and Li-admissable is contained in stability_d1.txt and stability_d2.txt respectively. The ID's as they are defined by the database Reflexivepolytope('dimension', 'ID') in Sage is shown. If any of the three investigated properties hold for the example, it is written under the ID. If they correspond to a Fano polytope of a non-singular toric Fano, i.e. they are Delzant, that is also shown. In the end the total number of each type is shown. 

The script structStabRef.py generates the data. Changing dimension amounts to setting the variable 'n' in the script. 
