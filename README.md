# structuralUnstability
Check the classification of two and three dimensional reflexive polytopes for those that are structurally unstable

Structural stability was introduced in [arxiv link] as a means to study the non-solvability of a type of real Monge ampere equation
on singular affine manifolds related to reflexive polytopes. 

The result of which reflexive polytopes that are structurally stable is contained in structural_stability_d1.txt and structural_stability_d2.txt respectively. The ID's as they are defined by the database Reflexivepolytope('dimension', 'ID') in Sage is shown together with information regarding their structural stability is shown. If they correspond to a Fano polytope of a non-singular toric Fano, that is also shown. In the end the total number of structurally unstable and semistable ones is shown. 

The script structStabRef.py generates the data. Changing dimension amounts to setting the variable 'n' in the script. 
